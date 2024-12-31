



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
		if isinstance(self.props, dict):
			for currentKey in self.props.keys():
				returnList.append(f" {currentKey}={self.props[currentKey]}")
			return "".join(returnList)
	def __repr__(self):
		return (f" tag=", self.tag, " value=", self.value," children=", self.children,
		" props=",self.props
		)
class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None, children=None):
		super().__init__(tag, value,children, props)

	def to_html(self):
		#Starting an empty compliationList to append to later
		compliationList = []
		#Making sure the value isn't None or an empty string
		if self.value == None or self.value == "":
			raise ValueError("All leaf nodes need a value")
		#Returning plain text if the tag is empty or a NoneType
		if self.tag == None or self.tag == "":
			return self.value
		#Checking to see if the tag is a string, otherwise it will ignore it
		if isinstance(self.tag, str):
			#Making sure props is both a dictionary, and not empty
			if isinstance(self.props, dict) and self.props != {}:
				#Iterating through the keys in the props dictionary and appending
				#them to the previously established compliationList to be
				#joined later
				for currentKey in self.props.keys():
					compliationList.append(f'{currentKey}="{self.props[currentKey]}"')
				#Joining the compliationList under a newly established newString variable
				newString = " ".join(compliationList)
				#If this isinstance was entered, returning this value
				return (f"<{self.tag} {newString}>{self.value}</{self.tag}>")
			#Else if the isinstance was skipped, returning just tag wrapping string
			return f"<{self.tag}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag=tag, value=None, children=children, props=props)
		
	def to_html(self):
		appendingList = []
		print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) ONE")
		if isinstance(self, ParentNode):
			print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) TWO")
			if not isinstance(self.tag, str):
				raise ValueError("Tags must be a string")
			if not self.tag or self.tag == '' or self.tag.strip() == '':
				raise ValueError("A tag is required for parent nodes")
			print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) THREE")
			for currentChild in self.children:
				if  currentChild.children:
					appendingList.append(ParentNode.to_html(currentChild))
					print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) THREE - 1")
				else:
					appendingList.append(ParentNode.to_html(currentChild))
					print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) THREE - 2")
		if isinstance(self, LeafNode):
			print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) FOUR")
		#Starting an empty compliationList to append to later
			compliationList = []
			#Making sure the value isn't None or an empty string
			if self.value == None or self.value == "":
				raise ValueError("All leaf nodes need a value")
			#Returning plain text if the tag is empty or a NoneType
			if self.tag == None or self.tag == "":
				print ("RETURNING VALUE AS IT HAD NO TAG")
				return self.value
			#Checking to see if the tag is a string, otherwise it will ignore it
			if isinstance(self.tag, str):
				print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) FIVE")
				#Making sure props is both a dictionary, and not empty
				if isinstance(self.props, dict) and self.props != {}:
					#Iterating through the keys in the props dictionary and appending
					#them to the previously established compliationList to be
					#joined later
					print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) SIX")
					for currentKey in self.props.keys():
						compliationList.append(f'{currentKey}="{self.props[currentKey]}"')
					#Joining the compliationList under a newly established newString variable
					print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) SEVEN")
					newString = "".join(compliationList)
					#If this isinstance was entered, returning this value
					return (f"<{self.tag} {newString}>{self.value}</{self.tag}>")
				#Else if the isinstance was skipped, returning just tag wrapping string
				print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) EIGHT")
				return f"<{self.tag}>{self.value}</{self.tag}>"			
		newList = []
		print(f"ParentNode initialized: props={self.props} (type: {type(self.props)}) NINE")
		if self.props and self.props != {} and not isinstance(self.props,str):
			print("NINE-1")
			for currentKey in self.props.keys():
				newList.append(f'{currentKey}="{self.props[currentKey]}"')
				newStringTwo = "".join(newList)
			return (f"<{self.tag} {newStringTwo}>{self.value}</{self.tag}>")
		elif (self.props):
			print("NINE-2")
			appendingList = "".join(appendingList)
			return (f"<{self.tag}>{appendingList}</{self.tag}>")