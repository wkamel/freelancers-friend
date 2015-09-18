from ..idownloader import iDownloader


class FreelancerDownloader(iDownloader):
    name = "freelancer"
    offers_url = "https:/www.freelancer.com"

    def __init__(self):

        # TODO - cut more of unnecessary params from url
        self._url = "https://www.freelancer.com/ajax/table/project_contest_datatable.php?"
        self._url += "sEcho=8&iColumns=35&sColumns=&iDisplayStart=0&iDisplayLength=100&iSortingCols=1&iSortCol_0=6"
        self._url += "&sSortDir_0=desc&bSortable_0=false&bSortable_1=false&bSortable_2=false&bSortable_3=true"
        self._url += "&bSortable_34=false&keyword=&featured=false&fulltime=false&nda=false&qualified=false&sealed=false"
        self._url += "&urgent=false&guaranteed=false&highlight=false&private=false&top=false&type=&budget_min=false"
        self._url += "&budget_max=false&hourlyrate_min=false&hourlyrate_max=false&skills_chosen="
        self._url += "&verified_employer=false&bidding_ends=N%2FA&bookmarked=false&countries=false&languages="
        self._url += "&hourlyProjectDuration=false&advancedFilterPanelView=&disablePushState=true"
        self._url += "&pushStateRoot=%2Fwork%2Fpython&lat=false&lon=false&local=false"
        self._url += "&location=%5Bobject+Object%5D&ul=pl&uc=19"
        self._url += "&tag=python&xpbonus_catIds=15%2C51%2C92%2C106%2C673%2C113%2C335%2C9%2C343%2C31%2C63%2C305%2C3%2C13%2C400%2C68%2C101%2C10%2C236"
        self._url += "&jobIdEnable=on&status=open&_=1441908051372"

        super(FreelancerDownloader, self).__init__()

    def download_offers(self):
        url = self.get_url()
        rq = self.requests.get(url)

        offers = rq.json()['aaData']
        for offer in offers:
            item = self.ItemOffer(
                id=offer[0],
                title=offer[1],
                description=offer[2],
                url=self.get_offer_url(offer[21]),
                source=self.name
            )
            self.offers_items.append(item)
