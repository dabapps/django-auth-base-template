from django.conf import settings


def auth_base_template(request):

    if request.user.is_authenticated():
        base_template = settings.LOGGED_IN_BASE_TEMPLATE
    else:
        base_template = settings.LOGGED_OUT_BASE_TEMPLATE

    return {'auth_base_template': base_template}
