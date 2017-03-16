from WebTest.Action.SearchAction import SearchAction
import unittest


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.action = SearchAction()

    def tearDown(self):
        self.action.searchPage.quit()

    def testSearchSmoke(self):
        """
        对图书和拍品搜索冒烟测试
        :return:
        """
        # 搜索图书
        self.action.search('book', '小说')

        # 验证搜索结果
        self.assertIn('小说', self.action.get_first_search_result('book'))

        # 搜索拍品
        self.action.search('auction', '旧书')

        # 验证搜索结果
        self.assertIn('旧书', self.action.get_first_search_result('auction'))
