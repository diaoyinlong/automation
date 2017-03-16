from Module import Config

prefix_shop = ''
prefix_pay = ''
prefix_user = ''
prefix_auction = ''
prefix_message = ''
prefix_m_user = ''
prefix_m_auction = ''
prefix_m_shop = ''
prefix_m_pay = ''

# Internal uri prefix
if Config.env == 'Internal':
    prefix_shop = 'http://neibushop.kongfz.com'
    prefix_pay = 'https://neibupay.kongfz.com'
    prefix_user = 'http://neibuuser.kongfz.com'
    prefix_auction = 'http://neibuwww.kongfz.cn'
    prefix_message = 'http://neibumessage.kongfz.com'
    prefix_m_default = 'https://neibum.kongfz.com'
    prefix_m_user = 'http://neibumuser.kongfz.com'
    prefix_m_auction = 'http://neibumwww.kongfz.cn'
    prefix_m_shop = 'http://neibumshop.kongfz.com'
    prefix_m_pay = 'https://neibumpay.kongfz.com'

    # 图书详情页
    BookDetailPage = 'http://neibubook.kongfz.com/181449/5715/'
    LoginPage = 'https://neibulogin.kongfz.com/'

    # Search
    SearchPage = 'http://neibusearch.kongfz.com/'

    # M Site
    MLoginPage = 'https://neibum.kongfz.com/m/?mustLogin=1'
    MSearchPage = 'http://neibumsearch.kongfz.com/'
    MShopPage = 'http://neibushop.kongfz.com/181449/'
    MBookDetailPage = 'http://neibubook.kongfz.com/181449/5715/'
    MContactPage = 'http://neibummessage.kongfz.com/?type=chat#/contacts'

# External uri prefix
elif Config.env == 'External':
    prefix_shop = 'http://shop.kongfz.com'
    prefix_pay = 'https://pay.kongfz.com'
    prefix_user = 'http://user.kongfz.com'
    prefix_auction = 'http://www.kongfz.cn'
    prefix_message = 'http://message.kongfz.com'
    prefix_m_default = 'https://m.kongfz.com'
    prefix_m_user = 'http://muser.kongfz.com'
    prefix_m_auction = 'http://mwww.kongfz.cn'
    prefix_m_shop = 'http://mshop.kongfz.com'
    prefix_m_pay = 'https://mpay.kongfz.com/'

    # 图书详情页
    BookDetailPage = 'http://book.kongfz.com/187380/366726019/'
    LoginPage = 'https://login.kongfz.com/'

    # Search
    SearchPage = 'http://search.kongfz.com/'

    # M Site
    MLoginPage = 'https://m.kongfz.com/m/?mustLogin=1'
    MSearchPage = 'http://msearch.kongfz.com/'
    MShopPage = 'http://shop.kongfz.com/208670/'
    MBookDetailPage = 'http://mbook.kongfz.com/208670/481929004/'
    MContactPage = 'http://mmessage.kongfz.com/?type=chat#/contacts'

# Book Store
BookSellerItemPage = prefix_shop + '/seller/product/item.html'
AddBookPage = prefix_shop + '/seller/product/item.html#add'
CartPage = prefix_shop + '/cart/mycart.html'
DefaultMemberPic = prefix_user + '/images/member/default_member_pic.gif'
FavoriteProductPage = prefix_user + '/buyer/favorite_manage.html'
FavoriteShopPage = prefix_user + '/buyer/favorite_manage.html#shop'
FavoriteSitePage = prefix_user + '/buyer/favorite_manage.html#site'

# Fund
CashAccountPage = prefix_pay + '/account/cashAccount.html'
EditPasswordPage = prefix_pay + '/account/editPwd.html'
PayDetailPage = prefix_pay + '/detail/pay.html'
PostalRechargePage = prefix_pay + '/fill/postal.html'
RefundDetailPage = prefix_pay + '/detail/refund.html'
TransferPage = prefix_pay + '/transfer/transfer.html'
PostalRechargeNotePage = prefix_pay + '/fill/postal_note.html'
TransferDetailPage = prefix_pay + '/detail/transfer.html'
CashBackPage = prefix_pay + '/cash/cash.html'

# Order in book store
BookBuyerOrderPage = prefix_shop + '/buyer/order/order_list.html'
BookBuyerEvaluateOrderPage = prefix_shop + '/buyer/order/order_list.html#buyerReviewed'
BookBuyerPayOrderPage = prefix_shop + '/buyer/order/order_list.html#ConfirmedToPay'
BookBuyerReceivingOrderPage = prefix_shop + '/buyer/order/order_list.html#ShippedToReceipt'
BookBuyerRefundOrderPage = prefix_shop + '/buyer/order/order_list.html#Refund'
BookBuyerSuccessOrderPage = prefix_shop + '/buyer/order/order_list.html#Successful'
BookBuyerConfirmPaymentOrderPage = prefix_shop + '/buyer/order/order_list.html#PaidToConfirm'
BookBuyerAllOrderPage = prefix_shop + '/buyer/order/order_list.html#all'
BookSellerOrderPage = prefix_shop + '/seller/order/order_list.html'
BookSellerAllOrderPage = prefix_shop + '/seller/order/order_list.html#all'
BookSellerDeliveryOrderPage = prefix_shop + '/seller/order/order_list.html#PaidToShip'
BookSellerEvaluateOrderPage = prefix_shop + '/seller/order/order_list.html#sellerReviewed'
BookSellerPayOrderPage = prefix_shop + '/seller/order/order_list.html#ConfirmedToPay'
BookSellerPendingOrderPage = prefix_shop + '/seller/order/order_list.html#Pending'
BookSellerReceivingOrderPage = prefix_shop + '/seller/order/order_list.html#ShippedToReceipt'
BookSellerRefundFinishOrderPage = prefix_shop + '/seller/order/order_list.html#RefundDeald'
BookSellerRefundOrderPage = prefix_shop + '/seller/order/order_list.html#Refund'
BookSellerSuccessOrderPage = prefix_shop + '/seller/order/order_list.html#Successful'

# Trade in auction
AuctionBuyerTradePage = prefix_auction + '/buyer/trade_list.html'
AuctionBuyerAllTradeOrderPage = prefix_auction + '/buyer/trade_list.html#all'
AuctionBuyerWaitToPayOrderPage = prefix_auction + '/buyer/trade_list.html#ConfirmedToPay'
AuctionBuyerWaitToReceiveOrderPage = prefix_auction + '/buyer/trade_list.html#ShippedToReceipt'
AuctionBuyerRefundOrderPage = prefix_auction + '/buyer/trade_list.html#Refund'
AuctionBuyerEvaluateOrderPage = prefix_auction + '/buyer/trade_list.html#buyerReviewed'
AuctionBuyerSuccessOrderPage = prefix_auction + '/buyer/trade_list.html#Successful'
AuctionSellerTradePage = prefix_auction + '/seller/trade_list.html'
AuctionSellerAllTradeOrderPage = prefix_auction + '/seller/trade_list.html#all'
AuctionSellerWaitToPayOrderPage = prefix_auction + '/seller/trade_list.html#ConfirmedToPay'
AuctionSellerConfirmPaymentOrderPage = prefix_auction + '/seller/trade_list.html#PaidToConfirm'
AuctionSellerWaitToDeliveryOrderPage = prefix_auction + '/seller/trade_list.html#PaidToShip'
AuctionSellerRefundOrderPage = prefix_auction + '/seller/trade_list.html#Refund'
AuctionSellerEvaluateOrderPage = prefix_auction + '/seller/trade_list.html#sellerReviewed'
AuctionSellerSuccessOrderPage = prefix_auction + '/seller/trade_list.html#Successful'

# Center
ManageProductCategoryPage = prefix_shop + '/seller/info/shop_product_category.html'
ProductRecyclePage = prefix_shop + '/seller/product/item.html#recycle'
ReceiveAddressPage = prefix_user + '/buyer/receive_address.html'
ChangePwdPage = prefix_user + '/person/edit_password.html'
RecommendPage = prefix_shop + '/seller/product/item.html#column'
SalePage = prefix_shop + '/seller/product/item.html#sale'
UnSoldPage = prefix_shop + '/seller/product/item.html#unsold'
UnCertifyPage = prefix_shop + '/seller/product/item.html#uncertify'
ShopFittingPage = prefix_shop + '/seller/info/shop_fitting.html'
ShopBaseInfoPage = prefix_shop + '/seller/info/shop_info.html'
ShopMemoPage = prefix_shop + '/seller/info/shop_note.html'
ShopBlackListPage = prefix_shop + '/seller/info/shop_blacklist.html'
AuctionBlackListPage = prefix_auction + '/seller/auction_blacklist.html'
SearchFriendPage = prefix_user + '/person/search_friend.html'
MyFriendPage = prefix_message + '/Index/myFriend'
SetOrderAutoConfirmPage = prefix_shop + '/seller/order/setAutoConfirm'
SetOrderAutoCancelPage = prefix_shop + '/seller/order/setAutoCancel'

# Auction
AddAuctionGoodPage = prefix_auction + '/seller/product.html'
AuctionNotBeginPage = prefix_auction + '/seller/product_list.html#notbid'
AuctionDetailPage = prefix_auction + '/' + Config.auctionId
AuctionFavPage = prefix_auction + '/buyer/favorite_manage.html'

# MSite
MAuctionDetailPage = prefix_m_auction + '/' + Config.auctionId
FavMProdPage = prefix_m_default + '/m/#/user/personal-favorites-goods/'
FavMShopPage = prefix_m_default + '/m/#/user/personal-favorites-shop/'
FavMAuctionPage = prefix_m_auction + '/Index/mobile#/bidding-collections/1?collections'
MChangePwdPage = prefix_m_default + '/m/#/user/account-loginpass'
MReceiveAddressPage = prefix_m_default + '/m/#/user/personal-address'
MCartPage = prefix_m_default + '/m/#/shop/cart/list'
MBuyerEvalOrderPage = prefix_m_shop + '/index/mobile/#/buyer/orderlist/1?status=buyerReviewed'
MSellerEvalOrderPage = prefix_m_shop + '/index/mobile/#/seller/orderlist/1?status=sellerReviewed'
MBuyerEvalTradePage = prefix_m_auction + '/Index/mobile#/tradelist/1?status=buyerReviewed'
MReceivedBookOrderPage = prefix_m_default + '/m/#/shop/buyer/orderlist/1?status=ShippedToReceipt'
MSendBookOrderPage = prefix_m_shop + '/index/mobile/#/seller/orderlist/1?status=PaidToShip'
MReceivedAuctionTradePage = prefix_m_auction + '/Index/mobile#/tradelist/1?status=ShippedToReceipt'
MBuyerPayOrderPage = prefix_m_shop + '/index/mobile/#/buyer/orderlist/1?status=ConfirmedToPay'
MBuyerPayTradePage = prefix_m_auction + '/Index/mobile#/tradelist/1?status=ConfirmedToPay'
MCashAccountPage = prefix_m_pay + '/#/account-fundcard'
MCashBackPage = prefix_m_pay + '/#/cash/0/0'
MTransferPage = prefix_m_pay + '/#/transfer'
