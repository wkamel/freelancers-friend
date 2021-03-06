from item_offer import ItemOffer
import requests


class iDownloader(object):

    def __init__(self):
        self.offers_items = []
        self.ItemOffer = ItemOffer
        self.requests = requests

    def get_offers(self):
        if not self.offers_items:
            self.download_offers()

        return self.offers_items

    def download_offers(self):
        assert False, "method not implemented!"

    def add_item(self, id, title, description, link):
            item = self.ItemOffer(
                id=id,
                title=title,
                description=description,
                url=self.get_offer_url(link),
                source=self.name
            )
            self.offers_items.append(item)

    def get_url(self):
        if not self._url:
            raise Exception("Url not set")
        return self._url

    def get_offer_url(self, param):
        return "%s%s" % (self.offers_url, param)
