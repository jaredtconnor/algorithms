# Hi, here's your problem today. This problem was recently asked by Amazon:
# 
# Given a sorted linked list of integers, remove all the duplicate elements in the linked list 
# so that all elements in the linked list are unique.
# 
# Here's an example and some starter code: 

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"

def remove_dup(lst):

    current = lst
    
    if current is None: 
        return

    while current.next is not None: 

        if current.value == current.next.value: 
            temp = current.next.next
            current.next = None
            current.next = temp
        else: 
            current = current.next


lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
