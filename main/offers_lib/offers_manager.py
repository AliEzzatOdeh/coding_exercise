from urllib.request import urlopen,Request
import json
from .hotel_offer import HotelOffer

class OffersManager:	
	
	OFFERS = 'offers'
	HOTEL = 'Hotel'
	HOTEL_INFO = 'hotelInfo'
	LOCALIZED_HOTEL_NAME = 'localizedHotelName'
	HOTEL_IMAGE_URL = 'hotelImageUrl'
	HOTEL_STAR_RATING = 'hotelStarRating'
	HOTEL_URLS = 'hotelUrls'
	HOTEL_INFOSITE_URL = 'hotelInfositeUrl'
	HOTEL_PRICING_INFO = 'hotelPricingInfo'
	AVERAGE_PRICE_VALUE = 'averagePriceValue'
	TOTAL_PRICE_VALUE = 'totalPriceValue'
	CURRENCY = 'currency'

	def __init__(self, initial_base_url):
		self.base_url = initial_base_url
	
	def get_offers(self, params):
		offers = []
		try:
			header = { 'User-Agent' : 'aliezzat' }
			req = Request(self.base_url, headers=header)
			serialized_data = urlopen(req).read()
			data = json.loads(serialized_data)
			offers = self.parse_api_json(data)
		except:
			print("error while trying to get offers")

		return offers
	
	def parse_api_json(self, data):
		hotel_offers = []
		
		for element in data[self.OFFERS][self.HOTEL]:
			hotel_offer = HotelOffer()
			hotel_offer.name = element[self.HOTEL_INFO][self.LOCALIZED_HOTEL_NAME]
			hotel_offer.image_url = element[self.HOTEL_INFO][self.HOTEL_IMAGE_URL]
			hotel_offer.star_rating = element[self.HOTEL_INFO][self.HOTEL_STAR_RATING]
			hotel_offer.website_url = element[self.HOTEL_URLS][self.HOTEL_INFOSITE_URL]
			hotel_offer.average_price_per_night = element[self.HOTEL_PRICING_INFO][self.AVERAGE_PRICE_VALUE]
			hotel_offer.total_price = element[self.HOTEL_PRICING_INFO][self.TOTAL_PRICE_VALUE]
			hotel_offer.currency = element[self.HOTEL_PRICING_INFO][self.CURRENCY]
			hotel_offers.append(hotel_offer)
		
		return hotel_offers
