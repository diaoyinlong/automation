from WebTest.Page.BasePage import BasePage


class BuyerCenterPage(BasePage):
    @property
    def add_fav_site_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_add_site"]')

    @property
    def edit_fav_site_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_edit_site font14"]')

    @property
    def delete_fav_site_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_delete_site font14"]')

    @property
    def delete_fav_site_link_confirm_btn(self):
        return self.browser.find_element_by_id('deleteSiteWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def add_site_name_txt(self):
        return self.browser.find_element_by_id('addSiteWin').find_element_by_name('siteName')

    @property
    def add_site_url_txt(self):
        return self.browser.find_element_by_id('addSiteWin').find_element_by_name('siteUrl')

    @property
    def add_site_note_txt(self):
        return self.browser.find_element_by_id('addSiteWin').find_element_by_name('siteNote')

    @property
    def edit_site_name_txt(self):
        return self.browser.find_element_by_id('editSiteWin').find_element_by_name('siteName')

    @property
    def edit_site_url_txt(self):
        return self.browser.find_element_by_id('editSiteWin').find_element_by_name('siteUrl')

    @property
    def edit_site_note_txt(self):
        return self.browser.find_element_by_id('editSiteWin').find_element_by_name('siteNote')

    @property
    def edit_fav_site_confirm(self):
        return self.browser.find_element_by_id('editSiteWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def address_list_box(self):
        return self.browser.find_element_by_id('addr_list_box')

    @property
    def delete_receive_address_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_del_addr m_l10"]')

    @property
    def common_check_all_chk(self):
        return self.browser.find_element_by_id('check_all')

    @property
    def common_batch_delete_btn(self):
        return self.browser.find_element_by_id('btn_batch_delete')

    @property
    def add_address_btn(self):
        return self.browser.find_element_by_css_selector(self.add_address_css)

    @property
    def add_address_css(self):
        return '#addrRadio_new'

    @property
    def receiver_name_txt(self):
        return self.browser.find_element_by_name('receiverName')

    @property
    def receiver_mobile_txt(self):
        return self.browser.find_element_by_name('mobile')

    @property
    def receiver_province_list(self):
        self.browser.find_element_by_id('province').click()
        return self.browser.find_element_by_id('province').find_elements_by_tag_name('li')

    @property
    def receiver_area_css(self):
        return '#city'

    @property
    def receiver_area_list(self):
        self.browser.find_element_by_css_selector(self.receiver_area_css).click()
        return self.browser.find_element_by_css_selector(self.receiver_area_css).find_elements_by_tag_name('li')

    @property
    def receiver_detail_address_txt(self):
        return self.browser.find_element_by_name('address')

    @property
    def set_default_address_chk(self):
        return self.browser.find_element_by_id('setDefAddr')

    @property
    def receiver_address_confirm_css(self):
        return 'a[class="subBtn f_left m_r20"]'

    @property
    def receiver_address_confirm_btn(self):
        return self.browser.find_element_by_css_selector(self.receiver_address_confirm_css)

    @property
    def receiver_edit_address_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_edit_addr"]')

    @property
    def old_password_txt(self):
        return self.browser.find_element_by_name('password')

    @property
    def new_password_txt(self):
        return self.browser.find_element_by_name('newPassword')

    @property
    def repeat_password_txt(self):
        return self.browser.find_element_by_name('confirmPassword')

    @property
    def submit_change_password_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_110_35 f_left m_r20 btn_submit"]')

    @property
    def my_friend_box(self):
        return self.browser.find_element_by_css_selector('#con_list_box')

    @property
    def batch_delete_friend_confirm_btn(self):
        return self.browser.find_element_by_id('batchDeleteAsWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def search_friend_txt(self):
        return self.browser.find_element_by_id('search_shop_input')

    @property
    def search_friend_btn(self):
        return self.browser.find_element_by_id('btn_search_friend')

    @property
    def add_to_friend_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_add_friend f_right"]')
