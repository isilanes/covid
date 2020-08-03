from django.contrib.auth.decorators import login_required

from ..get.insert import handle_insert_get


@login_required
def handle_insert_post(request, WhichForm):
    form = WhichForm(request.POST)
    if form.is_valid():
        form.save()

    return handle_insert_get(request)
