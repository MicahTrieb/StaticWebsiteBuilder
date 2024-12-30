



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
class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, props,children=None)

	def to_html(self):
		if not isinstance(self.value, None):
			if not self.tag or self.tag == "":
				return self.value
			if isinstance(self.tag, str):
				return f"<{self.tag}>{self.value}</{self.tag}>"
			if isinstance(self.tag, dict):
				
				pass
			
		raise ValueError("All leaf nodes need a value")
			
