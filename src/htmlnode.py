class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
#every data member should be optional and default to None:

#An HTMLNode without a tag will just render as raw text
#An HTMLNode without a value will be assumed to have children
#An HTMLNode without children will be assumed to have a value
#An HTMLNode without props simply won't have any attributes

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            result = ""
            for key, value in self.props.items():
                result += f" {key}=\"{value}\""
            return result

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        elif self.children is None:
            raise ValueError("invalid HTML: no children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"