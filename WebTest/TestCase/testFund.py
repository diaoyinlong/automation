import unittest

from Module import UserInfo
from WebTest.Action.FundAction import FundAction


class FundTestCase(unittest.TestCase):
    def setUp(self):
        self.action = FundAction()

    def tearDown(self):
        self.action.fundPage.quit()

    def testPostalRecharge(self):
        """
        测试汇款充值
        :return:
        """
        self.action.login()
        # 填写汇款通知单
        self.action.fill_postal_recharge_form()

        # 验证汇款成功
        self.assertTrue(self.action.verify_postal_recharge_success())

        # 编辑汇款通知单
        self.action.edit_postal_recharge_form()

        # 验证编辑成功
        self.assertEqual('修改汇款通知单成功！', self.action.get_top_msg_text())
        self.assertTrue(self.action.verify_postal_recharge_success())

    def testFundTransfer(self):
        """
        测试转账
        :return:
        """
        self.action.login()
        # 进行转账操作
        self.action.do_transfer()

        # 验证转账成功
        self.assertTrue(self.action.verify_transfer_success())

    def testManageCashAccount(self):
        """
        测试管理提现账号
        :return:
        """
        self.action.login()
        # 添加提现账号
        self.action.add_cash_account()

        # 验证提现账号添加成功
        self.assertEqual('添加提现账号成功！', self.action.get_top_msg_text())

        # 编辑提现账号
        self.action.edit_cash_account()

        # 验证编辑成功
        self.assertEqual('编辑提现账号成功！', self.action.get_top_msg_text())

        # 删除提现账号
        self.action.delete_cash_account()

        # 验证删除成功
        self.assertEqual('删除提现账号成功！', self.action.get_top_msg_text())

    def testChangePayPwd(self):
        """
        测试修改支付密码
        :return:
        """
        self.action.login()
        # 修改支付密码
        self.action.change_pay_pwd(UserInfo.PwdPay, 'test321')

        # 验证修改成功
        self.assertEqual('修改支付密码成功！', self.action.get_change_pay_success_text())

        # 修改支付密码
        self.action.change_pay_pwd('test321', UserInfo.PwdPay)

        # 验证修改成功
        self.assertEqual('修改支付密码成功！', self.action.get_change_pay_success_text())

    def testCashBack(self):
        """
        测试提现操作
        :return:
        """
        try:
            self.action.login()
            # 添加提现账号
            self.action.add_cash_account()

            # 进行提现操作
            self.action.do_cash_back()

            # 验证提现结果
            if self.action.tempData == 1:
                self.assertTrue('提现申请提交成功！', self.action.get_cash_back_success_text())
            else:
                self.assertEqual('您今日已提现3次，请明天再来提现。', self.action.get_top_msg_text())
        finally:
            # 删除提现账号
            self.action.delete_cash_account()
