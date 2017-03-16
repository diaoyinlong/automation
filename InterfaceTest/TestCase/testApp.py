import unittest
from Module import AppInfo, UserInfo, IAddress, TestData, Config
from Public.Toolkit import Toolkit


class UserAppInterfaceTest(unittest.TestCase):
    # 用户登录
    def testUserLogin(self):
        data = {
            'username': UserInfo.User2,
            'password': UserInfo.PwdLogin,
            'appId': AppInfo.Android,
            'appName': AppInfo.AppName,
            'apiId': AppInfo.ApiID
        }
        values = Toolkit.get_response_from_server(IAddress.Login, data)
        self.assertEqual(4, len(values))
        self.assertIsNotNone(values['code'])
        self.assertEqual('登录成功', values['info'])
        self.assertEqual(11, len(values['member']))
        self.assertEqual(UserInfo.User2, values['member']['nickname'])
        self.assertEqual(UserInfo.UserID2, values['member']['uid'])
        self.assertEqual(1, values['status'])
        self.assertTrue(values['member']['auction'] >= 0 and
                        int(values['member']['bind']) >= 0 and
                        values['member']['email'] is not None and
                        values['member']['funds'] >= 0 and
                        values['member']['mobile'] is not None and
                        values['member']['photo'] is not None and
                        values['member']['shop'] >= 0 and
                        values['member']['shortToken'] != '' and
                        values['member']['token'] != '')

    # 卖家中心用户登录
    def testSellerLogin(self):
        data = {
            'apiId': AppInfo.ApiID,
            'username': UserInfo.User2,
            'password': UserInfo.PwdLogin,
        }
        values = Toolkit.get_response_from_server(IAddress.SellerLogin, data)
        self.assertEqual(8, len(values))
        self.assertEqual(1, values['isAuction'])
        self.assertEqual(1, values['isSeller'])
        self.assertEqual(UserInfo.User2, values['nickname'])
        self.assertTrue(values['photo'] != '' and
                        values['short'] != '' and
                        values['token'] != '')
        self.assertEqual(1, values['status'])
        self.assertEqual(UserInfo.UserID2, values['uid'])

    # 卖家中心用户注销
    def testSellerLogout(self):
        data = {
            'apiId': AppInfo.ApiID,
            'token': Toolkit.get_seller_token()
        }
        values = Toolkit.get_response_from_server(IAddress.SellerLogout, data)
        self.assertEqual(1, values['status'])

    # 获取用户信息
    def testUserInfo(self):
        data = {
            'userId': UserInfo.UserID2
        }
        values = Toolkit.get_response_from_server(IAddress.UserInfo, data)
        self.assertEqual(4, len(values))
        self.assertEqual(6, len(values['auction']))
        self.assertTrue(values['auction']['address'] is not None and
                        values['auction']['capitalGuarantee'] >= 0 and
                        values['auction']['isRealAuth'] != '' and
                        values['auction']['level'] >= 0 and
                        values['auction']['openedTime'] != '' and
                        values['auction']['telephone'] >= 0)

        self.assertEqual(15, len(values['member']))
        self.assertEqual(1, values['member']['auctionState'])
        self.assertTrue(values['member']['avatar'] != '' and
                        values['member']['buyerCredit'] >= 0 and
                        values['member']['buyerFavorable'] != '' and
                        values['member']['fundNumber'] > 0 and
                        values['member']['level'] >= 0 and
                        values['member']['mobile'] is not None and
                        values['member']['passDate'] != '' and
                        values['member']['regDate'] != '' and
                        values['member']['sellerCredit'] >= 0 and
                        values['member']['sellerFavorable'] != '')
        self.assertEqual(UserInfo.User2, values['member']['nickName'])
        self.assertEqual('刁某人的书摊', values['member']['shopName'])
        self.assertEqual(1, values['member']['shopState'])
        self.assertEqual(UserInfo.UserID2, values['member']['userId'])
        self.assertEqual(8, len(values['shop']))
        self.assertEqual('孔夫子旧书网', values['shop']['address'])
        self.assertEqual('刁某人的书摊', values['shop']['shopName'])
        self.assertTrue(values['shop']['capitalGuarantee'] >= 0 and
                        values['shop']['isRealAuth'] != '' and
                        values['shop']['level'] >= 0 and
                        values['shop']['mobile'] is not None and
                        values['shop']['shopId'] != '' and
                        values['shop']['telephone'] is not None)
        self.assertEqual(1, values['status'])

    # 用户注册
    def testUserRegister(self):
        name = 'autotest_' + Toolkit.get_random_value().lower()
        data = {
            'username': name,
            'password': UserInfo.PwdLogin,
            'appId': AppInfo.Android,
            'appName': AppInfo.AppName
        }
        values = Toolkit.get_response_from_server(IAddress.Register, data)
        self.assertEqual(4, len(values))
        self.assertIsNotNone(values['code'])
        self.assertEqual('注册成功', values['info'])
        self.assertEqual(6, len(values['member']))
        self.assertEqual(name, values['member']['nickname'])
        self.assertEqual(1, values['status'])
        self.assertTrue(values['member']['email'] is not None and
                        values['member']['mobile'] is not None and
                        values['member']['photo'] != '' and
                        values['member']['token'] != '' and
                        values['member']['uid'] != '')

    # 获取用户收货地址
    def testListUserAddress(self):
        data = {
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.ListUserAddress, data)
        self.assertEqual(2, len(values))
        if len(values['list']) != 0:
            self.assertEqual(9, len(values['list'][0]))
            self.assertTrue(values['list'][0]['address'] != '' and
                            values['list'][0]['area'] != '' and
                            values['list'][0]['areaDesc'] != '' and
                            values['list'][0]['def'] != '' and
                            values['list'][0]['id'] != '' and
                            values['list'][0]['mobile'] is not None and
                            values['list'][0]['name'] != '' and
                            values['list'][0]['telephone'] is not None and
                            values['list'][0]['zipCode'] != '')
        self.assertEqual(1, values['status'])

    # 添加用户收货地址
    def testAddUserAddress(self):
        data = {
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'id': 0,
            'name': 'interface test',
            'area': 1001000000,
            'address': 'interface test',
            'zipCode': '100000',
            'telephone': '',
            'mobile': '12345678'
        }
        values = Toolkit.get_response_from_server(IAddress.ReplaceUserAddress, data)
        self.assertEqual(2, len(values))
        self.assertTrue(values['id'] != '' and
                        values['status'] == 1)
        TestData.TempID = values['id']

    # 编辑用户收货地址
    def testEditUserAddress(self):
        data = {
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'id': TestData.TempID,
            'name': 'interface Edit test',
            'area': 1001000000,
            'address': 'interface Edit test',
            'zipCode': '100000',
            'telephone': '',
            'mobile': '12345678'
        }
        values = Toolkit.get_response_from_server(IAddress.ReplaceUserAddress, data)
        self.assertEqual(2, len(values))
        self.assertTrue(values['id'] == TestData.TempID and
                        values['status'] == 1)

    # 设置默认地址
    def testSetDefaultAddress(self):
        data = {
            'id': TestData.TempID,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.SetDefaultAddress, data)
        self.assertEqual(1, len(values))
        self.assertEqual(1, values['status'])

    # 删除用户地址
    def testDeleteUserAddress(self):
        data = {
            'id': TestData.TempID,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.DeleteUserAddress, data)
        self.assertEqual(1, len(values))
        self.assertEqual(1, values['status'])

    # 获取地区列表
    def testGetAreaList(self):
        data = {
            'areaId': '-1',
            'levelId': '-1',
            'isNeedShort': '0'
        }
        values = Toolkit.get_response_from_server(IAddress.GetAreaList, data)
        self.assertEqual(2, len(values))
        self.assertEqual(1, values['status'])

        self.assertEqual(3, len(values['list'][0]))
        self.assertEqual(1000000000, values['list'][0]['areaId'])
        self.assertEqual('北京市', values['list'][0]['areaName'])
        self.assertEqual(1, values['list'][0]['level'])

        self.assertEqual(3, len(values['list'][1]))
        self.assertEqual(2000000000, values['list'][1]['areaId'])
        self.assertEqual('上海市', values['list'][1]['areaName'])
        self.assertEqual(1, values['list'][1]['level'])

        self.assertEqual(3, len(values['list'][2]))
        self.assertEqual(3000000000, values['list'][2]['areaId'])
        self.assertEqual('天津市', values['list'][2]['areaName'])
        self.assertEqual(1, values['list'][2]['level'])

        self.assertEqual(3, len(values['list'][3]))
        self.assertEqual(4000000000, values['list'][3]['areaId'])
        self.assertEqual('重庆市', values['list'][3]['areaName'])
        self.assertEqual(1, values['list'][3]['level'])

        self.assertEqual(3, len(values['list'][4]))
        self.assertEqual(5000000000, values['list'][4]['areaId'])
        self.assertEqual('安徽省', values['list'][4]['areaName'])
        self.assertEqual(1, values['list'][4]['level'])

        self.assertEqual(3, len(values['list'][5]))
        self.assertEqual(6000000000, values['list'][5]['areaId'])
        self.assertEqual('福建省', values['list'][5]['areaName'])
        self.assertEqual(1, values['list'][5]['level'])

        self.assertEqual(3, len(values['list'][6]))
        self.assertEqual(7000000000, values['list'][6]['areaId'])
        self.assertEqual('甘肃省', values['list'][6]['areaName'])
        self.assertEqual(1, values['list'][6]['level'])

        self.assertEqual(3, len(values['list'][7]))
        self.assertEqual(8000000000, values['list'][7]['areaId'])
        self.assertEqual('广东省', values['list'][7]['areaName'])
        self.assertEqual(1, values['list'][7]['level'])

        self.assertEqual(3, len(values['list'][8]))
        self.assertEqual(9000000000, values['list'][8]['areaId'])
        self.assertEqual('广西壮族自治区', values['list'][8]['areaName'])
        self.assertEqual(1, values['list'][8]['level'])

        self.assertEqual(3, len(values['list'][9]))
        self.assertEqual(10000000000, values['list'][9]['areaId'])
        self.assertEqual('贵州省', values['list'][9]['areaName'])
        self.assertEqual(1, values['list'][9]['level'])

        self.assertEqual(3, len(values['list'][10]))
        self.assertEqual(11000000000, values['list'][10]['areaId'])
        self.assertEqual('海南省', values['list'][10]['areaName'])
        self.assertEqual(1, values['list'][10]['level'])

        self.assertEqual(3, len(values['list'][11]))
        self.assertEqual(12000000000, values['list'][11]['areaId'])
        self.assertEqual('河北省', values['list'][11]['areaName'])
        self.assertEqual(1, values['list'][11]['level'])

        self.assertEqual(3, len(values['list'][12]))
        self.assertEqual(13000000000, values['list'][12]['areaId'])
        self.assertEqual('河南省', values['list'][12]['areaName'])
        self.assertEqual(1, values['list'][12]['level'])

        self.assertEqual(3, len(values['list'][13]))
        self.assertEqual(14000000000, values['list'][13]['areaId'])
        self.assertEqual('黑龙江省', values['list'][13]['areaName'])
        self.assertEqual(1, values['list'][13]['level'])

        self.assertEqual(3, len(values['list'][14]))
        self.assertEqual(15000000000, values['list'][14]['areaId'])
        self.assertEqual('湖北省', values['list'][14]['areaName'])
        self.assertEqual(1, values['list'][14]['level'])

        self.assertEqual(3, len(values['list'][15]))
        self.assertEqual(16000000000, values['list'][15]['areaId'])
        self.assertEqual('湖南省', values['list'][15]['areaName'])
        self.assertEqual(1, values['list'][15]['level'])

        self.assertEqual(3, len(values['list'][16]))
        self.assertEqual(17000000000, values['list'][16]['areaId'])
        self.assertEqual('吉林省', values['list'][16]['areaName'])
        self.assertEqual(1, values['list'][16]['level'])

        self.assertEqual(3, len(values['list'][17]))
        self.assertEqual(18000000000, values['list'][17]['areaId'])
        self.assertEqual('江苏省', values['list'][17]['areaName'])
        self.assertEqual(1, values['list'][17]['level'])

        self.assertEqual(3, len(values['list'][18]))
        self.assertEqual(19000000000, values['list'][18]['areaId'])
        self.assertEqual('江西省', values['list'][18]['areaName'])
        self.assertEqual(1, values['list'][18]['level'])

        self.assertEqual(3, len(values['list'][19]))
        self.assertEqual(20000000000, values['list'][19]['areaId'])
        self.assertEqual('辽宁省', values['list'][19]['areaName'])
        self.assertEqual(1, values['list'][19]['level'])

        self.assertEqual(3, len(values['list'][20]))
        self.assertEqual(21000000000, values['list'][20]['areaId'])
        self.assertEqual('内蒙古自治区', values['list'][20]['areaName'])
        self.assertEqual(1, values['list'][20]['level'])

        self.assertEqual(3, len(values['list'][21]))
        self.assertEqual(22000000000, values['list'][21]['areaId'])
        self.assertEqual('宁夏回族自治区', values['list'][21]['areaName'])
        self.assertEqual(1, values['list'][21]['level'])

        self.assertEqual(3, len(values['list'][22]))
        self.assertEqual(23000000000, values['list'][22]['areaId'])
        self.assertEqual('青海省', values['list'][22]['areaName'])
        self.assertEqual(1, values['list'][22]['level'])

        self.assertEqual(3, len(values['list'][23]))
        self.assertEqual(24000000000, values['list'][23]['areaId'])
        self.assertEqual('山东省', values['list'][23]['areaName'])
        self.assertEqual(1, values['list'][23]['level'])

        self.assertEqual(3, len(values['list'][24]))
        self.assertEqual(25000000000, values['list'][24]['areaId'])
        self.assertEqual('山西省', values['list'][24]['areaName'])
        self.assertEqual(1, values['list'][24]['level'])

        self.assertEqual(3, len(values['list'][25]))
        self.assertEqual(26000000000, values['list'][25]['areaId'])
        self.assertEqual('陕西省', values['list'][25]['areaName'])
        self.assertEqual(1, values['list'][25]['level'])

        self.assertEqual(3, len(values['list'][26]))
        self.assertEqual(27000000000, values['list'][26]['areaId'])
        self.assertEqual('四川省', values['list'][26]['areaName'])
        self.assertEqual(1, values['list'][26]['level'])

        self.assertEqual(3, len(values['list'][27]))
        self.assertEqual(28000000000, values['list'][27]['areaId'])
        self.assertEqual('西藏自治区', values['list'][27]['areaName'])
        self.assertEqual(1, values['list'][27]['level'])

        self.assertEqual(3, len(values['list'][28]))
        self.assertEqual(29000000000, values['list'][28]['areaId'])
        self.assertEqual('新疆维吾尔自治区', values['list'][28]['areaName'])
        self.assertEqual(1, values['list'][28]['level'])

        self.assertEqual(3, len(values['list'][29]))
        self.assertEqual(30000000000, values['list'][29]['areaId'])
        self.assertEqual('云南省', values['list'][29]['areaName'])
        self.assertEqual(1, values['list'][29]['level'])

        self.assertEqual(3, len(values['list'][30]))
        self.assertEqual(31000000000, values['list'][30]['areaId'])
        self.assertEqual('浙江省', values['list'][30]['areaName'])
        self.assertEqual(1, values['list'][30]['level'])

        self.assertEqual(3, len(values['list'][31]))
        self.assertEqual(32000000000, values['list'][31]['areaId'])
        self.assertEqual('澳门特别行政区', values['list'][31]['areaName'])
        self.assertEqual(1, values['list'][31]['level'])

        self.assertEqual(3, len(values['list'][32]))
        self.assertEqual(33000000000, values['list'][32]['areaId'])
        self.assertEqual('中国台湾', values['list'][32]['areaName'])
        self.assertEqual(1, values['list'][32]['level'])

        self.assertEqual(3, len(values['list'][33]))
        self.assertEqual(34000000000, values['list'][33]['areaId'])
        self.assertEqual('香港特别行政区', values['list'][33]['areaName'])
        self.assertEqual(1, values['list'][33]['level'])

        self.assertEqual(3, len(values['list'][34]))
        self.assertEqual(40000000000, values['list'][34]['areaId'])
        self.assertEqual('海外地区', values['list'][34]['areaName'])
        self.assertEqual(1, values['list'][34]['level'])

        self.assertEqual(3, len(values['list'][35]))
        self.assertEqual(35000000000, values['list'][35]['areaId'])
        self.assertEqual('其他', values['list'][35]['areaName'])
        self.assertEqual(1, values['list'][35]['level'])

    # 获取卖家支持的支付方式
    def testGetSupportPayType(self):
        data = {
            'userId': int(UserInfo.UserID3),
            'type': 1
        }
        values = Toolkit.get_response_from_server(IAddress.GetSupportPayType, data)
        self.assertEqual(2, len(values))
        self.assertEqual(3, len(values['list']))
        self.assertEqual(2, len(values['list'][0]))
        self.assertEqual(2, len(values['list'][1]))
        self.assertEqual(2, len(values['list'][2]))
        self.assertEqual(1, values['status'])
        self.assertEqual(2, values['list'][0]['payType'])
        self.assertEqual('即时到账', values['list'][0]['typeName'])

        self.assertEqual(1, values['list'][1]['payType'])
        self.assertEqual('中介保护', values['list'][1]['typeName'])

        self.assertEqual(3, values['list'][2]['payType'])
        self.assertEqual('线下付款', values['list'][2]['typeName'])

    # 获取用户资金信息
    def testGetUserCommissionInfo(self):
        data = {
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'userId': UserInfo.UserID1
        }
        values = Toolkit.get_response_from_server(IAddress.GetUserCommissionInfo, data)
        self.assertEqual(8, len(values))
        self.assertEqual(1, values['status'])
        self.assertTrue(values['availableBalance'] != '' and
                        values['balance'] != '' and
                        values['frozenAmount'] != '' and
                        values['isActive'] != '' and
                        values['isCertified'] != '' and
                        values['isValid'] != '' and
                        values['realname'] != '')

    # 按照昵称搜索书友
    def testSearchUserByName(self):
        data = {
            'key': 'autotest',
            'page': 1,
            'type': 1
        }
        values = Toolkit.get_response_from_server(IAddress.SearchUser, data)
        self.assertEqual(1, values['status'])
        self.assertEqual(4, len(values))
        self.assertTrue(values['itemNum'] >= 0 and
                        values['pageNum'] >= 0)
        if len(values['list']) > 0:
            self.assertEqual(3, len(values['list'][0]))
            self.assertTrue(values['list'][0]['avatar'] != '' and
                            values['list'][0]['nickName'] != '' and
                            values['list'][0]['userId'] != 0)

    # 按照ID搜索书友
    def testSearchUserByID(self):
        data = {
            'key': UserInfo.UserID1,
            'page': 1,
            'type': 2
        }
        values = Toolkit.get_response_from_server(IAddress.SearchUser, data)
        self.assertEqual(4, len(values))
        self.assertEqual(1, values['status'])
        self.assertEqual(1, values['pageNum'])
        self.assertEqual(1, values['itemNum'])
        self.assertEqual(1, len(values['list']))
        self.assertTrue(values['list'][0]['avatar'] != '')
        self.assertEqual(UserInfo.User1, values['list'][0]['nickName'])
        self.assertEqual(int(UserInfo.UserID1), values['list'][0]['userId'])


class AuctionAppInterfaceTest(unittest.TestCase):
    # 增加拍卖留言
    def testAddLeaveWord(self):
        data = {
            'itemId': int(Config.auctionId),
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'comment': 'interface test'
        }
        values = Toolkit.get_response_from_server(IAddress.AddLeaveWord, data)
        self.assertEqual(1, len(values))
        self.assertEqual(1, values['status'])

    # 获取拍卖详情
    def testGetAuction(self):
        data = {
            'itemId': int(Config.auctionId)
        }
        values = Toolkit.get_response_from_server(IAddress.GetAuction, data)
        self.assertEqual(2, len(values))
        self.assertEqual(19, len(values['item']))
        self.assertEqual(1, values['status'])
        self.assertEqual(int(Config.auctionId), values['item']['id'])
        self.assertEqual(int(UserInfo.UserID3), values['item']['seller']['id'])
        self.assertEqual(UserInfo.User3, values['item']['seller']['nickname'])
        self.assertTrue(len(values['item']['descList']) != 0 and
                        len(values['item']['imageList']) != 0 and
                        len(values['item']['shippingList']) != 0 and
                        len(values['item']['albumList']) != 0 and
                        values['item']['beginPrice'] != '' and
                        values['item']['beginTime'] != '' and
                        values['item']['bidNum'] != '' and
                        values['item']['buyer']['id'] is not None and
                        values['item']['buyer']['nickname'] is not None and
                        values['item']['currTime'] != '' and
                        values['item']['endTime'] != '' and
                        values['item']['maxPrice'] != '' and
                        values['item']['minAddPrice'] != '' and
                        values['item']['name'] != '' and
                        values['item']['promise'] is not None and
                        values['item']['seller']['credit'] != '' and
                        values['item']['seller']['rate'] != '' and
                        values['item']['specialArea'] != '' and
                        values['item']['url'] != '' and
                        values['item']['viewedNum'] != '')

    # 手动竞价
    def testBidAuction(self):
        auction_info = Toolkit.get_response_from_server(IAddress.GetAuction, {'itemId': int(Config.auctionId)})
        max_price = auction_info['item']['maxPrice']
        min_add_price = auction_info['item']['minAddPrice']

        data = {
            'itemId': int(Config.auctionId),
            'bidType': 0,
            'price': max_price + min_add_price * 2,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.BidAuction, data)
        self.assertEqual(1, values['status'])
        self.assertEqual(6, len(values))
        self.assertEqual(UserInfo.User1, values['buyer'])
        self.assertEqual(float(max_price + min_add_price * 2), float(values['price']))
        self.assertTrue(values['beginTime'] != '' and
                        values['currTime'] != '' and
                        values['endTime'] != '')

    # 代理竞价
    def testProxyBidAuction(self):
        auction_info = Toolkit.get_response_from_server(IAddress.GetAuction, {'itemId': int(Config.auctionId)})
        max_price = auction_info['item']['maxPrice']
        min_add_price = auction_info['item']['minAddPrice']

        data = {
            'itemId': int(Config.auctionId),
            'bidType': 1,
            'price': max_price + min_add_price * 2,
            'token': Toolkit.get_user_token(UserInfo.User2, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.BidAuction, data)
        self.assertEqual(6, len(values))
        self.assertEqual(1, values['status'])
        self.assertEqual(UserInfo.User2, values['buyer'])
        self.assertEqual(float(max_price + min_add_price), float(values['price']))
        self.assertTrue(values['beginTime'] != '' and
                        values['currTime'] != '' and
                        values['endTime'] != '')

    # 修改我的心里价位
    def testChangeMyMaxPrice(self):
        auction_info = Toolkit.get_response_from_server(IAddress.GetAuction, {'itemId': int(Config.auctionId)})
        max_price = auction_info['item']['maxPrice']
        min_add_price = auction_info['item']['minAddPrice']

        data = {
            'itemId': int(Config.auctionId),
            'price': max_price + min_add_price * 2,
            'token': Toolkit.get_user_token(UserInfo.User2, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.ChangeMyMaxPrice, data)
        self.assertEqual(6, len(values))
        self.assertEqual(1, values['status'])
        self.assertEqual(UserInfo.User2, values['buyer'])
        self.assertTrue(values['beginTime'] != '' and
                        values['currTime'] != '' and
                        values['endTime'] != '' and
                        values['price'] != '')

    # 加入拍卖收藏夹
    def testInsertUserFav(self):
        data = {
            'itemId': int(Config.auctionId),
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.InsertUserFav, data)
        self.assertEqual(2, len(values))
        self.assertEqual(1, values['status'])
        TestData.TempID = values['favId']

    # 拍品是否被收藏
    def testIsInUserFav(self):
        data = {
            'itemId': int(Config.auctionId),
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.IsInUserFav, data)
        self.assertEqual(2, len(values))
        self.assertEqual(1, values['status'])
        TestData.TempID = values['favId']

    # 获取拍卖收藏列表
    def testListUserFav(self):
        data = {
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'page': 1
        }
        values = Toolkit.get_response_from_server(IAddress.ListUserFav, data)
        self.assertEqual(4, len(values))
        self.assertEqual(1, values['status'])
        self.assertTrue(values['itemNum'] >= 0 and
                        values['pageNum'] >= 0)
        if len(values['list']) > 0:
            self.assertEqual(18, len(values['list'][0]))
            self.assertTrue(values['list'][0]['beginPrice'] > 0 and
                            values['list'][0]['beginTime'] > 0 and
                            values['list'][0]['bidNum'] > 0 and
                            values['list'][0]['currTime'] > 0 and
                            values['list'][0]['endTime'] > 0 and
                            values['list'][0]['favId'] > 0 and
                            values['list'][0]['id'] > 0 and
                            values['list'][0]['maxPrice'] > 0 and
                            values['list'][0]['minAddPrice'] >= 0 and
                            values['list'][0]['name'] != '' and
                            values['list'][0]['nickname'] != '' and
                            values['list'][0]['remark'] is not None and
                            values['list'][0]['smallImg'] != '' and
                            values['list'][0]['status'] > 0 and
                            values['list'][0]['userId'] != '' and
                            values['list'][0]['viewedNum'] >= 0)
            self.assertEqual(2, len(values['list'][0]['buyer']))
            self.assertTrue(values['list'][0]['buyer']['id'] > 0 and
                            values['list'][0]['buyer']['nickname'] != '')
            self.assertEqual(2, len(values['list'][0]['seller']))
            self.assertTrue(values['list'][0]['seller']['id'] > 0 and
                            values['list'][0]['seller']['nickname'] != '')

    # 修改收藏备注
    def testEditUserFavRemark(self):
        data = {
            'favId': TestData.TempID,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin),
            'remark': 'interface test'
        }
        values = Toolkit.get_response_from_server(IAddress.EditUserFavRemark, data)
        self.assertEqual(1, len(values))
        self.assertEqual(1, values['status'])

    # 删除拍卖收藏
    def testDeleteUserFav(self):
        data = {
            'favIds': TestData.TempID,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.DeleteUserFav, data)
        self.assertEqual(1, len(values))
        self.assertEqual(1, values['status'])

    # 获取用户资金信息
    def testGetBaiInfo(self):
        data = {
            'itemId': int(Config.auctionId),
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.GetBailInfo, data)
        self.assertEqual(6, len(values))
        self.assertEqual(1, values['status'])
        self.assertTrue(values['availableBalance'] != '' and
                        values['balance'] != '' and
                        values['frozenAmount'] != '' and
                        values['lostBalance'] >= 0 and
                        values['maxPrice'] >= 0)

    # 获取拍卖交易详情
    def testGetUserTrade(self):
        data = {
            'type': 1,
            'tradeId': Config.tradeId,
            'token': Toolkit.get_user_token(UserInfo.User1, UserInfo.PwdLogin)
        }
        values = Toolkit.get_response_from_server(IAddress.GetUserTrade, data)
        self.assertEqual(7, len(values))
        self.assertEqual(1, values['status'])
        self.assertEqual('查看评价', values['item']['actions'][0]['desc'])
        self.assertEqual('viewReview', values['item']['actions'][0]['name'])
        self.assertEqual(UserInfo.UserID1, values['item']['buyer']['id'])
        self.assertEqual(UserInfo.User1, values['item']['buyer']['nickname'])
        self.assertEqual(UserInfo.UserID3, values['item']['seller']['id'])
        self.assertEqual(UserInfo.User3, values['item']['seller']['nickname'])
        self.assertEqual('registerPost', values['item']['shippingList'][0]['id'])
        self.assertEqual('挂号印刷品', values['item']['shippingList'][0]['name'])
        self.assertEqual('2', values['item']['shippingList'][0]['price'])
        self.assertEqual('express', values['item']['shippingList'][1]['id'])
        self.assertEqual('快递', values['item']['shippingList'][1]['name'])
        self.assertEqual('3', values['item']['shippingList'][1]['price'])
        self.assertEqual('generalParcel', values['item']['shippingList'][2]['id'])
        self.assertEqual('普通包裹', values['item']['shippingList'][2]['name'])
        self.assertEqual('4', values['item']['shippingList'][2]['price'])
        self.assertEqual('ems', values['item']['shippingList'][3]['id'])
        self.assertEqual('EMS', values['item']['shippingList'][3]['name'])
        self.assertEqual('5', values['item']['shippingList'][3]['price'])
        self.assertEqual('expressParcels', values['item']['shippingList'][4]['id'])
        self.assertEqual('快递包裹', values['item']['shippingList'][4]['name'])
        self.assertEqual('6', values['item']['shippingList'][4]['price'])
        self.assertEqual(Config.tradeId, values['item']['tradeId'])
        self.assertEqual('successful', values['item']['status'])
        self.assertEqual(7, len(values['address']))
        self.assertTrue(values['address']['address'] != '' and
                        values['address']['area'] != '' and
                        values['address']['areaDesc'] != '' and
                        (values['address']['mobile'] != '' or values['address']['telephone'] != '') and
                        values['address']['zipCode'] is not None and
                        values['address']['name'] != '')
        self.assertEqual(3, len(values['deliver']))
        self.assertTrue(values['deliver']['companyName'] != '' and
                        values['deliver']['shipName'] != '' and
                        values['deliver']['shipNum'] != '')
        self.assertEqual(23, len(values['item']))
        self.assertTrue(values['item']['adjustAmount'] != '' and
                        values['item']['buyerReviewId'] > 0 and
                        values['item']['deductedNum'] > 0 and
                        values['item']['desc'] != '' and
                        values['item']['goodsAmount'] != '' and
                        values['item']['hasRefund'] >= 0 and
                        values['item']['itemList'][0]['count'] > 0 and
                        values['item']['itemList'][0]['id'] != '' and
                        values['item']['itemList'][0]['name'] != '' and
                        values['item']['itemList'][0]['price'] != '' and
                        values['item']['itemList'][0]['smallImg'] != '' and
                        (values['item']['payId'] == '中介保护' or values['item']['payId'] == '即时到账' or values['item'][
                            'payId'] == '线下付款') and
                        values['item']['payStatus'] != '' and
                        values['item']['reviewed'] > 0 and
                        values['item']['sellerReviewId'] > 0 and
                        values['item']['shippingFee'] is not None and
                        values['item']['shippingName'] != '' and
                        values['item']['shippingStatus'] != '' and
                        values['item']['shippingUrl'] != '' and
                        values['item']['status'] != '' and
                        values['item']['tradeAmount'] != '' and
                        values['item']['tradeId'] and
                        values['item']['wShippingFee'] > 0)
        if len(values['logs']) > 0:
            self.assertEqual(2, len(values['logs'][0]))
            self.assertTrue(values['logs'][0]['date'] != '' and
                            values['logs'][0]['info'] != '')
        self.assertEqual(3, len(values['shipping']))
        self.assertTrue(values['shipping']['id'] != '' and
                        values['shipping']['name'] != '' and
                        values['shipping']['price'] >= 0)

    # 获取拍卖列表
    def testListAuction(self):
        for i in range(9):
            data = {
                'type': i,
                'page': 1,
                'order': 1
            }
            values = Toolkit.get_response_from_server(IAddress.ListAuction, data)
            self.assertTrue(int(values['itemNum']) >= 0 and
                            values['pageNum'] >= 0)
            self.assertEqual(1, values['status'])
            if len(values['list']) != 0:
                self.assertEqual(13, len(values['list'][0]))
                self.assertEqual(2, len(values['list'][0]['buyer']))
                self.assertEqual(2, len(values['list'][0]['seller']))
                self.assertTrue(values['list'][0]['beginPrice'] >= 0 and
                                values['list'][0]['beginTime'] >= 0 and
                                values['list'][0]['bidNum'] >= 0 and
                                values['list'][0]['currTime'] >= 0 and
                                values['list'][0]['endTime'] >= 0 and
                                values['list'][0]['id'] >= 0 and
                                values['list'][0]['maxPrice'] >= 0 and
                                values['list'][0]['minAddPrice'] >= 0 and
                                values['list'][0]['name'] != '' and
                                values['list'][0]['smallImg'] != '' and
                                values['list'][0]['viewedNum'] >= 0 and
                                values['list'][0]['buyer']['id'] >= 0 and
                                values['list'][0]['buyer']['nickname'] != '' and
                                values['list'][0]['seller']['id'] >= 0 and
                                values['list'][0]['seller']['nickname'] != '')

    # 获取出价记录
    def testListAuctionRecord(self):
        data = {
            'itemId': Config.auctionId,
            'page': 1
        }
        values = Toolkit.get_response_from_server(IAddress.ListAuctionRecord, data)
        self.assertEqual(4, len(values))
        self.assertEqual(1, values['status'])
        self.assertTrue(values['pageNum'] >= 0)
        self.assertTrue(len(values['itemNum']) >= 0)
        if len(values['list']) != 0:
            self.assertEqual(6, len(values['list'][0]))
            self.assertTrue(values['list'][0]['dateTime'] != '' and
                            values['list'][0]['isActing'] != '' and
                            values['list'][0]['isOut'] != '' and
                            values['list'][0]['nickname'] != '' and
                            values['list'][0]['price'] > 0 and
                            values['list'][0]['userId'] != '')
