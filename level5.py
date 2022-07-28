class Node:
    def __init__(self, value):
        self.left = None
        self.top = None
        self.bottom = None
        self.right = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def flatten(self):
        current = self.head
        values = []

        while current is not None:
            values.append(current.value)

            #CHECK NODE COLUMN (TOP)
            top = current.top

            while top is not None:
                values.append(top.value)
                top = top.top

            #CHECK NODE COLUMN (BOTTOM)
            bottom = current.bottom

            while bottom is not None:
                values.append(bottom.value)

                #CHECKING LEFT AND RIGHT SIDES OF NODE
                left = bottom.left

                while left is not None:
                    values.append(left.value)
                    left = left.left

                right = bottom.right

                while right is not None:
                    values.append(right.value)
                    right = right.right

                bottom = bottom.bottom

            #MOVING TO NODE IN THE RIGHT
            current = current.right

        #FLATTENED
        print("Flattened Linked List:")
        for x in values:
            print(x)

        #SORTING
        print("\n\nSorted Flattened Linked List:")
        values.sort()
        for x in values:
            print(x)


node1 = Node(10)
node2 = Node(1)
node3 = Node(8)
node4 = Node(6)
node5 = Node(2)
node6 = Node(3)
node7 = Node(7)
node8 = Node(4)
node9 = Node(5)
node10 = Node(9)

#SETTING RIGHT VALUES
node1.right = node2
node2.right = node6
node6.right = node10
node8.right = node9

#SETTING BOTTOM VALUES
node2.bottom = node3
node3.bottom = node4

node6.bottom = node8

#SETTING LEFT VALUES
node4.left = node5

#SETTING TOP VALUES
node6.top = node7


#INITIALIZING LINKED LIST
linkedlist = LinkedList()
linkedlist.head = node1
linkedlist.flatten()