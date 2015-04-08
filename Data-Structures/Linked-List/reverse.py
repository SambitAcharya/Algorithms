'''

Python program to reverse a linked list

'''

class Node:
  def __init__(self,val,nxt):
    self.val = val
    self.nxt = nxt
 
def prnt(n):
  nxt = n.nxt
  print n.val
  if(nxt is not None):
    prnt(nxt)

#Iterative
def reverse(n):
  last = None
  current = n
 
  while(current is not None):
    nxt = current.nxt
    current.nxt = last 
    last = current
    current = nxt
    
#Recursive
def recurse(n,last):
  if n is None:
    return last
  nxt = n.nxt
  n.nxt = last
  return reverse(nxt, n)

 
  return last
