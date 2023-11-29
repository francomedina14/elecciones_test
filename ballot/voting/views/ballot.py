from django.shortcuts import render
from voting.models import PoliticalParty, Voter
from ballot.settings import BALLOT_OPEN

def initial_form(request):
    if BALLOT_OPEN == True:
        return render(request, 'index.html', {"message": 'Bienvenido'})
    else:
        return render(request, 'close.html')

def ballot_form(request):
    dni = request.POST["dni"]
    try:
        voter = Voter.objects.get(dni=dni)
        if voter.has_voted == False:
            parties = PoliticalParty.objects.all()
            context = {"parties":parties, "voter":voter}
            return render(request, 'ballot.html', context)
        return render(request, 'index.html', {"message":'Usted ya ha votado o no se encuentra en el Padron Electoral'})
    except Voter.DoesNotExist:
        return render(request, 'index.html', {"message":'Usted ya ha votado o no se encuentra en el Padron Electoral'})

def vote(request, voter_id):
    party_id = request.POST["party_id"]
    try:
        party = PoliticalParty.objects.get(pk=party_id)
        party.votes += 1
        voter = Voter.objects.get(pk=voter_id)
        voter.has_voted = True
        party.save()
        voter.save()
        return render(request, 'index.html', {"message": 'Bienvenido'})
    except PoliticalParty.DoesNotExist:
        return render(request, 'index.html', {"message": 'Bienvenido'})