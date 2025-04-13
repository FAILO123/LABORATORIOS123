# LABORATORIOS123
#PROBLEMA 1
def reverse_string(s):
    stack = []
   
    for char in s:
        stack.append(char)


    reversed_str = ''
    while stack:
        reversed_str += stack.pop()


    return reversed_str


input_string = input( "text here : ")
reversed_string = reverse_string(input_string)
print("text original:", input_string)
print("text invertid:", reversed_string)



#PROBLEMA 2



def precedence(op):
    """Return operator precedence."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    """Convert infix expression to postfix using Shunting Yard algorithm."""
    output = []
    stack = []


    tokens = expression.split()
   
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while stack and precedence(token) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(token)
   
    while stack:
        output.append(stack.pop())
   
    return output


def evaluate_postfix(postfix_tokens):
    """Evaluate postfix expression using a stack."""
    stack = []


    for token in postfix_tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()


            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b


            stack.append(result)
   
    return stack[0]


def evaluate_infix(expression):
    """Evaluate an infix expression by converting it to postfix first."""
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


# Test
if __name__ == "__main__":
    expr = "( 3 + 4 ) * 2"
    result = evaluate_infix(expr)
    print(f"Infix expression: {expr}")
    print(f"Result: {result}")





#PROBLEMA 3

class Node:
    """Node class for the Linked List Stack."""
   
    def __init__(self, data=None):
        """Initialize node with data and next reference."""
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using a linked list."""
   
    def __init__(self):
        """Initialize empty stack using linked list."""
        self.head = None  
        self.count = 0
        self.min_stack = []  
   
    def is_empty(self):
        """Check if stack is empty."""
        return self.head is None
   
    def push(self, item):
        """Add item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
       
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
   
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
       
        item = self.head.data
        self.head = self.head.next
        self.count -= 1
       
        if item == self.min_stack[-1]:
            self.min_stack.pop()
       
        return item
   
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
       
        return self.head.data
   
    def size(self):
        """Return the number of items in the stack."""
        return self.count
   
    def get_min(self):
        """Return the minimum value in the stack."""
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]
   
    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"
       
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
           
        return f"Stack: [{', '.join(items)}]"




stack = LinkedListStack()
   
stack.push(20)
stack.push(10)
stack.push(5)
stack.push(15)
print(stack)
print("Stack min: "+str(stack.min_stack))


stack.pop()
print("Minimum value after pop:", stack.get_min())     
stack.pop()
print("Minimum value after making another pop:", stack.get_min())  






#PROBLEMA 4 
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []


    def type(self, new_text):
        self.history.append(self.text)
        self.text += new_text
        print(f"Texto actual: '{self.text}'")


    def delete(self, count):
        self.history.append(self.text)
        self.text = self.text[:-count]
        print(f"Texto actual después de borrar: '{self.text}'")


    def undo(self):
        if self.history:
            self.text = self.history.pop()
            print(f"Deshacer realizado. Texto actual: '{self.text}'")
        else:
            print("No hay acciones para deshacer.")


    def get_text(self):
        return self.text




if __name__ == "__main__":
    editor = TextEditor()
   
    editor.type("QUE VA")
    editor.type(" PERU")
    editor.delete(6)
    editor.undo()
    editor.undo()
    editor.undo()








#PROBLEMA 5 

import re

def is_balanced_html(html):
     # Regex to find tags (opening or closing)
    tag_pattern = re.compile(r'</?([a-zA-Z][a-zA-Z0-9])[^>]>')
    
    stack = []
    
    for match in tag_pattern.finditer(html):
        tag = match.group()
        tag_name = match.group(1)

        if tag.startswith('</'):
            # It's a closing tag
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        else:
            # It's an opening tag
            stack.append(tag_name)

    return not stack  

# Examples
test_cases = {
    "Example 1 (Correct)": "<html><body><h1>Hello</h1></body></html>",
    "Example 2 (Incorrect nesting)": "<div><span>Text</div></span>",
    "Example 3 (Missing closing tag)": "<ul><li>Item 1<li>Item 2</ul>",
    "Example 4 (Extra closing tag)": "<p>Paragraph</p></p>",
    "Example 5 (Empty string)": "",
    "Example 6 (Plain text, no tags)": "Just some plain text",
    "Example 7 (Proper nested tags)": "<div><p><strong>Bold</strong></p></div>",
    "Example 8 (Wrong order nesting)": "<div><p>Text</div></p>",
    "Example 9 (Tags with attributes)": '<a href="#">Link</a>',
    "Example 10 (Self-closing tags - not handled here)": "<br><hr>",
}

for description, html in test_cases.items():
    result = is_balanced_html(html)
    print(f"{description}: {'Balanced HTML Tags' if result else 'Unbalanced HTML tags'}")



  
#PROBLEMA 6 
