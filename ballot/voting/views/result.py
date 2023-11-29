from django.shortcuts import render, redirect
from voting.models import PoliticalParty, Voter
from voting.utils import has_voted_percentage
from ballot.settings import BALLOT_OPEN
from django.db.models import Sum

def results(request):
    percentage_function = has_voted_percentage()
    total_voters = percentage_function["total_voters"]
    if BALLOT_OPEN == False:
        parties = PoliticalParty.objects.all()
        winner = PoliticalParty.objects.order_by('-votes').first()
        parties_votes = PoliticalParty.objects.aggregate(Sum('votes'))
        print(parties_votes)
        blank_votes = int(total_voters) - int(parties_votes["votes__sum"])
        context = {"parties":parties, "blank_votes":blank_votes, "winner":winner}
        return render(request, 'result.html', context)
    else:
        percentage_voters = percentage_function["percentage_voters"]
        context = {"total_voters":total_voters, "percentage_voters":percentage_voters}
        return render(request, 'result_partial.html', context)

