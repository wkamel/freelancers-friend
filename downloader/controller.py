from downloader_builder import DownloaderBuilder
from downloader.modules.freelancer import FreelancerDownloader
from downloader.modules.guru import GuruDownloader
from downloader.modules.stackoverflow import StackoverflowDownloader


class DownloaderController(object):
    offers = []
    downloaders = []

    def __init__(self):
        self.d_builder = DownloaderBuilder()
        self.add_downloaders()

    def add_downloaders(self):
        self.d_builder.add_downloader(FreelancerDownloader)
        self.d_builder.add_downloader(GuruDownloader)
        self.d_builder.add_downloader(StackoverflowDownloader)

    def get_offers(self):
        for downloader in self.d_builder.downloaders:
            self.add_offers_list(downloader.get_offers())

        return self.offers

    def add_offers_list(self, offers):
        self.offers += offers
