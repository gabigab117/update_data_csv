import csv
import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction

from account.models import UserData


logger = logging.getLogger(__name__)
User = get_user_model()


class Command(BaseCommand):
    help = "Update User Data from csv file"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The file to import data from")

    def handle(self, *args, **options):
        try:
            csv_file = options["file"]
            with open(csv_file) as csvfile:
                data = list(csv.DictReader(csvfile))
                users = User.objects.in_bulk([row["User"] for row in data])
                users_data_to_create = []
                users_data_to_update = []

                for row in data:
                    pk = int(row["User"])
                    user = users.get(pk)
                    if user:
                        index = row.get("Data")
                        if not index:
                            logger.critical(f"Aucune data pour {user}")
                        else:
                            try:
                                user_data: UserData = UserData.objects.get(user=user)
                                user_data.index = index
                                users_data_to_update.append(user_data)
                            except ObjectDoesNotExist:
                                users_data_to_create.append(UserData(user=user, index=index))
                    else:
                        logger.critical(f"Le PK --> {pk} n'existe pas")
            with transaction.atomic():
                if users_data_to_create:
                    UserData.objects.bulk_create(users_data_to_create)
                if users_data_to_update:
                    UserData.objects.bulk_update(users_data_to_update, ["index"])
            self.stdout.write(
                f"Opération réalisée avec succès mais n'oubliez pas de lire le fichier de logging. "
                f"{len(users_data_to_create)} utilisateurs créés et "
                f"{len(users_data_to_update)} utilisateurs mis à jour")

        except FileNotFoundError:
            self.stderr.write("Fichier non Trouvé")
