import time

from Module import Uri, TestData, Config
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.BookStorePage import BookStorePage


class BookStoreAction(BaseAction):
    def __init__(self):
        self.bookStorePage = BookStorePage()
        BaseAction.__init__(self, self.bookStorePage)

    # 将商品加入购物车
    def add_prod_to_cart(self):
        self.bookStorePage.go_to(Uri.BookDetailPage)
        self.bookStorePage.add_to_cart_btn.click()
        time.sleep(1)

    # 在购物车内进行结算
    def settle_in_cart(self):
        self.bookStorePage.go_to(Uri.CartPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.shop_box_css)
        self.bookStorePage.check_all_cart_prod_chk.click()
        self.bookStorePage.settle_prod_btn.click()
        self.bookStorePage.wait_until_clickable(self.bookStorePage.order_info_css)
        self.bookStorePage.create_order_btn.click()

    # 将商品放入收藏夹
    def add_prod_to_fav_folder(self):
        self.bookStorePage.go_to(Uri.BookDetailPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.add_prod_to_fav_css)
        self.bookStorePage.add_prod_to_fav_btn.click()

    # 将店铺放入收藏夹
    def add_shop_to_fav_folder(self):
        self.bookStorePage.go_to(Uri.BookDetailPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.add_shop_to_fav_css)
        self.bookStorePage.add_shop_to_fav_btn.click()

    # 清空商品收藏夹
    def clean_up_prod_fav(self):
        self.bookStorePage.go_to(Uri.FavoriteProductPage)
        time.sleep(2)
        if self.bookStorePage.fav_prod_item_box.text != '暂无数据':
            self.bookStorePage.check_all_fav_chk.click()
            self.bookStorePage.batch_delete_fav_prod_btn.click()
            self.bookStorePage.wait_until_clickable(self.bookStorePage.confirm_btn_css)
            self.bookStorePage.confirm_btn.click()

    # 清空书店收藏夹
    def clean_up_shop_fav(self):
        self.bookStorePage.go_to(Uri.FavoriteShopPage)
        time.sleep(2)
        if self.bookStorePage.fav_shop_item_box.text != '暂无数据':
            self.bookStorePage.check_all_fav_chk.click()
            self.bookStorePage.batch_delete_fav_shop_btn.click()
            self.bookStorePage.wait_until_clickable(self.bookStorePage.confirm_btn_css)
            self.bookStorePage.confirm_btn.click()

    # 进行举报操作
    def do_report(self):
        self.bookStorePage.report_submit_btn.click()

    # 上传举报图片
    def upload_report_file(self):
        self.bookStorePage.go_to(Uri.BookDetailPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.report_link_css)
        self.bookStorePage.report_link.click()
        self.bookStorePage.switch_to_new_window()
        self.bookStorePage.report_type_1.click()
        self.bookStorePage.report_content_box.send_keys(TestData.Words101)
        self.bookStorePage.file_upload.send_keys(Config.rootPath + '/Resource/pic.jpg')
        self.bookStorePage.wait_until_clickable(self.bookStorePage.msg_bar_css)
        if '成功' in self.bookStorePage.msg_bar.text:
            return True
        else:
            return False

    # 批量删除购物车内商品
    def batch_delete_cart_prod(self):
        self.bookStorePage.go_to(Uri.CartPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.shop_box_css)
        self.bookStorePage.check_all_cart_prod_chk.click()
        self.bookStorePage.batch_delete_cart_link.click()
        self.bookStorePage.wait_until_clickable(self.bookStorePage.confirm_btn_css)
        self.bookStorePage.confirm_btn.click()

    # 批量移入搜藏夹
    def batch_move_cart_prod_to_fav(self):
        self.bookStorePage.go_to(Uri.CartPage)
        self.bookStorePage.wait_until_clickable(self.bookStorePage.shop_box_css)
        self.bookStorePage.check_all_cart_prod_chk.click()
        self.bookStorePage.batch_move_to_fav_link.click()

    # 获取创建订单成功后的提示
    def get_create_order_success_text(self):
        return self.bookStorePage.create_success_msg.text

    # 获取商品成功加入收藏夹后的提示
    def get_add_book_to_fav_success_msg(self):
        return self.bookStorePage.add_book_to_fav_success_msg.text

    # 获取店铺成功加入收藏夹后的提示
    def get_add_shop_to_fav_success_msg(self):
        return self.bookStorePage.add_shop_to_fav_success_msg.text

    # 进入到收藏夹列表验证是否存在藏品
    def has_fav_prod(self):
        self.bookStorePage.go_to(Uri.FavoriteProductPage)
        time.sleep(2)
        fav_id = self.bookStorePage.fav_prod_item_box.get_attribute('favbookid')
        if fav_id is not None and fav_id != '':
            return True
        else:
            return False

    # 进入到收藏夹列表验证是否存在收藏的店铺
    def has_fav_shop(self):
        self.bookStorePage.go_to(Uri.FavoriteShopPage)
        time.sleep(2)
        fav_id = self.bookStorePage.fav_shop_item_box.get_attribute('favshopid')
        if fav_id is not None and fav_id != '':
            return True
        else:
            return False

    # 获取举报成功的提示
    def get_report_success_msg(self):
        return self.bookStorePage.create_success_msg.text

    # 获取成功提示条信息
    def get_top_msg_text(self):
        self.bookStorePage.wait_until_clickable(self.bookStorePage.msg_bar_css)
        return self.bookStorePage.msg_bar.text

    # 获取没有清空购物车后的文本显示
    def get_clean_up_cart_txt(self):
        return self.bookStorePage.no_record_msg

    # 获取加入购物车失败文本
    def get_add_cart_fail_txt(self):
        return self.bookStorePage.add_cart_fail_notice.text

    # 获取加入购物车成功文本
    def get_add_cart_success_txt(self):
        return self.bookStorePage.add_cart_success_notice.text
