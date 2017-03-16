from WebTest.Page.BasePage import BasePage


class BookStorePage(BasePage):
    @property
    def add_to_cart_btn(self):
        return self.browser.find_element_by_css_selector('#addCart')

    @property
    def add_to_fav_btn(self):
        return self.browser.find_element_by_css_selector('#favoriteBook')

    @property
    def go_to_cart_btn(self):
        return self.browser.find_element_by_css_selector('a[class="f_left btn_orange_205"]')

    @property
    def check_all_cart_prod_chk(self):
        return self.browser.find_element_by_css_selector('#all_sec_2')

    @property
    def settle_prod_btn(self):
        return self.browser.find_element_by_css_selector('#btn_settle_accounts')

    @property
    def create_order_btn(self):
        return self.browser.find_element_by_css_selector('#btn_create_order')

    @property
    def create_success_msg(self):
        return self.browser.find_element_by_id('msgText')

    @property
    def add_prod_to_fav_btn(self):
        return self.browser.find_element_by_css_selector(self.add_prod_to_fav_css)

    @property
    def add_prod_to_fav_css(self):
        return '#favoriteBook'

    @property
    def go_to_prod_fav_btn(self):
        return self.browser.find_element_by_id('favoriteBookOverWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def check_all_fav_chk(self):
        return self.browser.find_element_by_css_selector('#check_all_sec')

    @property
    def batch_delete_cart_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_batch_del_cart_book"]')

    @property
    def batch_delete_fav_prod_btn(self):
        return self.browser.find_element_by_css_selector('#btn_batch_delete_product')

    @property
    def add_book_to_fav_success_msg(self):
        return self.browser.find_element_by_css_selector(
            '#favoriteBookOverWin > div > div.overWinCon > div.overWinText > div > p')

    @property
    def add_shop_to_fav_success_msg(self):
        return self.browser.find_element_by_css_selector(
            '#kfz_favorite_shop_public_over_win > div > div.overWinCon > div.overWinText > div > p')

    @property
    def fav_prod_item_box(self):
        return self.browser.find_element_by_css_selector('#product_list_box > tr')

    @property
    def report_link_css(self):
        return '#book_info > div > div:nth-child(6) > a'

    @property
    def report_link(self):
        return self.browser.find_element_by_css_selector(self.report_link_css)

    @property
    def report_type_1(self):
        return self.browser.find_element_by_css_selector('#rep_type_1')

    @property
    def report_content_box(self):
        return self.browser.find_element_by_css_selector('#description')

    @property
    def file_upload(self):
        return self.browser.find_element_by_css_selector('input[type="file"]')

    @property
    def report_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_blue_submit m_l10"]')

    @property
    def batch_delete_cart_prod_chk(self):
        return self.browser.find_element_by_css_selector('a[class="btn_batch_del_cart_book"]')

    @property
    def batch_move_to_fav_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_batch_moveto_favorite"]')

    @property
    def add_shop_to_fav_btn(self):
        return self.browser.find_element_by_css_selector(self.add_shop_to_fav_css)

    @property
    def add_shop_to_fav_css(self):
        return '#kfz_favorite_shop_public_button'

    @property
    def go_to_shop_fav_btn(self):
        return self.browser.find_element_by_id('kfz_favorite_shop_public_over_win').find_element_by_css_selector(
            self.confirm_btn_css)

    @property
    def batch_delete_fav_shop_btn(self):
        return self.browser.find_element_by_css_selector('#btn_batch_delete_shop')

    @property
    def fav_shop_item_box(self):
        return self.browser.find_element_by_css_selector('#shop_list_box > tr')

    @property
    def add_cart_fail_notice(self):
        return self.browser.find_element_by_css_selector('div[class="text notice"]').find_element_by_class_name('tit')

    @property
    def add_cart_success_notice(self):
        return self.browser.find_element_by_css_selector('span[class="f_left green "]')

    @property
    def shop_box_css(self):
        return 'div[class="shop_box m_t10"]'

    @property
    def order_info_css(self):
        return 'div[class="cart_table no_btm"]'
