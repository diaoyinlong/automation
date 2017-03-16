import os
from Public.XmlParser import XmlParser

rootPath = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
xmlObject = XmlParser(rootPath + '/Config.xml')
env = xmlObject.get_text_value('env')
browser = xmlObject.get_text_value('browser')
auctionId = xmlObject.get_text_value('auctionId')
tradeId = xmlObject.get_text_value('tradeId')
emulateMobile = xmlObject.get_text_value('emulateMobile')
log = xmlObject.get_text_value('log')
