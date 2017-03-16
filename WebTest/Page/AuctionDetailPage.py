from WebTest.Page.BasePage import BasePage


class AuctionDetailPage(BasePage):
    @property
    def bid_to_buy_btn(self):
        return self.browser.find_element_by_id('normalBid_box').find_element_by_css_selector(
                'a[class="f_left btn_price "]')

    @property
    def bid_success_msg_css(self):
        return 'div[class="bid_suc_ico"]'

    @property
    def bid_success_msg_txt(self):
        return self.browser.find_element_by_css_selector(self.bid_success_msg_css).text

    @property
    def agent_bid_rdo(self):
        return self.browser.find_element_by_css_selector('#agentBid')

    @property
    def normal_bid_rdo(self):
        return self.browser.find_element_by_css_selector('#normalBid')

    @property
    def set_agent_bid_btn(self):
        return self.browser.find_element_by_id('agentBid_box').find_element_by_css_selector(
                'a[class="f_left btn_price"]')

    @property
    def check_all_chk(self):
        return self.browser.find_element_by_id('check_all')

    @property
    def batch_delete_fav_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_gray_60_21 batchDelete_btn"]')

    @property
    def batch_delete_fav_confirm(self):
        return self.browser.find_element_by_id('batchDeleteWin').find_element_by_css_selector(
                'a[class="subBtn f_left"]')

    @property
    def add_to_fav_btn(self):
        return self.browser.find_element_by_id('btn_add_to_favorite')

    @property
    def add_to_fav_success_txt(self):
        return self.browser.find_element_by_id('setFavoriteSucWin').find_element_by_css_selector(
                'div[class="text"]').text

    @property
    def first_fav_auction_row(self):
        return self.browser.find_element_by_css_selector('#auction_box > tr')
