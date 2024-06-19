# Mise à jour des données utilisateur à partir d'un fichier CSV

Ce projet est un script Django qui met à jour les données utilisateur à partir d'un fichier CSV.

## Dépendances

```bash
asgiref==3.8.1
Django==5.0.6
iniconfig==2.0.0
mypy==1.10.0
mypy-extensions==1.0.0
packaging==24.1
pluggy==1.5.0
pytest==8.2.2
pytest-django==4.8.0
ruff==0.4.9
sqlparse==0.5.0
typing_extensions==4.12.2
```

## Utilisation

Pour utiliser ce script, vous devez passer le chemin du fichier CSV en argument lors de l'exécution de la commande.

```bash
python manage.py update_user_data "chemin_vers_votre_fichier.csv"
```

# Fonctionnement

Le script ouvre le fichier CSV et lit les données. Il récupère ensuite tous les utilisateurs correspondant aux
identifiants présents dans le fichier CSV.

Pour chaque ligne du fichier CSV, le script vérifie si l’utilisateur existe. Si c’est le cas, il tente de récupérer les
données de l’utilisateur. Si les données existent, elles sont mises à jour. Sinon, de nouvelles données sont créées pour
l’utilisateur.

Toutes les opérations de mise à jour et de création sont effectuées dans une transaction pour garantir l’intégrité des
données.

# Logs

Le script génère des logs pour chaque opération. Assurez-vous de consulter les logs pour obtenir des informations
détaillées sur le déroulement de l’opération.

# Erreurs

Si le fichier CSV n’est pas trouvé, le script affiche un message d’erreur.

