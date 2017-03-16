from Module import Config

# 买家1
User1 = 'autotest02'
FundID1 = '100005256107'

# 买家2
User2 = '刁某人'

# 卖家
User3 = (Config.env == 'External' and 'autotest002' or 'autotest04')

# 登录密码
PwdLogin = (Config.env == 'External' and '!@#$%^' or '123456')

# 支付密码
PwdPay = 'test123'
