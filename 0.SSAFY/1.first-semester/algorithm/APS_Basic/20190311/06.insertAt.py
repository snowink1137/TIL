from LinkedList import List, Node

# ------------------------------------------------

mylist = List()
mylist.insertfirst(1)
mylist.insertfirst(2)
mylist.insertfirst(3)
mylist.insertfirst(4)
mylist.insertfirst(5)
mylist.printlist()

mylist.insertAt(2, 100)
mylist.insertAt(4, 200)
mylist.printlist()

mylist.insertAt(3, -1)
mylist.printlist()

mylist.deleteAt(3)
mylist.deleteAt(0)
mylist.deleteAt(1)
mylist.printlist()

mylist.deleteAt(0)
mylist.deleteAt(0)
mylist.deleteAt(0)
mylist.deleteAt(0)
mylist.printlist()

mylist.deleteAt(0)
mylist.printlist()

mylist.deleteAt(0)
mylist.printlist()