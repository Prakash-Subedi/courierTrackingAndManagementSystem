from django.shortcuts import render

from .models import Branch


def branch(request):
    branch_details = Branch.objects.all()

    return render(request, 'branches.html', {'branch_details': branch_details})