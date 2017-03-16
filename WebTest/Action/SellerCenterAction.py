import time

from selenium.webdriver.common.keys import Keys

from Module import Uri, UserInfo, TestData, Config
from Public.Toolkit import Toolkit
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.SellerCenterPage import SellerCenterPage


class SellerCenterAction(BaseAction):
    def __init__(self):
        self.temp_data = ''
        self.sellerCenterPage = SellerCenterPage()
        BaseAction.__init__(self, self.sellerCenterPage)

    # 进行常规上书
    def add_book_normal(self):
        self.sellerCenterPage.go_to(Uri.BookSellerItemPage)
        self.sellerCenterPage.go_to(Uri.AddBookPage)
        if self.sellerCenterPage.product_type.text != '小说':
            self.sellerCenterPage.change_prod_type_link.click()
            self.sellerCenterPage.book_novel_type_li.click()
        self.sellerCenterPage.prod_name_txt.send_keys('测试用书_' + Toolkit.get_random_value())
        self.sellerCenterPage.author_name_txt.send_keys('WebDriver')
        self.sellerCenterPage.press_txt.send_keys('Selenium')
        self.sellerCenterPage.pub_date_txt.send_keys('不详')
        self.sellerCenterPage.quality_list[1].click()
        self.sellerCenterPage.price_txt.send_keys('0.01')
        self.sellerCenterPage.seller_ship_fee_rdo.click()
        self.sellerCenterPage.add_book_submit_btn.click()

    # 进行ISBN上书
    def add_book_isbn(self):
        self.sellerCenterPage.fast_add_book_txt.send_keys('9787229036201')
        self.sellerCenterPage.fast_add_book_txt.send_keys(Keys.ENTER)
        time.sleep(1)
        # self.sellerCenterPage.wait_until_not_clickable(self.sellerCenterPage.isbn_pop_win)

    # 删除未审核图书
    def delete_no_certify_book(self):
        self.sellerCenterPage.go_to(Uri.BookSellerItemPage)
        self.sellerCenterPage.go_to(Uri.UnCertifyPage)
        self.temp_data = self.sellerCenterPage.first_book_name
        self.sellerCenterPage.delete_no_verify_book_link.click()
        time.sleep(1)
        self.sellerCenterPage.delete_book_confirm_btn.click()

    # 在回收站删除图书
    def delete_book_in_recycle(self):
        self.sellerCenterPage.go_to(Uri.ProductRecyclePage)
        time.sleep(2)
        self.sellerCenterPage.search_book_name_txt.send_keys(self.temp_data)
        self.sellerCenterPage.search_btn.click()
        time.sleep(2)
        self.sellerCenterPage.delete_no_verify_book_link.click()
        time.sleep(2)
        self.sellerCenterPage.delete_book_confirm_btn.click()

    # 推荐图书
    def change_book_to_best(self):
        self.sellerCenterPage.go_to(Uri.SalePage)
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.first_td_css)
        self.sellerCenterPage.check_all_book_chk.click()
        self.sellerCenterPage.browser.execute_script(
            'document.getElementById("unsold_choose_btn_top").getElementsByClassName("win")[0].setAttribute("style","display:block");')
        time.sleep(1)
        self.temp_data = self.sellerCenterPage.best_book_btn.text
        self.sellerCenterPage.best_book_btn.click()

    # 取消推荐
    def cancel_best_book(self):
        self.sellerCenterPage.go_to(Uri.BookSellerItemPage)
        self.sellerCenterPage.go_to(Uri.RecommendPage)
        time.sleep(1)
        if self.sellerCenterPage.first_td.text != '无记录！':
            self.sellerCenterPage.check_all_book_chk.click()
            self.sellerCenterPage.cancel_best_btn.click()
            self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.confirm_btn_css)
            self.sellerCenterPage.confirm_btn.click()

    # 添加商品分类
    def add_prod_type(self):
        self.sellerCenterPage.go_to(Uri.ManageProductCategoryPage)
        self.sellerCenterPage.add_prod_type_btn.click()
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.confirm_btn_css)
        self.sellerCenterPage.prod_type_name_txt.send_keys('auto_test')
        self.sellerCenterPage.prod_type_id_txt.send_keys(Toolkit.get_random_number(4))
        self.sellerCenterPage.prod_type_sort_txt.send_keys('1')
        self.sellerCenterPage.confirm_btn.click()

    # 编辑商品分类
    def edit_prod_type(self):
        self.sellerCenterPage.edit_prod_type_link.click()
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.confirm_btn_css)
        self.sellerCenterPage.prod_type_name_txt.clear()
        self.sellerCenterPage.prod_type_name_txt.send_keys('auto_edit')
        self.sellerCenterPage.prod_type_id_txt.clear()
        self.sellerCenterPage.prod_type_id_txt.send_keys(Toolkit.get_random_number(4))
        self.sellerCenterPage.prod_type_sort_txt.clear()
        self.sellerCenterPage.prod_type_sort_txt.send_keys('2')
        self.sellerCenterPage.confirm_btn.click()

    # 启动商品分类
    def switch_on_prod_type(self):
        if self.sellerCenterPage.prod_type_switch_btn.get_attribute('val') == '0':
            self.sellerCenterPage.prod_type_switch_btn.click()

    # 批量删除商品分类
    def batch_delete_prod_type(self):
        self.sellerCenterPage.go_to(Uri.ManageProductCategoryPage)
        self.sellerCenterPage.select_all_prod_type_chk.click()
        self.sellerCenterPage.batch_delete_prod_type_btn.click()
        time.sleep(1)
        self.sellerCenterPage.kfz_confirm_btn.click()
        time.sleep(1)

    # 编辑临时通知
    def edit_temp_inform(self):
        self.sellerCenterPage.go_to(Uri.ShopFittingPage)
        self.sellerCenterPage.edit_shop_temp_inform_link.click()
        self.sellerCenterPage.browser.switch_to_frame(self.sellerCenterPage.pop_win_frame)
        self.sellerCenterPage.rich_txt.clear()
        self.sellerCenterPage.rich_txt.send_keys(TestData.Words101)
        self.sellerCenterPage.browser.switch_to_default_content()
        self.sellerCenterPage.confirm_btn.click()

    # 编辑店铺公告
    def edit_shop_notice(self):
        self.sellerCenterPage.edit_shop_notice_link.click()
        self.sellerCenterPage.browser.switch_to_frame(self.sellerCenterPage.pop_win_frame)
        self.sellerCenterPage.rich_txt.clear()
        self.sellerCenterPage.rich_txt.send_keys(TestData.Words101)
        self.sellerCenterPage.browser.switch_to_default_content()
        self.sellerCenterPage.confirm_btn.click()

    # 添加友情店铺
    def add_friend_shop(self):
        self.sellerCenterPage.edit_friend_shop_link.click()
        time.sleep(1)
        rows = len(self.sellerCenterPage.friend_shop_row)
        if rows != 0:
            for i in range(rows):
                self.sellerCenterPage.delete_friend_shop_link.click()
                time.sleep(1)
                self.sellerCenterPage.kfz_confirm_btn.click()

        self.sellerCenterPage.search_friend_shop_txt.send_keys(UserInfo.User2 + '的书摊')
        self.sellerCenterPage.add_friend_shop_btn.click()

    # 新增备忘录
    def add_shop_memo(self):
        self.sellerCenterPage.go_to(Uri.ShopMemoPage)
        self.sellerCenterPage.add_shop_memo_btn.click()
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.center_confirm_css)
        self.sellerCenterPage.shop_memo_content_txt.send_keys(TestData.Words101)
        self.sellerCenterPage.center_confirm_btn.click()

    # 编辑备忘录
    def edit_shop_memo(self):
        self.sellerCenterPage.edit_shop_memo_link.click()
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.center_confirm_css)
        self.sellerCenterPage.shop_memo_content_txt.clear()
        self.sellerCenterPage.shop_memo_content_txt.send_keys('Edit_Memo')
        self.sellerCenterPage.center_confirm_btn.click()

    # 删除备忘录
    def delete_shop_memo(self):
        rows = len(self.sellerCenterPage.shop_memo_list)
        for i in range(rows):
            self.sellerCenterPage.delete_link.click()
            self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.confirm_btn_css)
            self.sellerCenterPage.confirm_btn.click()
            time.sleep(1)

    # 将用户添加进黑名单
    def add_book_black_list(self):
        self.sellerCenterPage.go_to(Uri.ShopBlackListPage)
        self.sellerCenterPage.book_black_name_txt.send_keys(UserInfo.User1)
        self.sellerCenterPage.add_to_black_btn.click()

    # 将用户移除黑名单
    def delete_from_book_black_list(self):
        self.sellerCenterPage.go_to(Uri.ShopBlackListPage)
        if self.sellerCenterPage.black_list[0].text != '暂无相关黑名单记录！':
            rows = len(self.sellerCenterPage.black_list)
            for i in range(rows):
                self.sellerCenterPage.go_to(Uri.ShopBlackListPage)
                self.sellerCenterPage.delete_link.click()
                self.sellerCenterPage.browser.switch_to_alert().accept()

    # 添加拍品
    def add_auction(self, category):
        self.sellerCenterPage.go_to(Uri.AddAuctionGoodPage)

        if category == '小说':
            if self.sellerCenterPage.product_type.text != '小说':
                self.sellerCenterPage.change_prod_type_link.click()
                time.sleep(1)
                self.sellerCenterPage.auction_novel_type_li.click()
                time.sleep(1)
            self.sellerCenterPage.pub_date_txt.send_keys('不详')
            self.sellerCenterPage.press_txt.send_keys('不详')

        if category == '线装古旧书':
            if self.sellerCenterPage.product_type.text != '线装古旧书 > 小说':
                self.sellerCenterPage.change_prod_type_link.click()
                time.sleep(1)
                self.sellerCenterPage.auction_line_old_book_li.click()
                time.sleep(1)
            self.sellerCenterPage.auction_pub_year.send_keys('不详')
            self.sellerCenterPage.auction_paper_type[1].click()
            self.sellerCenterPage.auction_print_type[1].click()
            self.sellerCenterPage.auction_length_txt.send_keys('15')
            self.sellerCenterPage.auction_width_txt.send_keys('30')
            self.sellerCenterPage.auction_height_txt.send_keys('5')
            self.sellerCenterPage.auction_print_num.send_keys('100')
            self.sellerCenterPage.press_txt.send_keys('不详')

        if category == '名人墨迹':
            if self.sellerCenterPage.product_type.text != '名人墨迹 > 信札':
                self.sellerCenterPage.change_prod_type_link.click()
                time.sleep(1)
                self.sellerCenterPage.auction_famous_ink_li.click()
                time.sleep(1)
            self.sellerCenterPage.auction_promise_rdo.click()
            self.sellerCenterPage.auction_pub_year.send_keys('不详')
            self.sellerCenterPage.page_txt.send_keys('100')

        if category == '名人字画':
            if self.sellerCenterPage.product_type.text != '名人字画 > 书法':
                self.sellerCenterPage.change_prod_type_link.click()
                time.sleep(1)
                self.sellerCenterPage.auction_famous_painting_li.click()
                time.sleep(1)
            self.sellerCenterPage.auction_pub_year.send_keys('不详')
            self.sellerCenterPage.auction_famous_type[1].click()
            self.sellerCenterPage.auction_material_type[1].click()
            self.sellerCenterPage.auction_binding_type[1].click()
            self.sellerCenterPage.auction_length_txt.send_keys('15')
            self.sellerCenterPage.auction_width_txt.send_keys('30')

        if category == '古玩杂项':
            if self.sellerCenterPage.product_type.text != '古玩杂项 > 其他古玩杂项':
                self.sellerCenterPage.change_prod_type_link.click()
                time.sleep(1)
                self.sellerCenterPage.auction_antique_li.click()
                time.sleep(1)
            self.sellerCenterPage.auction_length_txt.send_keys('15')
            self.sellerCenterPage.auction_width_txt.send_keys('30')
            self.sellerCenterPage.auction_height_txt.send_keys('5')

        self.sellerCenterPage.prod_name_txt.send_keys('测试拍卖请勿购买_' + Toolkit.get_random_value())
        self.sellerCenterPage.author_name_txt.send_keys('不详')
        self.sellerCenterPage.quality_list[1].click()
        self.sellerCenterPage.auction_area_list[2].click()
        # self.sellerCenterPage.special_area_list[1].click()
        self.sellerCenterPage.auction_begin_price_txt.send_keys('1')
        self.sellerCenterPage.auction_min_add_txt.send_keys('1')
        '''
        begin_time = self.sellerCenterPage.auction_begin_time.get_attribute('value')
        end_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(time.mktime(time.strptime(begin_time, '%Y-%m-%d %H:%M:%S')) + 2))
        self.sellerCenterPage.auction_end_time.clear()
        self.sellerCenterPage.auction_end_time.send_keys(end_time)
        self.sellerCenterPage.browser.execute_script(
            'document.getElementById("_my97DP").setAttribute("style","display:none");')
        '''
        self.sellerCenterPage.auction_ship_fee_list[2].click()
        self.sellerCenterPage.pic_uploader.send_keys(Config.rootPath + '/Resource/pic.jpg')
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.msg_bar_css)
        self.sellerCenterPage.add_auction_submit_btn.click()

    # 保存添加的拍品ID
    def save_auction_id(self):
        self.sellerCenterPage.go_to(Uri.AuctionNotBeginPage)
        rows = self.sellerCenterPage.not_bid_auction_list
        with open(Config.rootPath + '/Resource/auction_goods_id.txt', 'w', encoding='utf-8') as f:
            f.truncate()
            for row in rows:
                f.write(row.get_attribute('itemid') + '\n')

    # 添加到拍卖黑名单
    def add_auction_black_list(self):
        self.sellerCenterPage.go_to(Uri.AuctionBlackListPage)
        self.sellerCenterPage.add_auction_black_list_btn.click()
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.center_confirm_css)
        self.sellerCenterPage.auction_black_name_txt.send_keys(UserInfo.User1)
        self.sellerCenterPage.center_confirm_btn.click()

    # 从拍卖黑名单删除
    def delete_from_auction_black_list(self):
        rows = len(self.sellerCenterPage.black_list)
        for i in range(rows):
            self.sellerCenterPage.go_to(Uri.AuctionBlackListPage)
            self.sellerCenterPage.delete_auction_black_list_link.click()
            time.sleep(1)
            self.sellerCenterPage.kfz_confirm_btn.click()

    # 获取删除结果
    def get_delete_result(self):
        time.sleep(1)
        self.sellerCenterPage.search_book_name_txt.clear()
        self.sellerCenterPage.search_book_name_txt.send_keys(self.temp_data)
        self.sellerCenterPage.search_btn.click()
        time.sleep(2)
        no_record = self.sellerCenterPage.no_record_msg
        if no_record == '无记录！':
            return True
        else:
            return False

    # 获取取消推荐的结果
    def get_cancel_best_result(self):
        time.sleep(1)
        no_record = self.sellerCenterPage.no_record_msg
        if no_record == '无记录！':
            return True
        else:
            return False

    # 获取成功提示条信息
    def get_top_msg_text(self):
        self.sellerCenterPage.wait_until_clickable(self.sellerCenterPage.msg_bar_css)
        time.sleep(1)
        return self.sellerCenterPage.msg_bar.text

    # 获取ISBN载入数据
    def get_isbn_load_data(self):
        time.sleep(2)
        return {
            'book_name': self.sellerCenterPage.prod_name_txt.get_attribute('value'),
            'isbn': self.sellerCenterPage.isbn_txt.get_attribute('value'),
            'author': self.sellerCenterPage.author_name_txt.get_attribute('value'),
            'press': self.sellerCenterPage.press_txt.get_attribute('value'),
            'pub_date': self.sellerCenterPage.pub_date_txt.get_attribute('value'),
            'binding': self.sellerCenterPage.binging_txt.text,
            'edition': self.sellerCenterPage.edition_txt.get_attribute('value'),
            'page': self.sellerCenterPage.page_txt.get_attribute('value'),
            'origin_price': self.sellerCenterPage.origin_price_txt.get_attribute('value'),
            'pic_url': self.sellerCenterPage.pic_data_url
        }

    # 获取商品分类
    def get_prod_type(self):
        self.sellerCenterPage.go_to(Uri.AddBookPage)
        return self.sellerCenterPage.prod_type_list[1].text

    # 验证推荐结果
    def verify_best_result(self):
        return self.get_top_msg_text() == '添加' + self.temp_data + '成功！'
