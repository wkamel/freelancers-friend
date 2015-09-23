from ..idownloader import iDownloader
from bs4 import BeautifulSoup


class PythonforumDownloader(iDownloader):
    name = "stackoverflow"
    offers_url = "http://careers.stackoverflow.com"

    def __init__(self):

        """
         This url is for params:
         keywords: python
         location: Allows remote
         sorting: Most recent
        """
        self._url = "https://pl.python.org/forum/index.php?board=9.0"

        super(PythonforumDownloader, self).__init__()

    def download_offers(self):
        url = self.get_url()
        rq = self.requests.get(url)

        for offer in self.parse_html(rq.content):
            self.add_item(offer['id'],
                          offer['title'],
                          offer['description'],
                          offer['link'])

    def parse_html(self, html):
        page = BeautifulSoup(html, 'html.parser')
        offers = []
        for item in page.find_all('tr', class_="windowbg2"):
            link = item.find("a")
            title = unicode(link.contents[0])
            description = "brak"
            msg_id = item.find("span")['id'].split("_")
            id = msg_id[1]

            offers.append({
                'id': id,
                'link': link['href'],
                'title': title,
                'description': description,
            })

        return offers
