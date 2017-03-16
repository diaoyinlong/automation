from WebTest.Page.BasePage import BasePage


class EvalPage(BasePage):
    @property
    def bad_eval(self):
        return self.browser.find_element_by_css_selector('#rating_bad')

    @property
    def mid_eval(self):
        return self.browser.find_element_by_css_selector('#rating_common')

    @property
    def good_eval(self):
        return self.browser.find_element_by_css_selector(self.good_eval_css)

    @property
    def good_eval_css(self):
        return '#rating_good'

    @property
    def eval_content(self):
        return self.browser.find_element_by_name('content')

    @property
    def submit_eval(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_110_35 inline m_r55 btn_submit"]')

    @property
    def quality(self):
        return self.browser.find_elements_by_css_selector('input[name="quality"]')

    @property
    def quality_1(self):
        return self.quality[4]

    @property
    def quality_3(self):
        return self.quality[2]

    @property
    def ship_time(self):
        return self.browser.find_elements_by_css_selector('input[name="shipInTime"]')

    @property
    def ship_time_1(self):
        return self.ship_time[4]

    @property
    def ship_time_3(self):
        return self.ship_time[2]

    @property
    def service(self):
        return self.browser.find_elements_by_css_selector('input[name="service"]')

    @property
    def service_1(self):
        return self.service[4]

    @property
    def service_3(self):
        return self.service[2]

    @property
    def pay_speed(self):
        return self.browser.find_elements_by_css_selector('input[name="shipInTime"]')

    @property
    def pay_speed_1(self):
        return self.pay_speed[4]

    @property
    def pay_speed_3(self):
        return self.pay_speed[2]

    @property
    def receive_speed(self):
        return self.browser.find_elements_by_css_selector('input[name="service"]')

    @property
    def receive_speed_1(self):
        return self.receive_speed[4]

    @property
    def receive_speed_3(self):
        return self.receive_speed[2]

    @property
    def reset(self):
        return self.browser.find_element_by_css_selector('a[class="btn_gray_110_35 inline btn_reset"]')

    @property
    def eval_btn(self):
        return self.browser.find_element_by_css_selector(self.eval_order_btn_css)

    @property
    def eval_order_btn_css(self):
        return 'a[class="btn_evaluate btn_gray_41_24"]'

    @property
    def edit_eval_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_edit_evaluate btn_gray_70_24"]')

    @property
    def look_book_eval_link(self):
        return self.browser.find_element_by_css_selector('tbody > tr > td.wd98.font14 > p.m_t10 > a')

    @property
    def look_auction_eval_link(self):
        return self.browser.find_element_by_css_selector('tbody > tr > td.last > p:nth-child(2) > a')

    @property
    def reply_eval_text_area(self):
        return self.browser.find_element_by_css_selector('textarea[name="recontent"]')

    @property
    def reply_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_submit btn_orange_110_35 inline m_r55"]')

    @property
    def delete_reply_link(self):
        return self.browser.find_element_by_css_selector(self.delete_reply_link_css)

    @property
    def delete_reply_link_css(self):
        return 'a[class="f_right btn_delReply"]'

    @property
    def my_reply_message(self):
        return self.browser.find_element_by_css_selector(
                'div.user_box.pd0 > div:nth-child(3) > table > tbody > tr > td:nth-child(1) > div.gray.m_t15')

    @property
    def edit_eval_link(self):
        return self.browser.find_element_by_css_selector('a[class="f_right"]')
