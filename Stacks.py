#User-Defined Data Structures

#Stack is a data structure which adds & remove elements in a particular order.
#Element added goes on top of the stack and to remove , the element on top of the stack can be removed first

#Just like a stack of books

#THis follows LIFO ( last in first out) behaviour.

#Adding new element -- Push
#Removing an element -- Pop

#Lets create a stack then

#We will define 4 methods here , push() , pop(), isempty(),print_stack() under Class Stack

class Stack:
    def __init__(self):
        self.items = [] #the stack is empty now ,self.items shows items

#This method will return an empty stack
    def is_empty(self):
        return self.items==[]

#This method pushes element on top at index 0
    def push(self,item):
        self.items.insert(0,item)

#This method pops element out from index 0
    def pop(self):
        self.items.pop(0)

#This method prints stack
    def print_stack(self):
        if self.items == []:
            print("Empty stack []")
        else:
            print(self.items)

stack1 = Stack()
stack1.print_stack()
stack1.push(2)
stack1.push(5)
stack1.push(6)
stack1.push(8)
stack1.print_stack()
stack1.pop()
stack1.print_stack()

#my o/p is :
# Empty stack []
# [8, 6, 5, 2]
# [6, 5, 2]
#Successfully created a stack now....

