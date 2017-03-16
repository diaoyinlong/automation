from Module import Uri, UserInfo


class BaseAction:
    def __init__(self, page):
        self.page = page

    # 登录
    def login(self, user):
        self.page.go_to(Uri.LoginPage)
        if user == 'user1':
            self.page.login_name_txt.send_keys(UserInfo.User1)
        if user == 'user2':
            self.page.login_name_txt.send_keys(UserInfo.User2)
        if user == 'user3':
            self.page.login_name_txt.send_keys(UserInfo.User3)
        self.page.login_password_txt.send_keys(UserInfo.PwdLogin)
        self.page.login_submit_btn.click()
        self.page.wait_until_clickable(self.page.page_index_css)
