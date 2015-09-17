from idownloader import iDownloader


class DownloaderBuilder(object):
    downloaders = set()
    offers = []

    def __init__(self):
        pass

    def add_downloader(self, downloader):
        assert issubclass(downloader, iDownloader), (
            "Error on adding downloader: %s is not using iDownloader interface!" % downloader.__name__
        )

        self.downloaders.add(downloader())
