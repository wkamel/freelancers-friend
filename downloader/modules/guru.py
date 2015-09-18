from ..idownloader import iDownloader
import xml.etree.ElementTree as ET
import urllib2


class GuruDownloader(iDownloader):
    name = "guru"
    offers_url = ""

    def __init__(self):

        self._url = "http://www.guru.com/rss/jobs/q/python/"

        super(GuruDownloader, self).__init__()

    def download_offers(self):
        url = self.get_url()
        rq = urllib2.Request(url)
        u = urllib2.urlopen(rq)
        tree = ET.parse(u)
        root = tree.getroot()
        channel = root.find('channel')

        for offer in channel.findall('item'):
            title = offer.find('title').text
            link = offer.find('link').text
            description = offer.find('description').text
            id = self.gen_id(link)
            self.add_item(id, title, description, link)

    def gen_id(self, link):
        link = link
        id = link[link.rfind('/')+1:]
        return id
