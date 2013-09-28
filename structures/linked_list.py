class LinkNode(object):
    def __init__(self,key,nextnode):
        self.key = key
        self.nextnode = nextnode


class LinkedList(object):
    """ Class for a singly linked list """

    def __init__(self):
        self.data = []
        self.firstNode = None
        self.freeList = []
        self.numNodes = 0

    def addAfter(self,key,target):
        """ Adds a new node after the one at position target"""
        if self.firstNode is None:
            self.data.append(LinkNode(key,None))
            self.firstNode = 0
        else:
            t_nextnode = self.data[target].nextnode
            if not len(self.freeList):
                #If there are no gaps in the list, append:
                self.data.append(LinkNode(key,t_nextnode))
                new_indx = len(self.data)-1
            else:
                #Else, pop a gap off the list of empty cells
                #and populate it:
                new_indx = self.freeList.pop()
                self.data[new_indx] = LinkNode(key,t_nextnode)
            self.data[target].nextnode = new_indx
        self.numNodes += 1

    def delAfter(self,target):
        """ Deletes the node after the one at position target
        and decrements all keys for nodes at higher positions """

        removed_node = self.data[target].nextnode

        #Freelist contains a list of gaps in the linked list:
        self.freeList.append(removed_node)

        nextnextnode = self.data[removed_node].nextnode
        self.data[target].nextnode = nextnextnode
        self.numNodes -= 1


    def __iter__(self):
        self.indx = self.firstNode
        return self

    def next(self):
        while self.indx is not None:
            use_indx = self.indx
            self.indx = self.data[self.indx].nextnode
            return (self.data[use_indx].key,use_indx,self.data[use_indx].nextnode)
        raise StopIteration

    def __str__(self):
        outstr = "Length of linked list is "+str(self.numNodes)+"\n"
        outstr += "First ele linked list is "+str(self.firstNode)
        return outstr 

l = LinkedList()
l.addAfter(1,0)
l.addAfter(2,0)
l.addAfter(3,0)
l.addAfter(4,0)
l.addAfter(7,2)
l.addAfter(5,0)
l.addAfter(6,3)

print l
for i,el in enumerate(l):
    print i,el

l.delAfter(4)
print "-------------"

print l
for i,el in enumerate(l):
    print i,el
print l.freeList


l.addAfter(3,3)

print l
for i,el in enumerate(l):
    print i,el
print l.freeList
