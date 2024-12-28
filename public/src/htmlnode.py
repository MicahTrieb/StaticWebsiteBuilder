



class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_html(self):
		raise NotImplementedError
	def props_to_html(self):
		returnList = []
		for currentKey in self.props.keys():
			returnList.append(f" {currentKey}={self.props[currentKey]}")
		return "".join(returnList)
	def __repr__(self):
		return (f" tag=", self.tag, " value=", self.value," children=", self.children,
		" props=",self.props
		)
class LeafNode:
	def __init__(self):
		super().__init__(self, tag=None, value=None, props=None)
