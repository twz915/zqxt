from django.db import transaction
from django.http import HttpResponseRedirect as redirect
from django.db.models import F
from iclick.models import Link


def click_count(request, token):
    with transaction.atomic():
        try:
            link = Link.objects.select_for_update().filter(token=token).first()
        except Link.DoesNotExist:
            pass
        else:
            to_url = link.to_url
            if to_url:
                link.count = F('count') + 1
                link.save()
                return redirect(to_url)
        return redirect('/')
