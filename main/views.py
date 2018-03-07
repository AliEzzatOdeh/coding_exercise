from django.shortcuts import render
from .offers_lib.offers_manager import OffersManager
from .offers_lib.hotel_offer import HotelOffer

def index(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html'#,
        #context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

def offers(request):
    offers_manager = OffersManager("https://offersvc.expedia.com/offers/v2/getOffers?scenario=deal-finder&page=foo&uid=foo&productType=Hotel") 
    hotel_offers = offers_manager.get_offer("")
    return render(
        request,
        'index.html'#,
        #context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )