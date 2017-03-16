from WebTest.Page.BasePage import BasePage


class SellerCenterPage(BasePage):
    @property
    def fast_add_book_txt(self):
        return self.browser.find_element_by_id('keywords')

    @property
    def change_prod_type_link(self):
        return self.browser.find_element_by_id('change_cat')

    @property
    def book_novel_type_li(self):
        return self.browser.find_element_by_id('category_win_item_43000000000000000')

    @property
    def prod_name_txt(self):
        return self.browser.find_element_by_id('itemName')

    @property
    def author_name_txt(self):
        return self.browser.find_element_by_id('author')

    @property
    def press_txt(self):
        return self.browser.find_element_by_id('press')

    @property
    def pub_date_txt(self):
        return self.browser.find_element_by_id('pubDate')

    @property
    def quality_list(self):
        self.browser.find_element_by_id('quality').click()
        return self.browser.find_element_by_id('quality').find_elements_by_tag_name('li')

    @property
    def price_txt(self):
        return self.browser.find_element_by_id('price')

    @property
    def seller_ship_fee_rdo(self):
        return self.browser.find_element_by_id('bearShipping_seller')

    @property
    def add_book_submit_btn(self):
        return self.browser.find_element_by_id('product_submit')

    @property
    def isbn_pop_win(self):
        return self.browser.find_element_by_id('popwin_loading')

    @property
    def isbn_txt(self):
        return self.browser.find_element_by_id('isbn')

    @property
    def binging_txt(self):
        return self.browser.find_element_by_css_selector('#binding > a')

    @property
    def edition_txt(self):
        return self.browser.find_element_by_id('edition')

    @property
    def page_txt(self):
        return self.browser.find_element_by_id('pageNum')

    @property
    def origin_price_txt(self):
        return self.browser.find_element_by_id('oriPrice')

    @property
    def pic_data_url(self):
        return self.browser.find_element_by_css_selector('#images > ul > li > img').get_attribute('data-url')

    @property
    def do_not_auto_confirm_rdo(self):
        return self.browser.find_element_by_id('setAuto0')

    @property
    def auto_confirm_rdo(self):
        return self.browser.find_element_by_id('setAuto1')

    @property
    def auto_confirm_submit_btn(self):
        return self.browser.find_element_by_css_selector('a[class="add110 btn_submit"]')

    @property
    def auto_cancel_rdo(self):
        return self.browser.find_element_by_id('radio_type1')

    @property
    def do_not_auto_cancel_rdo(self):
        return self.browser.find_element_by_id('radio_type3')

    @property
    def auto_cancel_submit_btn(self):
        return self.browser.find_element_by_id('submitBtn')

    @property
    def delete_no_verify_book_link(self):
        return self.browser.find_element_by_class_name('delete')

    @property
    def search_book_name_txt(self):
        return self.browser.find_element_by_id('s_itemName')

    @property
    def search_btn(self):
        return self.browser.find_element_by_css_selector('a[class="submit btn_blue"]')

    @property
    def first_book_name(self):
        return self.browser.find_element_by_class_name('pro_name3').text

    @property
    def delete_book_confirm_btn(self):
        return self.browser.find_element_by_id('removeOverWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def best_book_css(self):
        return 'div[class="win"] > a'

    @property
    def best_book_btn(self):
        return self.browser.find_element_by_css_selector(self.best_book_css)

    @property
    def check_all_book_chk(self):
        return self.browser.find_element_by_name('selectAll')

    @property
    def cancel_best_btn(self):
        return self.browser.find_element_by_css_selector('a[class="delete-selected btn_gray_70_25 f_left m_r10"]')

    @property
    def add_prod_type_btn(self):
        return self.browser.find_element_by_id('addShopCat')

    @property
    def prod_type_name_txt(self):
        return self.browser.find_element_by_name('catName')

    @property
    def prod_type_id_txt(self):
        return self.browser.find_element_by_name('myCatId')

    @property
    def prod_type_sort_txt(self):
        return self.browser.find_element_by_name('sortOrder')

    @property
    def edit_prod_type_link(self):
        return self.browser.find_element_by_class_name('edit_shopcat')

    @property
    def prod_type_switch_btn(self):
        return self.browser.find_element_by_id('useMyCat')

    @property
    def prod_type_list(self):
        self.browser.find_element_by_id('myCatId').click()
        return self.browser.find_element_by_id('myCatId').find_elements_by_tag_name('li')

    @property
    def select_all_prod_type_chk(self):
        return self.browser.find_element_by_id('all_sec_2')

    @property
    def batch_delete_prod_type_btn(self):
        return self.browser.find_element_by_id('muitydel')

    @property
    def kfz_confirm_btn(self):
        return self.browser.find_element_by_id('kfz_confirmWin').find_element_by_css_selector(self.confirm_btn_css)

    @property
    def edit_shop_temp_inform_link(self):
        return self.browser.find_element_by_id('temp_inform_box').find_element_by_css_selector('a[class="btn_edit"]')

    @property
    def edit_shop_notice_link(self):
        return self.browser.find_element_by_id('shop_notice_box').find_element_by_css_selector('a[class="btn_edit"]')

    @property
    def edit_friend_shop_link(self):
        return self.browser.find_element_by_id('friend_link_box').find_element_by_css_selector('a[class="btn_edit"]')

    @property
    def pop_win_frame(self):
        return self.browser.find_element_by_tag_name('iframe')

    @property
    def rich_txt(self):
        return self.browser.find_element_by_css_selector('body[class="cke_show_borders"]')

    @property
    def friend_shop_row(self):
        return self.browser.find_element_by_id('friend_link_win_box').find_elements_by_tag_name('tr')

    @property
    def delete_friend_shop_link(self):
        return self.browser.find_element_by_css_selector('a[class="btn_del f_left"]')

    @property
    def search_friend_shop_txt(self):
        return self.browser.find_element_by_class_name('text_230')

    @property
    def add_friend_shop_btn(self):
        return self.browser.find_element_by_css_selector('a[class="btn_add btn_gray_60"]')

    @property
    def add_shop_memo_btn(self):
        return self.browser.find_element_by_id('btn_add')

    @property
    def edit_shop_memo_link(self):
        return self.browser.find_element_by_class_name('btn_edit')

    @property
    def delete_link(self):
        return self.browser.find_element_by_class_name('btn_delete')

    @property
    def shop_memo_content_txt(self):
        return self.browser.find_element_by_id('noteContent')

    @property
    def center_confirm_css(self):
        return 'a[class="subBtn f_left"]'

    @property
    def center_confirm_btn(self):
        return self.browser.find_element_by_css_selector(self.center_confirm_css)

    @property
    def shop_memo_list(self):
        return self.browser.find_element_by_id('note_list').find_elements_by_tag_name('tr')

    @property
    def auction_black_name_txt(self):
        return self.browser.find_element_by_name('nickname')

    @property
    def book_black_name_txt(self):
        return self.browser.find_element_by_id('nickname')

    @property
    def add_to_black_btn(self):
        return self.browser.find_element_by_id('btn_addlist')

    @property
    def black_list(self):
        return self.browser.find_element_by_id('black_list').find_elements_by_tag_name('tr')

    @property
    def auction_novel_type_li(self):
        return self.browser.find_element_by_id('productCategoryWin_item_43000000000000000')

    @property
    def auction_line_old_book_li(self):
        self.browser.find_element_by_id('productCategoryWin_item_8000000000000000').click()
        return self.browser.find_element_by_id('productCategoryWin_item_8001000000000000')

    @property
    def auction_famous_ink_li(self):
        self.browser.find_element_by_id('productCategoryWin_item_21000000000000000').click()
        return self.browser.find_element_by_id('productCategoryWin_item_21001000000000000')

    @property
    def auction_famous_painting_li(self):
        self.browser.find_element_by_id('productCategoryWin_item_37000000000000000').click()
        return self.browser.find_element_by_id('productCategoryWin_item_37001000000000000')

    @property
    def auction_antique_li(self):
        self.browser.find_element_by_id('productCategoryWin_item_58000000000000000').click()
        return self.browser.find_element_by_id('productCategoryWin_item_58012000000000000')

    @property
    def auction_pub_year(self):
        return self.browser.find_element_by_css_selector('input[class="selectTit text_213 down"]')

    @property
    def auction_promise_rdo(self):
        return self.browser.find_element_by_id('promise_31')

    @property
    def auction_paper_type(self):
        self.browser.find_element_by_id('paper').click()
        return self.browser.find_element_by_id('paper').find_elements_by_tag_name('li')

    @property
    def auction_print_type(self):
        self.browser.find_element_by_id('printType').click()
        return self.browser.find_element_by_id('printType').find_elements_by_tag_name('li')

    @property
    def auction_length_txt(self):
        return self.browser.find_element_by_id('sizeLength')

    @property
    def auction_width_txt(self):
        return self.browser.find_element_by_id('sizeWidth')

    @property
    def auction_height_txt(self):
        return self.browser.find_element_by_id('sizeHeight')

    @property
    def auction_print_num(self):
        return self.browser.find_element_by_id('printingNum')

    @property
    def auction_famous_type(self):
        self.browser.find_element_by_id('sort').click()
        return self.browser.find_element_by_id('sort').find_elements_by_tag_name('li')

    @property
    def auction_material_type(self):
        self.browser.find_element_by_id('material').click()
        return self.browser.find_element_by_id('material').find_elements_by_tag_name('li')

    @property
    def auction_binding_type(self):
        self.browser.find_element_by_id('binding').click()
        return self.browser.find_element_by_id('binding').find_elements_by_tag_name('li')

    @property
    def auction_area_list(self):
        self.browser.find_element_by_id('auctionArea').click()
        return self.browser.find_element_by_id('auctionArea').find_elements_by_tag_name('li')

    @property
    def special_area_list(self):
        self.browser.find_element_by_id('specialArea').click()
        return self.browser.find_element_by_id('specialArea').find_elements_by_tag_name('li')

    @property
    def auction_begin_price_txt(self):
        return self.browser.find_element_by_id('beginPrice')

    @property
    def auction_min_add_txt(self):
        return self.browser.find_element_by_id('minAddPrice')

    @property
    def auction_end_time(self):
        return self.browser.find_element_by_id('endTime')

    @property
    def auction_begin_time(self):
        return self.browser.find_element_by_id('beginTime')

    @property
    def auction_ship_fee_list(self):
        self.browser.find_element_by_id('wShippingFee').click()
        return self.browser.find_element_by_id('wShippingFee').find_elements_by_tag_name('li')

    @property
    def pic_uploader(self):
        return self.browser.find_element_by_css_selector('input[type="file"]')

    @property
    def add_auction_submit_btn(self):
        return self.browser.find_element_by_id('btn_add_submit')

    @property
    def not_bid_auction_list(self):
        return self.browser.find_element_by_id('product_list_box').find_elements_by_tag_name('tr')

    @property
    def add_auction_black_list_btn(self):
        return self.browser.find_element_by_css_selector('a[class="f_right btn_orange_90_25"]')

    @property
    def delete_auction_black_list_link(self):
        return self.browser.find_element_by_css_selector('#black_list > tr > td.last > a')

    @property
    def first_td_css(self):
        return '#unsold_list_table > tbody > tr > td.first'

    @property
    def first_td(self):
        return self.browser.find_element_by_css_selector('#column_list_table > tbody > tr > td')

    @property
    def product_type(self):
        return self.browser.find_element_by_id('catId')
