from django.conf import settings # import the settings file

def api_key(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'API_KEY': settings.API_KEY}
