class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def insert_begin(self, data: int) -> None:
        temp = Node(data)
        if self.head:
            temp.next = self.head
            self.head = temp
        else:
            self.head = temp
            self.tail = temp
        self.count += 1

    def insert_end(self, data: int) -> None:
        temp = Node(data)
        if self.head:
            self.tail.next = temp
            self.tail = temp
        else:
            self.head = temp
            self.tail = temp
        self.count += 1

    def insert_pos(self, data: int, pos: int) -> None:
        if pos < 1 or pos > self.count + 1:
            print("Given position is invalid.")
        elif pos == 1:
            self.insert_begin(data)
        elif pos == self.count + 1:
            self.insert_end(data)
        else:
            i = 2
            temp = Node(data)
            temp1 = self.head
            while i < pos:
                temp1 = temp1.next
                i += 1
            temp.next = temp1.next
            temp1.next = temp
            self.count += 1

    def delete_begin(self) -> None:
        if self.head == None:
            print("Underflow")
        elif self.head.next == None:
            print("Deleted", self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            print("Deleted", self.head.data)
            self.head = self.head.next
            self.count -= 1

    def delete_end(self) -> None:
        if self.head == None:
            print("Underflow")
        elif self.head.next == None:
            print("Deleted", self.head.data)
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            print("Deleted", self.tail.data)
            temp.next = None
            self.tail = temp
            self.count -= 1

    def delete_pos(self, pos: int) -> None:
        if pos < 1 or pos > self.count:
            print("Given position is invalid.")
        elif pos == 1:
            self.delete_begin()
        elif pos == self.count:
            self.delete_end()
        else:
            i = 2
            temp = self.head
            while i < pos:
                temp = temp.next
                i += 1
            print("Deleted", temp.next.data)
            temp.next = temp.next.next
            self.count -= 1

    def display(self) -> None:
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            print("The elements are:")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def search(self, ele: int) -> None:
        temp = self.head
        f = False
        i = 1
        while temp:
            if temp.data == ele:
                f = True
                break
            i += 1
            temp = temp.next
        if f:
            print("The element is present at index", i)
        else:
            print("The element is not present in the list.")
            
    def reverse(self) -> None:
        if self.head == None:
            print("List is empty")
            return
        prev = None
        curr = self.head
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        self.head, self.tail = self.tail, self.head
        print("List reversed successfully.")
        
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_begin(5)
    sll.insert_pos(15, 3)
    sll.display()
    sll.reverse()
    sll.display()
    sll.delete_begin()
    sll.display()
    sll.delete_end()
    sll.display()
    sll.delete_pos(2)
    sll.display()
    sll.search(15)
    sll.display()