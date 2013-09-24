from node import TreeNode

# In addition to a key and satellite data, each node contains
# attributes left, right, and p that point to the nodes
# corresponding to its left child

# The keys in a binary search tree are always stored in such a
# way as to satisfy the binary-search-tree property:
# Let x be a node in a binary search tree. If y is a node in
# the left subtree of x, then y:key <= x:key. If y is a node
# in the right subtree of x, then y:key >= x:key.
class Tree:
   
   def __init__(self):
       self.nodelist = []
       self.index = 0
       self.numNodes = 0

   def __getChild(self,parent_index,key):
       """ Given an index and a key, return a Boolean stating
       whether the key is to the Left, and the index of the node
       to the left"""
       if key <= self.nodelist[parent_index].key:
           #I fit in the left.
           return True, self.nodelist[parent_index].Left
       else:
           return False, self.nodelist[parent_index].Right

   def addNode(self,key):

       if not self.numNodes:
           #We are adding the base node:
           parent_index = False
       else:
           #We need to insert a node, begin walking from the root:
           parent_index = 0
           LeftBranch, BranchVal = self.__getChild(parent_index,key)
           while BranchVal:
               if LeftBranch:
                   parent_index = self.nodelist[parent_index].Left
               else:
                   parent_index = self.nodelist[parent_index].Right
               LeftBranch, BranchVal = self.__getChild(parent_index,key)

       n = TreeNode(parent_index,False,False,key)
       self.nodelist.append(n)

       #Update my parent to point at new child (unless I am the root):
       if self.numNodes:
           if key <= self.nodelist[parent_index].key:
               self.nodelist[parent_index].Left = self.numNodes
           else:
               self.nodelist[parent_index].Right = self.numNodes

       self.numNodes += 1

   def treeMax(self,start=0):
       """ return the maximum key, starting from the node at offset
       start """
       indx = start
       max_val = self.nodelist[indx].key
       while self.nodelist[indx].Right:
           indx = self.nodelist[indx].Right
           if indx:
               max_val = self.nodelist[indx].key
       return max_val

   def treeMin(self,start=0):
       """ return the minimum key, starting from the node at offset
       start """
       indx = start
       min_val = self.nodelist[indx].key
       while self.nodelist[indx].Left:
           indx = self.nodelist[indx].Left
           if indx:
               min_val = self.nodelist[indx].key
       return min_val

   def treeWalkInorder(self,indx=0):
       """ Walk the tree in order and print the results """

       if self.nodelist[indx].Left:
           self.treeWalkInorder(self.nodelist[indx].Left)
       print self.nodelist[indx].key
       if self.nodelist[indx].Right:
           self.treeWalkInorder(self.nodelist[indx].Right)

   def treeSearch(self,k,indx=0):
       """Walk the tree to find if it contains a given value"""

       #Trivial, value is in root node:
       if (self.nodelist[indx].key == k):
           return indx
       LeftBranch, BranchVal = self.__getChild(indx,k)
       while BranchVal:
           if LeftBranch:
               indx = self.nodelist[indx].Left
           else:
               indx = self.nodelist[indx].Right

           if (k == self.nodelist[indx].key):
               return indx

           LeftBranch, BranchVal = self.__getChild(indx,k)

       return None

   #__iter__ has to return an object with a next method
   def __iter__(self):
        return self

   def next(self):
       if self.index == self.numNodes:
           raise StopIteration
       self.index += 1
       return self.nodelist[self.index-1]

   def checkRep(self):
       """ Various assertions to check that the state of the
       tree is valid """

       assert len(self.nodelist) == self.numNodes

       for i,n in enumerate(self.nodelist):
           #Check that the nodes to your left and right
           #have you as the parent and that the fundamental
           #property of trees holds:
           if self.nodelist[i].Left:
               assert self.nodelist[n.Left].Parent == i
               assert self.nodelist[i].key >= self.nodelist[n.Left].key
           if self.nodelist[i].Right:
               assert self.nodelist[n.Right].Parent == i
               assert self.nodelist[i].key <= self.nodelist[n.Right].key

           print self.treeSearch(self.nodelist[i].key),i,self.nodelist[i].key


t = Tree()
t.addNode(4)
t.checkRep()
t.addNode(7)
t.checkRep()
t.addNode(6)
t.addNode(1)
t.addNode(-1)
t.addNode(22)
t.addNode(4)
t.checkRep()

print "Tree max = ",t.treeMax()
print "Tree min = ",t.treeMin()
print "key -2 is in node ",t.treeSearch(-2)
print "key 22 is in node ",t.treeSearch(22)




#for node in t:
#    print "------------------"
#    print "key = ",node.key
#    print "left, right = ",node.Left,node.Right
#    print "parent = ",node.Parent
