from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # aquí se define el tipo de campo que se usará por defecto para los modelos de esta app
    name = 'apps.accounts' # aquí se define el nombre de la app, que es el mismo que el de la carpeta donde se encuentra
