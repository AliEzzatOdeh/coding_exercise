from django.shortcuts import render
from .offers_lib.offers_manager import OffersManager
from .offers_lib.hotel_offer import HotelOffer

def index(request):

    return render(request,'index.html')

def offers(request):
    offers_manager = OffersManager("https://offersvc.expedia.com/offers/v2/getOffers?scenario=deal-finder&page=foo&uid=foo&productType=Hotel") 
    hotel_offers = offers_manager.get_offers(request.GET)
    return render(
        request,
        'offers.html',
        context={'offers':hotel_offers, 'start_date':request.GET.get(offers_manager.START_DATE), 'end_date':request.GET.get(offers_manager.END_DATE), 'length_of_stay':request.GET.get(offers_manager.LENGTH_OF_STAY)}
    )