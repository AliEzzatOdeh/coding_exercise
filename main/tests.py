from django.test import TestCase
from .offers_lib.offers_manager import OffersManager

class OffersTestCase(TestCase):
    
    def setUp(self):
        self.base_url = "https://offersvc.expedia.com/offers/v2/getOffers?scenario=deal-finder&page=foo&uid=foo&productType=Hotel"
        self.offers_manager = OffersManager(self.base_url)

    def test_check_url_return_offers(self):
        zero_count = 0
        offers = self.offers_manager.get_offers([])
        print (len(offers))
        self.assertNotEqual(zero_count, len(offers))