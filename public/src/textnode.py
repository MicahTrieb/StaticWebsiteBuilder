from enum import Enum

class TextType(Enum):
	NORMAL = 'normal'
	BOLD = 'bold'
	ITALIC = 'italic'
	CODE = 'code'
	LINKS = 'links'
	IMAGES = 'images'

class TextNode:
	def __init__(self, text, text_type, url):
		self.text = text
		self.text_type = text_type
		self.url = url
	def __eq__(self, checkTestNode):
		if checkTestNode.text == self.text and checkTestNode.text_type == self.text_type and checkTestNode.url == self.url:
			return True
	def __repr__(self):
		return(f"{self}({self.text}, {self.text_type.value()}, {self.url}"
