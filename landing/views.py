from django.shortcuts import render


def vitalcen_landing_view(request):
    context = {}
    return render(request, 'landing/vitalcen.html', context)
