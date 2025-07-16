from django.shortcuts import render, get_object_or_404, redirect
from nfc.models import Tisch, Speise, Bestellung

def tisch_view(request, tisch_id):
    tisch = get_object_or_404(Tisch, id=tisch_id)
    speisen = tisch.restaurant.speisen.all()
    return render(request, 'vbusiness/tisch.html', {
        'tisch': tisch,
        'speisen': speisen,
    })

def home(request):
    return render(request, 'vbusiness/home.html')

def bestellung_absenden(request, tisch_id):
    tisch = get_object_or_404(Tisch, id=tisch_id)
    if request.method == 'POST':
        speise_ids = request.POST.getlist('speisen')
        if speise_ids:
            bestellung = Bestellung.objects.create(tisch=tisch)
            bestellung.speisen.set(Speise.objects.filter(id__in=speise_ids))
            bestellung.save()
            return render(request, 'vbusiness/tisch.html', {
                'tisch': tisch,
                'speisen': tisch.restaurant.speisen.all(),
                'message': 'Bestellung erfolgreich gesendet!'
            })
        else:
            return render(request, 'vbusiness/tisch.html', {
                'tisch': tisch,
                'speisen': tisch.restaurant.speisen.all(),
                'message': 'Bitte mindestens eine Speise auswählen.'
            })
    return redirect('tisch_view', tisch_id=tisch_id)
