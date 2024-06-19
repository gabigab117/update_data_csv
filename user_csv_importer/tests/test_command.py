from io import StringIO
import pytest

from django.core.management import call_command


@pytest.mark.django_db
def test_creation_data(user_1, user_2, user_3):
    out = StringIO()
    call_command("update_data", "user_csv_importer/tests/csv_test_alluser_alldata.csv", stdout=out)
    message = ("Opération réalisée avec succès mais n'oubliez pas de lire le fichier de logging. "
               "3 utilisateurs créés et 0 utilisateurs mis à jour")
    assert message in out.getvalue()


@pytest.mark.django_db
def test_two_creations_and_one_update_data(user_1, user_2, user_3, user_data_1):
    out = StringIO()
    call_command("update_data", "user_csv_importer/tests/csv_test_alluser_alldata.csv", stdout=out)
    message = ("Opération réalisée avec succès mais n'oubliez pas de lire le fichier de logging. "
               "2 utilisateurs créés et 1 utilisateurs mis à jour")
    assert message in out.getvalue()
