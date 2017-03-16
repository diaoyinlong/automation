from WebTest.Page.BasePage import BasePage


class SearchPage(BasePage):
    @property
    def search_txt(self):
        return self.browser.find_element_by_id('q')

    @property
    def search_btn(self):
        return self.browser.find_element_by_id('btn_search')

    @property
    def area_tab(self):
        return self.browser.find_element_by_class_name('area_tit').find_elements_by_tag_name('a')

    @property
    def book_first_result(self):
        return self.browser.find_element_by_class_name('result_tit')

    @property
    def auction_first_result(self):
        return self.browser.find_element_by_class_name('lb_tit')
