#  File: BST_Cipher.py

#  Description: encode and decode a message usinng a binary tree

#  Student Name:Kenneth Bowen

#  Student UT EID:keb2864

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created:4/29/16

#  Date Last Modified:4/23/16

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
    #gives a numerical value to the character for sorting
    if data==' ':
        self.score=0
    else:
        self.score=ord(self.data)
  

class Tree (object):
  def __init__ (self):
    self.root = None
  #runs checkNodes() against another tree
  def isSimilar(self,other):
    return self.checkNodes(self.root,other.root)
  #compares nodes of a tree
  def checkNodes(self,aNode,bNode):  
    if aNode==None or bNode==None:
      return aNode==bNode
    if aNode.data!=bNode.data :
      return False
    
    return self.checkNodes(aNode.lChild,bNode.lChild) and self.checkNodes(aNode.rChild,bNode.rChild)
  #runs level() on the root
  def printLevel(self,lvl):
    self.level(self.root,lvl)
    print()
  #prints each node at a given level
  def level(self,aNode,lvl):
    if lvl==1 and aNode!=None:
      print(aNode.data,end=" ")
      return
    if aNode==None or lvl<1:
      return
    self.level(aNode.lChild,lvl-1)
    self.level(aNode.rChild,lvl-1)
  #returns number of nodes in tree
  def numNodes(self):
    return self.getNum(self.root)
  #counts nodes
  def getNum(self,aNode):
    if aNode==None:
      return 0
    return 1+self.getNum(aNode.rChild)+self.getNum(aNode.lChild)
  #returns longest path length
  def getHeight(self):
    return max(self.getLengths(self.root))
  
  #returns list of path lengths
  def getLengths(self,aNode,length=0,lengths=[]):
    
    if aNode==None:
      lengths.append(length)
    else:
      self.getLengths(aNode.rChild,length+1,lengths)
      self.getLengths(aNode.lChild,length+1,lengths)
    return lengths
  
  # returns a string represting the path to the character
  def search (self, key):
    path=''
    #if key==' ':
      
    #  return '<'*(self.getHeight()-1)
    if key==' ':
      score=0
    else:
      score=ord(key)
    current = self.root
    if current.score ==score:
      return '*'
    while ((current != None) and (current.score != score)):
      if (ord(key) < current.score):
        current = current.lChild
        path+='<'
      else:
        current = current.rChild
        path+='>'
    if current==None:
      path=''
    return path

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)
    score=newNode.score
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        
        if score==current.score:
            break
        elif (score < current.score):
            current = current.lChild
        else:
            current = current.rChild
      if (score < parent.score):
        parent.lChild = newNode
      
      elif score > parent.score:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      inOrder (aNode.lChild)
      print (aNode.data)
      inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print (aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  #follows a string represting a path to return a letter
  def traverse(self,st):
    current=self.root
    if st==current.data:
      return '*'
    for i in st:
      if i=='<':
        current=current.lChild
      else:
        current=current.rChild
    return current.data
  #encrypts a message using the tree
  def encrypt(self,st):
    encrypted=''
    numLett=len(st)
    for i in range(numLett):
   
      encrypted+=self.search(st[i])
      if i!=numLett-1:
        encrypted+='!'
    return encrypted         
  #decrypts a message using a tree
  def decrypt(self,st):
    encrypted=st.split('!')
    decrypted=''
    for i in encrypted:
      decrypted+=self.traverse(i)
    return decrypted
def main():
  #create trees
  bst=Tree()
  data=str(input('Enter encryption key: '))
  for i in data:
    bst.insert(i)
  encrypt=str(input('Enter the string to be encrypted: '))
  print('Encrypted string:',bst.encrypt('encrypt'),'\n')
  decrypt=str(input('Enter the string to be decrypted: '))
  print('Decrypted string:',bst.decrypt('decrypt'))
  
  
    

  
    
  
    

main()        