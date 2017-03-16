from WebTest.Page.BasePage import BasePage


class FundPage(BasePage):
    @property
    def add_postal_recharge_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_input_note btn_gray_116_30 f_right"]')

    @property
    def postal_paper_id_txt(self):
        return self.browser.find_element_by_id('remitNO')

    @property
    def postal_amount_txt(self):
        return self.browser.find_element_by_id('amount')

    @property
    def postal_remark_txt(self):
        return self.browser.find_element_by_id('noteDesc')

    @property
    def postal_confirm_btn(self):
        return self.browser.find_element_by_css_selector('a[class="subBtn f_left"]')

    @property
    def postal_result_box_css(self):
        return 'div[class="result_box_green clearfix"]'

    @property
    def first_row_data(self):
        return self.browser.find_element_by_css_selector('#list_box > tr').find_elements_by_tag_name('td')

    @property
    def edit_first_row_link(self):
        return self.browser.find_element_by_class_name('btn_edit_note')

    @property
    def receive_account_id_txt(self):
        return self.browser.find_element_by_id('incomeAccountId')

    @property
    def receive_account_id_repeat_txt(self):
        return self.browser.find_element_by_id('incomeAccountIdConfirm')

    @property
    def transfer_amount_txt(self):
        return self.browser.find_element_by_id('fundtransferMoney')

    @property
    def transfer_remark_txt(self):
        return self.browser.find_element_by_id('note')

    @property
    def transfer_next_btn(self):
        return self.browser.find_element_by_id('btn_transfer_next')

    @property
    def pay_pwd_txt(self):
        return self.browser.find_element_by_id('payPass')

    @property
    def transfer_submit_css(self):
        return '#btn_transfer_submit'

    @property
    def transfer_submit_btn(self):
        return self.browser.find_element_by_css_selector(self.transfer_submit_css)

    @property
    def transfer_result_box_css(self):
        return 'div[class="result_box clearfix"]'

    @property
    def add_cash_account_css(self):
        return 'a[class="btn_add"]'

    @property
    def add_cash_account_btn(self):
        return self.browser.find_element_by_css_selector(self.add_cash_account_css)

    @property
    def bank_list(self):
        self.browser.find_element_by_name('bank').click()
        return self.browser.find_element_by_name('bank').find_elements_by_tag_name('li')

    @property
    def province_list(self):
        self.browser.find_element_by_name('province').click()
        return self.browser.find_element_by_name('province').find_elements_by_tag_name('li')

    @property
    def city_list(self):
        self.browser.find_element_by_name('city').click()
        return self.browser.find_element_by_name('city').find_elements_by_tag_name('li')

    @property
    def sub_bank(self):
        self.browser.find_element_by_name('branchBank').click()
        return self.browser.find_element_by_name('branchBank').find_elements_by_tag_name('li')

    @property
    def bank_account_txt(self):
        return self.browser.find_element_by_name('bankAccount')

    @property
    def edit_cash_account_link(self):
        return self.browser.find_element_by_css_selector('a[class="f_right m_r10 btn_edit"]')

    @property
    def delete_cash_account_link(self):
        return self.browser.find_element_by_css_selector('a[class="f_right btn_delete"]')

    @property
    def delete_cash_account_confirm_btn(self):
        return self.browser.find_element_by_id('cashAccount_delete_win').find_element_by_css_selector(
            self.confirm_btn_css)

    @property
    def cash_account_num(self):
        return len(self.browser.find_element_by_id('cashAccount_box').find_elements_by_tag_name('li')) - 1

    @property
    def old_pwd_txt(self):
        return self.browser.find_element_by_name('payPassword')

    @property
    def new_pwd_txt(self):
        return self.browser.find_element_by_name('newPayPassword')

    @property
    def new_pwd_repeat_txt(self):
        return self.browser.find_element_by_name('newPayPassword_d')

    @property
    def change_pwd_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_110_35 btn_submit"]')

    @property
    def change_pay_pwd_success_css(self):
        return 'p[class="m_t8 fb_18"]'

    @property
    def change_pay_pwd_success_msg(self):
        return self.browser.find_element_by_css_selector(self.change_pay_pwd_success_css)

    @property
    def back_money_amount_txt(self):
        return self.browser.find_element_by_name('drawMoney')

    @property
    def back_money_next_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_110_35 btn_next"]')

    @property
    def back_money_pay_password_txt(self):
        return self.browser.find_element_by_name('payPass')

    @property
    def back_money_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_orange_110_35 inline btn_submit m_r20"]')

    @property
    def back_money_confirm_btn(self):
        return self.browser.find_element_by_id('tip_win').find_element_by_class_name('subBtn')

    @property
    def back_money_success_msg(self):
        return self.browser.find_element_by_css_selector('p[class="m_t8 fb_18"]')

    @property
    def back_money_remain_times(self):
        return self.browser.find_elements_by_css_selector('span[class="red"]')
