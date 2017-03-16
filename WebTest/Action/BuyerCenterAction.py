import time

from Module import Uri, UserInfo
from WebTest.Page.BuyerCenterPage import BuyerCenterPage


class BuyerCenterAction:
    def __init__(self):
        self.buyerCenterPage = BuyerCenterPage()

    # 登录
    def login(self):
        self.buyerCenterPage.go_to(Uri.LoginPage)
        self.buyerCenterPage.login_name_txt.send_keys(UserInfo.User2)
        self.buyerCenterPage.login_password_txt.send_keys(UserInfo.PwdLogin)
        self.buyerCenterPage.login_submit_btn.click()
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.page_index_css)

    # 将网址添加进收藏夹
    def add_site_to_fav(self):
        self.buyerCenterPage.go_to(Uri.FavoriteProductPage)
        self.buyerCenterPage.go_to(Uri.FavoriteSitePage)
        self.buyerCenterPage.add_fav_site_link.click()
        self.buyerCenterPage.add_site_name_txt.send_keys('Test')
        self.buyerCenterPage.add_site_url_txt.send_keys('Test.com')
        self.buyerCenterPage.add_site_note_txt.send_keys('Note')
        self.buyerCenterPage.confirm_btn.click()

    # 编辑收藏的网址
    def edit_fav_site(self):
        self.buyerCenterPage.edit_fav_site_link.click()
        self.buyerCenterPage.edit_site_name_txt.send_keys('Edit')
        self.buyerCenterPage.edit_site_url_txt.send_keys('Edit')
        self.buyerCenterPage.edit_site_note_txt.send_keys('Edit')
        self.buyerCenterPage.edit_fav_site_confirm.click()

    # 删除收藏的网址
    def delete_fav_site(self):
        self.buyerCenterPage.delete_fav_site_link.click()
        time.sleep(1)
        self.buyerCenterPage.delete_fav_site_link_confirm_btn.click()

    # 删除收货地址
    def delete_receive_address(self):
        self.buyerCenterPage.go_to(Uri.ReceiveAddressPage)
        self.buyerCenterPage.delete_receive_address_link.click()
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.confirm_btn_css)
        self.buyerCenterPage.confirm_btn.click()

    # 添加收货地址
    def add_receive_address(self):
        self.buyerCenterPage.go_to(Uri.ReceiveAddressPage)
        self.buyerCenterPage.add_address_btn.click()
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.receiver_address_confirm_css)
        self.buyerCenterPage.receiver_name_txt.send_keys('测试账户')
        self.buyerCenterPage.receiver_mobile_txt.send_keys('18510291234')
        self.buyerCenterPage.receiver_province_list[1].click()
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.receiver_area_css)
        self.buyerCenterPage.receiver_area_list[6].click()
        self.buyerCenterPage.receiver_detail_address_txt.send_keys('红厂创意园区A6')
        self.buyerCenterPage.set_default_address_chk.click()
        self.buyerCenterPage.receiver_address_confirm_btn.click()

    # 编辑收货地址
    def edit_receive_address(self):
        self.buyerCenterPage.receiver_edit_address_btn.click()
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.receiver_address_confirm_css)
        self.buyerCenterPage.receiver_name_txt.clear()
        self.buyerCenterPage.receiver_name_txt.send_keys('测试账户改')
        self.buyerCenterPage.receiver_mobile_txt.clear()
        self.buyerCenterPage.receiver_mobile_txt.send_keys('18510294321')
        self.buyerCenterPage.receiver_province_list[2].click()
        time.sleep(1)
        self.buyerCenterPage.receiver_area_list[1].click()
        self.buyerCenterPage.receiver_detail_address_txt.clear()
        self.buyerCenterPage.receiver_detail_address_txt.send_keys('红厂创意园区A4')
        self.buyerCenterPage.receiver_address_confirm_btn.click()

    # 更改用户登录密码
    def change_user_password(self, old_pwd, new_pwd):
        self.buyerCenterPage.go_to(Uri.ChangePwdPage)
        self.buyerCenterPage.old_password_txt.send_keys(old_pwd)
        self.buyerCenterPage.new_password_txt.send_keys(new_pwd)
        self.buyerCenterPage.repeat_password_txt.send_keys(new_pwd)
        self.buyerCenterPage.submit_change_password_btn.click()

    # 清空我的好友
    def clean_up_my_friend(self):
        self.buyerCenterPage.go_to(Uri.MyFriendPage)
        if self.buyerCenterPage.my_friend_box.text != '暂无数据':
            self.buyerCenterPage.common_check_all_chk.click()
            self.buyerCenterPage.common_batch_delete_btn.click()
            time.sleep(1)
            self.buyerCenterPage.batch_delete_friend_confirm_btn.click()

    # 添加我的好友
    def add_my_friend(self):
        self.buyerCenterPage.go_to(Uri.SearchFriendPage)
        self.buyerCenterPage.search_friend_txt.send_keys(UserInfo.User1)
        self.buyerCenterPage.search_friend_btn.click()
        self.buyerCenterPage.add_to_friend_link.click()

    # 获取提示条信息
    def get_msg_bar_txt(self):
        self.buyerCenterPage.wait_until_clickable(self.buyerCenterPage.msg_bar_css)
        time.sleep(1)
        return self.buyerCenterPage.msg_bar.text
