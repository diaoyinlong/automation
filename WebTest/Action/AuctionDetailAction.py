import time

from Module import Uri, Config
from WebTest.Action.BaseAction import BaseAction
from WebTest.Page.AuctionDetailPage import AuctionDetailPage


class AuctionDetailAction(BaseAction):
    def __init__(self):
        self.auctionDetailPage = AuctionDetailPage()
        BaseAction.__init__(self, self.auctionDetailPage)

    # 进行常规竞价
    def bid_to_buy(self):
        with open(Config.rootPath + '/Resource/auction_goods_id.txt', 'r', encoding='utf-8') as f:
            item_id = f.readline()
        self.auctionDetailPage.go_to(Uri.prefix_auction + '/' + item_id)
        self.auctionDetailPage.normal_bid_rdo.click()
        self.auctionDetailPage.bid_to_buy_btn.click()

    # 进行批量购买
    def batch_bid_to_buy(self):
        with open(Config.rootPath + '/Resource/auction_goods_id.txt', 'r', encoding='utf-8') as f:
            items_ids = f.readlines()

        for item_id in items_ids:
            self.auctionDetailPage.go_to(Uri.prefix_auction + '/' + item_id)
            self.auctionDetailPage.bid_to_buy_btn.click()
            self.auctionDetailPage.wait_until_clickable(self.auctionDetailPage.bid_success_msg_css)

    # 设置代理竞价
    def set_agent_to_bid(self):
        with open(Config.rootPath + '/Resource/auction_goods_id.txt', 'r', encoding='utf-8') as f:
            item_id = f.readline()
        self.auctionDetailPage.go_to(Uri.prefix_auction + '/' + item_id)
        self.auctionDetailPage.agent_bid_rdo.click()
        self.auctionDetailPage.set_agent_bid_btn.click()

    # 清空收藏的拍卖
    def clean_up_auction_fav(self):
        self.auctionDetailPage.go_to(Uri.AuctionFavPage)
        time.sleep(1)
        if self.auctionDetailPage.first_fav_auction_row.text != '暂无数据':
            self.auctionDetailPage.check_all_chk.click()
            self.auctionDetailPage.batch_delete_fav_btn.click()
            time.sleep(1)
            self.auctionDetailPage.batch_delete_fav_confirm.click()

    # 将拍品添加到收藏夹
    def add_auction_to_fav(self):
        with open(Config.rootPath + '/Resource/auction_goods_id.txt', 'r', encoding='utf-8') as f:
            item_id = f.readline()
        self.auctionDetailPage.go_to(Uri.prefix_auction + '/' + item_id)
        self.auctionDetailPage.add_to_fav_btn.click()

    # 获取成功加入收藏夹文本
    def get_add_fav_success_txt(self):
        self.auctionDetailPage.wait_until_clickable(self.auctionDetailPage.confirm_btn_css)
        return self.auctionDetailPage.add_to_fav_success_txt

    # 获取成功信息
    def get_bid_success_txt(self):
        self.auctionDetailPage.wait_until_clickable(self.auctionDetailPage.bid_success_msg_css)
        return self.auctionDetailPage.bid_success_msg_txt

    # 获取头部提示条信息
    def get_top_bar_msg(self):
        self.auctionDetailPage.wait_until_clickable(self.auctionDetailPage.msg_bar_css)
        return self.auctionDetailPage.msg_bar.text

    # 是否存在拍品
    def has_auction_in_fav(self):
        self.auctionDetailPage.go_to(Uri.AuctionFavPage)
        time.sleep(1)
        fav_id = self.auctionDetailPage.first_fav_auction_row.get_attribute('data-favid')

        if fav_id is not None and fav_id != '':
            return True
        else:
            return False
