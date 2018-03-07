from urllib.request import urlopen,Request
import json
from .hotel_offer import HotelOffer

class OffersManager:	
	
	def __init__(self, initial_base_url):
		self.base_url = initial_base_url
	
	def get_offer(self, params):
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
		
		for element in data['offers']['Hotel']:
			hotel_offer = HotelOffer()
			hotel_offer.name = element['hotelInfo']['hotelName']
			hotel_offers.append(hotel_offer)
		
		return hotel_offers
