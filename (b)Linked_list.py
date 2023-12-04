#Explanation:
#To find the kth to the last element of a linked list, we can use the following algorithm:

#Initialize two pointers p1 and p2 to the head of the linked list.
#Move the p1 pointer k nodes ahead.
#Move both p1 and p2 pointers one node at a time until p1 reaches the end of the linked list.
#The node pointed to by p2 is the kth to the last node.

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def kth_to_last_node(self, k):
        if k <= 0:
            print("Invalid value for k")
            return

        p1 = p2 = self.head

        # Move p1 k nodes ahead
        for _ in range(k):
            if p1 is None:
                print("k is greater than the length of LinkedList")
                return
            p1 = p1.next

        # Move both pointers until p1 reaches the end
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        if p2 is not None:
            print("Kth to the last element is:", p2.data)

# Driver's Code
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)

    # Function call
    llist.kth_to_last_node(4)
