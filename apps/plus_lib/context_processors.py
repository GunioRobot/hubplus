
from django.conf import settings

def configs(context):
    # This function is a context processor to load the base.html template with some other standard 
    # values pulled from local_settings.py

    return {

        'COPYRIGHT_HOLDER' : settings.COPYRIGHT_HOLDER,
        'PROJECT_THEME': settings.PROJECT_THEME,
        'WELCOME_PAGE' : 'clients/%s/welcome.html' % settings.PROJECT_THEME,
        }