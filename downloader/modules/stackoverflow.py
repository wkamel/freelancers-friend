from ..idownloader import iDownloader
from bs4 import BeautifulSoup


class StackoverflowDownloader(iDownloader):
    name = "stackoverflow"
    offers_url = "http://careers.stackoverflow.com"

    def __init__(self):

        """
         This url is for params:
         keywords: python
         location: Allows remote
         sorting: Most recent
        """
        self._url = "http://careers.stackoverflow.com/jobs?searchTerm=python&allowsremote=true&sort=p"

        super(StackoverflowDownloader, self).__init__()

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
        for item in page.find_all('div', class_="-item"):
            link = item.find("a", class_="job-link")
            title = unicode(link.contents[0])
            description = unicode(item.find("p", class_="text _muted"))
            id = unicode(item['data-jobid'])
            offers.append({
                'id': id,
                'link': link['href'],
                'title': title,
                'description': description,
            })

        return offers
