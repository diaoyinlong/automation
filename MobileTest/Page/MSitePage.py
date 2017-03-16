from Public.Browser import Browser


class MSitePage(Browser):
    @property
    def book_search_tab(self):
        return self.browser.find_element_by_css_selector('span[data-area="shop"]')

    @property
    def auction_search_tab(self):
        return self.browser.find_element_by_css_selector('span[data-area="pm"]')

    @property
    def shop_search_tab(self):
        return self.browser.find_element_by_css_selector('span[data-area="dianpu"]')

    @property
    def search_txt(self):
        return self.browser.find_element_by_id('search-kw')

    @property
    def search_submit_css(self):
        return '#submitBtn'

    @property
    def search_submit_btn(self):
        return self.browser.find_element_by_css_selector(self.search_submit_css)

    @property
    def book_search_result(self):
        return self.browser.find_element_by_id('content').find_elements_by_css_selector('p[class="book-box-con-name"]')

    @property
    def auction_search_result(self):
        return self.browser.find_element_by_id('result_search_con').find_elements_by_css_selector(
            'p[class="item_text"]')

    @property
    def shop_search_result(self):
        return self.browser.find_element_by_css_selector('div[class="content"]').find_elements_by_css_selector(
            'div[class="title"]')

    @property
    def book_fav_btn(self):
        return self.browser.find_element_by_css_selector('div[class="f_right cang_box"] > div')

    @property
    def tip_view_css(self):
        return 'overlayautotip'

    @property
    def tip_view(self):
        return self.browser.find_element_by_tag_name(self.tip_view_css)

    @property
    def fav_books_name(self):
        return self.browser.find_elements_by_css_selector('div[class="info_title ng-binding"]')

    @property
    def del_fav_book_btn(self):
        return self.browser.find_elements_by_css_selector('span[ng-click="delFavBook(goods.favBookId)"]')

    @property
    def no_data(self):
        return self.browser.find_element_by_class_name('no_list')

    @property
    def loading_css(self):
        return 'div[ng-show="isLoading"]'

    @property
    def loading_css2(self):
        return 'div[class="loader"]'

    @property
    def shop_fav_btn(self):
        return self.browser.find_element_by_css_selector('div[class="shop-header-fav favorite"]')

    @property
    def del_fav_shop_btn(self):
        return self.browser.find_elements_by_css_selector('span[ng-click="delShop(shop.favShopId)"]')

    @property
    def fav_shops_name(self):
        return self.browser.find_elements_by_css_selector('span[ng-bind="shop.shopName"]')

    @property
    def auction_fav_css(self):
        return 'div[class="icon_btn c_gray_6"]'

    @property
    def auction_fav_btn(self):
        return self.browser.find_element_by_css_selector(self.auction_fav_css)

    @property
    def fav_auction_name(self):
        return self.browser.find_elements_by_css_selector('a[ng-bind="item.itemName"]')

    @property
    def del_fav_auction_btn(self):
        return self.browser.find_elements_by_css_selector('div[ng-click="del($index,item.favId)"]')

    @property
    def login_name_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.loginName"]')

    @property
    def login_pwd_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.loginPass"]')

    @property
    def login_submit_btn(self):
        return self.browser.find_element_by_class_name('login_form_btn')

    @property
    def old_pwd_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.password"]')

    @property
    def new_pwd_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.newPassword"]')

    @property
    def change_pwd_submit_btn(self):
        return self.browser.find_element_by_class_name('personal_form_btn')

    @property
    def success_msg_css(self):
        return 'div[ng-show="view.isSuccess"] > p[class="suc_title"]'

    @property
    def success_msg(self):
        return self.browser.find_element_by_css_selector(self.success_msg_css)

    @property
    def address_submit_css(self):
        return 'div[class="footer_fix_box"] > a'

    @property
    def address_submit_btn(self):
        return self.browser.find_element_by_css_selector(self.address_submit_css)

    @property
    def receiver_name_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.receiverName"]')

    @property
    def receiver_mobile_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.mobile"]')

    @property
    def receiver_area(self):
        return self.browser.find_element_by_css_selector('div[ng-click="addressChoose()"]')

    @property
    def receiver_area_confirm_btn(self):
        return self.browser.find_element_by_css_selector('a[class="submit_btn"]')

    @property
    def receiver_address_txt(self):
        return self.browser.find_element_by_css_selector('textarea[ng-model="input.address"]')

    @property
    def edit_address_css(self):
        return 'span[ng-click="setAddress(item.addrId)"]'

    @property
    def edit_address_btn(self):
        return self.browser.find_element_by_css_selector(self.edit_address_css)

    @property
    def del_address_btn(self):
        return self.browser.find_elements_by_css_selector('span[ng-click="delAddress(item.addrId)')

    @property
    def add_cart_btn(self):
        return self.browser.find_element_by_class_name('add_cart_box')

    @property
    def cart_item_css(self):
        return 'div[class="item_product"]'

    @property
    def check_all_rdo(self):
        return self.browser.find_element_by_css_selector('div[class="f_left check_all"]')

    @property
    def go_to_pay_btn(self):
        return self.browser.find_element_by_class_name('btn_submit')

    @property
    def create_order_btn(self):
        return self.browser.find_element_by_css_selector('div[ng-click="submitCreateOrder()"]')

    @property
    def order_book_box_css(self):
        return 'a[class="order_book_box clearfix last"]'

    @property
    def submit_order_result_css(self):
        return 'section.content > div.text > div.title'

    @property
    def submit_order_result(self):
        return self.browser.find_element_by_css_selector(self.submit_order_result_css)

    @property
    def pop_bid_win_css(self):
        return 'div[class="footer_fix_box clearfix show"] > div[class="text_btn"]'

    @property
    def pop_bid_win_btn(self):
        return self.browser.find_element_by_css_selector(self.pop_bid_win_css)

    @property
    def bid_btn(self):
        return self.browser.find_element_by_class_name('btn')

    @property
    def agent_bid_tab(self):
        return self.browser.find_element_by_css_selector('span[ng-click="tab_2()"]')

    @property
    def agent_bid_btn(self):
        return self.browser.find_element_by_css_selector('a[class="font_b2 btn agent"]')

    @property
    def search_friend_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="searchFriendName"]')

    @property
    def search_user_btn(self):
        return self.browser.find_element_by_class_name('search_btn')

    @property
    def search_user_result(self):
        return self.browser.find_element_by_class_name('gotalk')

    @property
    def send_message_txt(self):
        return self.browser.find_element_by_id('sendMsg')

    @property
    def send_btn(self):
        return self.browser.find_element_by_css_selector('span[ng-click="sendMessage()"]')

    @property
    def message_collection(self):
        return self.browser.find_elements_by_css_selector('p[class="ng-binding ng-scope"]')

    @property
    def order_action_css(self):
        return 'a[class="f_right sure_btn_small2 m_l30 ng-binding"]'

    @property
    def trade_action_css(self):
        return 'a[class="f_right sure_btn_small m_l30 m_top ng-binding"]'

    @property
    def order_action_btn(self):
        return self.browser.find_element_by_css_selector(self.order_action_css)

    @property
    def trade_action_btn(self):
        return self.browser.find_element_by_css_selector(self.trade_action_css)

    @property
    def eval_content_txt(self):
        return self.browser.find_element_by_name('content')

    @property
    def submit_eval_btn(self):
        return self.browser.find_element_by_css_selector('a[class="red_btm_box ng-binding ng-scope"]')

    @property
    def confirm_css(self):
        return 'a[class="confirmbtn"]'

    @property
    def confirm_btn(self):
        return self.browser.find_element_by_css_selector(self.confirm_css)

    @property
    def send_order_num_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="shipmentNum"]')

    @property
    def pay_step1_css(self):
        return 'div[class="f_right button"]'

    @property
    def pay_step1_btn(self):
        return self.browser.find_element_by_css_selector(self.pay_step1_css)

    @property
    def pay_step2_css(self):
        return 'div[class="red_btm_box ng-scope"]'

    @property
    def pay_step2_btn(self):
        return self.browser.find_element_by_css_selector(self.pay_step2_css)

    @property
    def pay_pass_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="payPass"]')

    @property
    def pay_step3_css(self):
        return 'div[class="btn font_b2"]'

    @property
    def pay_step3_btn(self):
        return self.browser.find_element_by_css_selector(self.pay_step3_css)

    @property
    def pay_success_css(self):
        return 'p[class="c_green font30"]'

    @property
    def pay_success_msg(self):
        return self.browser.find_element_by_css_selector(self.pay_success_css)

    @property
    def book_confirm_css(self):
        return 'a[class="confirmbtn c_red"]'

    @property
    def book_confirm_btn(self):
        return self.browser.find_element_by_css_selector(self.book_confirm_css)

    @property
    def trade_confirm_btn(self):
        return self.browser.find_element_by_css_selector('a[class="confirmbtn c_red ng-binding"]')

    @property
    def add_cash_account_btn(self):
        return self.browser.find_element_by_css_selector('a[ng-click="submit()"]')

    @property
    def alipay_chk(self):
        return self.browser.find_element_by_css_selector('i[ng-click="isAlipay()"]')

    @property
    def alipay_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.alipayAccount"]')

    @property
    def cash_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="money"]')

    @property
    def cash_back_pass_css(self):
        return 'input[ng-model="password"]'

    @property
    def cash_back_pass_txt(self):
        return self.browser.find_element_by_css_selector(self.cash_back_pass_css)

    @property
    def fund_success_css(self):
        return 'div[class="suc_box font_b2 c_green"]'

    @property
    def fund_success_msg(self):
        return self.browser.find_element_by_css_selector(self.fund_success_css)

    @property
    def del_cash_account_btn(self):
        return self.browser.find_elements_by_css_selector('li[class="f_right del"]')

    @property
    def book_receive_success_css(self):
        return 'p[class="content"]'

    @property
    def book_receive_success_msg(self):
        return self.browser.find_element_by_css_selector(self.book_receive_success_css)

    @property
    def auction_receive_success_css(self):
        return 'li[class="cleafix ng-binding"]'

    @property
    def auction_receive_success_msg(self):
        return self.browser.find_element_by_css_selector(self.auction_receive_success_css)

    @property
    def trans_fund_account_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.incomeAccountId"]')

    @property
    def trans_fund_money_txt(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.fundtransferMoney"]')

    @property
    def trans_pay_password(self):
        return self.browser.find_element_by_css_selector('input[ng-model="input.payPass"]')

    @property
    def submit_btn_1(self):
        return self.browser.find_element_by_css_selector('div[class="btn m_t10"]')

    @property
    def submit_btn_2(self):
        return self.browser.find_element_by_css_selector('div[class="btn m_t30"]')

    @property
    def submit_btn_3(self):
        return self.browser.find_element_by_css_selector('div[class="btn m_t10px"]')
