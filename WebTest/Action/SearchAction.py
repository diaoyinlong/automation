from WebTest.Page.SearchPage import SearchPage
from Module import Uri


class SearchAction:
    def __init__(self):
        self.searchPage = SearchPage()

    # 搜索
    def search(self, area, keyword):
        self.searchPage.go_to(Uri.SearchPage)
        if area == 'book':
            self.searchPage.area_tab[0].click()
        if area == 'auction':
            self.searchPage.area_tab[1].click()
        self.searchPage.search_txt.send_keys(keyword)
        self.searchPage.search_btn.click()

    # 获取第一个搜索结果
    def get_first_search_result(self, area):
        return area == 'book' and self.searchPage.book_first_result.text or self.searchPage.auction_first_result.text
