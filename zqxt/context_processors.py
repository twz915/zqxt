from django.conf import settings as original_settings


def settings(request):
    return {'settings': original_settings}


def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}
