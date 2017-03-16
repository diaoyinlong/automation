import unittest

from Module import UserInfo
from WebTest.Action.BuyerCenterAction import BuyerCenterAction


class BuyerCenterTestCase(unittest.TestCase):
    def setUp(self):
        self.action = BuyerCenterAction()

    def tearDown(self):
        self.action.buyerCenterPage.quit()

    def testManageFavSite(self):
        """
        测试管理收藏的网址
        :return:
        """
        self.action.login()
        # 添加网址到收藏夹
        self.action.add_site_to_fav()

        # 验证提示信息
        self.assertEqual('添加收藏网址操作成功！', self.action.get_msg_bar_txt())

        # 编辑收藏的网址
        self.action.edit_fav_site()

        # 验证编辑成功
        self.assertEqual('编辑收藏网址操作成功！', self.action.get_msg_bar_txt())

        # 删除收藏的网址
        self.action.delete_fav_site()

        # 验证删除成功
        self.assertEqual('删除收藏网址操作成功！', self.action.get_msg_bar_txt())

    def testManageReceiveAddress(self):
        """
        测试管理我的收货地址
        :return:
        """
        self.action.login()
        # 添加收货地址
        self.action.add_receive_address()

        # 验证新增收货地址成功
        self.assertEqual('新增收货地址操作成功！', self.action.get_msg_bar_txt())

        # 编辑收货地址
        self.action.edit_receive_address()

        # 验证编辑收货地址成功
        self.assertEqual('修改收货地址操作成功！', self.action.get_msg_bar_txt())

        # 删除收货地址
        self.action.delete_receive_address()

        # 验证删除收货地址成功
        self.assertEqual('删除收货地址操作成功！', self.action.get_msg_bar_txt())

    def testChangeLoginPassword(self):
        """
        测试更改登录密码
        :return:
        """
        # 登录
        self.action.login()

        # 修改登录密码
        self.action.change_user_password(UserInfo.PwdLogin, '654321')

        # 验证修改成功
        self.assertEqual('修改密码操作成功！', self.action.get_msg_bar_txt())

        # 还原以前的密码
        self.action.change_user_password('654321', UserInfo.PwdLogin)

        # 验证还原成功
        self.assertEqual('修改密码操作成功！', self.action.get_msg_bar_txt())

    def testMyFriend(self):
        """
        测试我的好友
        :return:
        """
        self.action.login()
        # 清空我的好友
        self.action.clean_up_my_friend()

        # 添加好友
        self.action.add_my_friend()

        # 验证添加成功
        self.assertEqual('添加好友成功', self.action.get_msg_bar_txt())

        # 清空我的好友
        self.action.clean_up_my_friend()

        # 验证清空成功
        self.assertEqual('批量删除好友操作成功！', self.action.get_msg_bar_txt())
