from django.contrib.auth.models import Group

def is_moderator(request):
    if request.user.is_authenticated:
        is_moderator = request.user.groups.filter(name="Moderateur").exists()
        return {'is_moderator':is_moderator}
    return {'is_moderator': False}