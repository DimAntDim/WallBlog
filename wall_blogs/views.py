from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.methos == 'POST':
        pass
    else:
        pass

