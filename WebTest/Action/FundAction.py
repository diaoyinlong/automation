import time

from Module import Uri, UserInfo
from Public.Toolkit import Toolkit
from WebTest.Page.FundPage import FundPage


class FundAction:
    def __init__(self):
        self.tempData = ''
        self.fundPage = FundPage()

    def login(self):
        self.fundPage.go_to(Uri.LoginPage)
        self.fundPage.login_name_txt.send_keys(UserInfo.User3)
        self.fundPage.login_password_txt.send_keys(UserInfo.PwdLogin)
        self.fundPage.login_submit_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.page_index_css)

    # 填写汇款通知单
    def fill_postal_recharge_form(self):
        self.fundPage.go_to(Uri.PostalRechargePage)
        self.fundPage.add_postal_recharge_btn.click()
        self.tempData = Toolkit.get_random_number(6)
        self.fundPage.postal_paper_id_txt.send_keys(self.tempData)
        self.fundPage.postal_amount_txt.send_keys('0.01')
        self.fundPage.postal_remark_txt.send_keys('测试用，无需处理！')
        self.fundPage.postal_confirm_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.postal_result_box_css)

    # 编辑汇款通知单
    def edit_postal_recharge_form(self):
        self.fundPage.edit_first_row_link.click()
        time.sleep(1)
        self.tempData = Toolkit.get_random_number(6)
        self.fundPage.postal_paper_id_txt.clear()
        self.fundPage.postal_paper_id_txt.send_keys(self.tempData)
        self.fundPage.confirm_btn.click()

    # 进行转账
    def do_transfer(self):
        self.fundPage.go_to(Uri.TransferPage)
        self.fundPage.receive_account_id_txt.send_keys(UserInfo.FundID1)
        self.fundPage.receive_account_id_repeat_txt.send_keys(UserInfo.FundID1)
        self.fundPage.transfer_amount_txt.send_keys('0.01')
        self.tempData = 'testTransfer_' + Toolkit.get_random_value()
        self.fundPage.transfer_remark_txt.send_keys(self.tempData)
        self.fundPage.transfer_next_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.transfer_submit_css)
        self.fundPage.pay_pwd_txt.send_keys(UserInfo.PwdPay)
        self.fundPage.transfer_submit_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.confirm_btn_css)
        self.fundPage.confirm_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.transfer_result_box_css)

    # 添加提现账号
    def add_cash_account(self):
        self.fundPage.go_to(Uri.CashAccountPage)
        self.fundPage.wait_until_clickable(self.fundPage.add_cash_account_css)
        self.fundPage.add_cash_account_btn.click()
        self.fundPage.wait_until_clickable(self.fundPage.confirm_btn_css)
        self.fundPage.bank_list[1].click()
        self.fundPage.bank_account_txt.send_keys('1234567890')
        self.fundPage.province_list[1].click()
        self.fundPage.city_list[1].click()
        self.fundPage.sub_bank[1].click()
        self.fundPage.confirm_btn.click()

    # 编辑提现账号
    def edit_cash_account(self):
        self.fundPage.go_to(Uri.CashAccountPage)
        self.fundPage.edit_cash_account_link.click()
        self.fundPage.wait_until_clickable(self.fundPage.confirm_btn_css)
        self.fundPage.bank_list[2].click()
        self.fundPage.bank_account_txt.clear()
        self.fundPage.bank_account_txt.send_keys('1234567890')
        self.fundPage.province_list[0].click()
        self.fundPage.city_list[0].click()
        self.fundPage.sub_bank[0].click()
        self.fundPage.confirm_btn.click()

    # 删除提现账号
    def delete_cash_account(self):
        self.fundPage.go_to(Uri.CashAccountPage)
        for i in range(self.fundPage.cash_account_num):
            self.fundPage.delete_cash_account_link.click()
            time.sleep(1)
            self.fundPage.delete_cash_account_confirm_btn.click()
            time.sleep(1)

    # 修改支付密码
    def change_pay_pwd(self, old_pwd, new_pwd):
        self.fundPage.go_to(Uri.EditPasswordPage)
        self.fundPage.old_pwd_txt.send_keys(old_pwd)
        self.fundPage.new_pwd_txt.send_keys(new_pwd)
        self.fundPage.new_pwd_repeat_txt.send_keys(new_pwd)
        self.fundPage.change_pwd_submit_btn.click()

    # 进行提现操作
    def do_cash_back(self):
        self.fundPage.go_to(Uri.CashBackPage)
        self.fundPage.back_money_amount_txt.send_keys('1.01')
        self.fundPage.back_money_next_btn.click()
        if self.fundPage.back_money_remain_times[6].text != '0':
            self.fundPage.back_money_pay_password_txt.send_keys(UserInfo.PwdPay)
            self.fundPage.back_money_submit_btn.click()
            time.sleep(1)
            self.fundPage.back_money_confirm_btn.click()
            self.tempData = 1
        else:
            self.tempData = 0

    # 验证汇款成功
    def verify_postal_recharge_success(self):
        self.fundPage.go_to(Uri.PostalRechargeNotePage)
        time.sleep(1)
        return (self.fundPage.first_row_data[1].text == self.tempData and
                self.fundPage.first_row_data[2].text == '0.01' and
                self.fundPage.first_row_data[4].text == '测试用，无需处理！')

    # 验证转账成功
    def verify_transfer_success(self):
        self.fundPage.go_to(Uri.TransferDetailPage)
        time.sleep(1)
        return self.fundPage.first_row_data[6].text == self.tempData + '(转到' + UserInfo.User1 + ')'

    # 获取成功提示条信息
    def get_top_msg_text(self):
        self.fundPage.wait_until_clickable(self.fundPage.msg_bar_css)
        return self.fundPage.msg_bar.text

    # 获取修改密码成功提示文本
    def get_change_pay_success_text(self):
        return self.fundPage.change_pay_pwd_success_msg.text

    def get_cash_back_success_text(self):
        return self.fundPage.back_money_success_msg.text
