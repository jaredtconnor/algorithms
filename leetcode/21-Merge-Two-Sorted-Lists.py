
# Definition of singly linked list
class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val
        self.next = next


def printList(node: ListNode): 
    while node is not None: 
        print(str(node.val), end = " ") 
        node = node.next
 
    print()

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode: 
        
        # Create the start of the new list 
        head = ListNode() 
        current = head
        
        # Iterate over the lists and zipper or push the highest value into the list
        while list1 and list2: 

            if list1.val < list2.val: 
                current.next = list1
                list1 = list1.next
            
            else: 
                current.next = list2
                list2 = list2.next 

            current = current.next 

        if list1: 
            current.next = list1

        elif list2: 
            current.next = list2

        return head.next

if __name__ == '__main__':  

    solution = Solution()

    head1 = ListNode(1) 
    head1.next = ListNode(2) 
    head1.next.next = ListNode(4)

    head2 = ListNode(1)  
    head2.next = ListNode(3) 
    head2.next.next = ListNode(4) 
    
    printList(solution.mergeTwoLists(head1, head2))

