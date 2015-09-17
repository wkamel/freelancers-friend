import unittest
# from .downloader.downloader_builder import DownloaderController
from downloader.downloader_builder import DownloaderBuilder
from downloader.modules.freelancer import FreelancerDownloader
from downloader.item_offer import ItemOffer, ItemOfferMissingParamException


class TestDownloaderBuilder(unittest.TestCase):

    def test_add_downloader(self):
        """ test adding downloaders to builder """
        d_builder = DownloaderBuilder()
        self.assertEqual(len(d_builder.downloaders), 0)
        d_builder.add_downloader(FreelancerDownloader)
        self.assertEqual(len(d_builder.downloaders), 1)

    def test_add_offeritem_no_params(self):
        """ test creating ItemOffer """
        self.assertRaises(ItemOfferMissingParamException, ItemOffer)

    def test_add_offeritem_no_param(self):
        """ test creating ItemOffer """
        item = ItemOffer(
            id="abc444",
            title="Test name",
            description="Test description bla",
            url="http://test.com",
            source="test_source"
        )
        self.assertEqual(item.source, "test_source")

    def test_get_offers(self):
        """ test downloading offers and store in array of ItemOffers"""

        d_builder = DownloaderBuilder()
        d_builder.add_downloader(FreelancerDownloader)
        d_builder.get_offers()
