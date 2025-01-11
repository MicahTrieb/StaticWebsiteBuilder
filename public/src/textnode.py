from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode
class TextType(Enum):
	NORMAL = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINKS = "links"
	IMAGES = "images"

class TextNode:
	def get_text_type(text_type):
		match (text_type):
			case (TextType.NORMAL):
				return "NORMAL"
			case TextType.BOLD:
				return "BOLD"
			case TextType.ITALIC:
				return "ITALIC"
			case TextType.CODE:
				return "CODE"
			case TextType.LINKS:
				return "LINKS"
			case TextType.IMAGES:
				return "IMAGES"
			case _:
				raise Exception("Invalid Text Type")
	def __init__(self, text, text_type, url=""):
		self.text = text
		self.url = url
		self.text_type = text_type
	def __eq__(self, checkTestNode):
		if checkTestNode.text == self.text and checkTestNode.text_type == self.text_type and checkTestNode.url == self.url:
			return True
	def __repr__(self):
		return(f"TextNode({self.text}, {self.text_type}, {self.url})")
	def text_node_to_html_node(self):
		match (self.text_type):
			case TextType.NORMAL:
				return LeafNode(tag=None,value=self.text)
			case TextType.BOLD:
				return LeafNode(tag="b",value=self.text)
			case TextType.ITALIC:
				return LeafNode(tag="i",value=self.text)
			case TextType.CODE:
				return LeafNode(tag="code",value=self.text)
			case TextType.LINKS:
				if self.url == "" or self.url.strip() == "":
					raise TypeError("Links need a URL")
				return LeafNode(tag="a",value=self.text, props={"href":self.url})
			case TextType.IMAGES:
				if self.url == "":
					raise TypeError("Images need an image link")
				return LeafNode(tag="img",value="",props={"src":self.url,"alt":self.text})
			case _:
				raise Exception("Invalid Text Type")