

class HTMLNode():
    def __init__(self, tag = None, value=None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output_str = ""
        if self.props == None:
            return ""
        for prop in self.props:
            output_str+= f" {prop}=\"{self.props[prop]}\""

        return output_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag,value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value Not Assigned to Node")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag Not Assigned to Node")
        if type(self.children) == None:
            raise ValueError ("Value Not Assigned to Node")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"