from xml.etree import ElementTree


class XmlParser:
    def __init__(self, path):
        self.path = path
        self.tree = ElementTree.parse(path)
        self.root = self.tree.getroot()

    def get_text_value(self, element):
        return self.root.find(element).text

    def get_attribute_value(self, element, key):
        return self.root.find(element).get(key)

    def set_attribute_value(self, element, key, value):
        self.root.find(element).set(key, value)
        self.tree.write(self.path)
