'''A queue is similar to Stacks , the way of adding and removing element is different.

The elements are added from end called Rear end and deleted from end called Front end.

Elements are basically added from last index and removed from first index.

Follows the behavior of FIFO( first in first out).

Process of adding new element is called Enqueue and
Process of deleting element is called Dequeue'''

class Queue:
    def __init__(self):
        self.items=[] #assigned blank list

#enqueue will add element at the end of the list
    def enqueue(self,item):
        self.items.append(item)
        return self.items

#dequeue will remove the first element of the list
    def dequeue(self):
        self.items.pop(0)
        return self.items

#if list is empty , it prints blank queue else prints the list
    def print_queue(self):
        if self.items == []:
            print("Blank queue")
        else:
            print(self.items)


queue1 = Queue()
queue1.print_queue()
queue1.enqueue(2)
queue1.enqueue(4)
queue1.enqueue(7)
queue1.enqueue(8)
queue1.print_queue()
queue1.dequeue()
queue1.print_queue()
queue1.dequeue()
queue1.print_queue()


#o/p is :
Blank queue
[2, 4, 7, 8]
[4, 7, 8]
[7, 8]