from django.shortcuts import render


def vitalcen_landing_view(request):
    context = {}
    return render(request, 'landing/vitalcen.html', context)


def terms_view(request):
    context = {'title': '| Terms'}
    return render(request, 'landing/terms.html', context)
