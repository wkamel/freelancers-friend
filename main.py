from downloader.controller import DownloaderController
from saver.saver import Saver


class OffersFeeder(object):
    def __init__(self):
        self.downloader_ctrl = DownloaderController()
        self.saver = Saver()

    def feed(self):
        offers = self.downloader_ctrl.get_offers()
        self.saver.save_offers(offers)

if __name__ == '__main__':
    print "ff"
    feeder = OffersFeeder()
    feeder.feed()
    print "ff"
