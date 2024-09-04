# free code camp implementation
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
#  
#     a
#    / \
#   b   c
#  / \   \
# d   e   f

# Iterative approach
def depthFirstValues(root):
  
  if root == None: 
    return []
  
  result = []
  stack = [root]

  while(len(stack) > 0):
    current = stack.pop()
    result.append(current.data)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)  

  return result
# test 1 (populated tree)
# print(depthFirstValues(a))

# test 2 (empty tree)
# print(depthFirstValues(None))

def depthFirstValuesRecursive(root):
  if root == None:
    return []
  
  leftValues = depthFirstValuesRecursive(root.left) # returns [b,d,e]
  rightValues = depthFirstValuesRecursive(root.right) # returns [c,f]

  return [root.data, *leftValues, *rightValues]

# test 1 (populated tree)
print(depthFirstValuesRecursive(a))

# test 2 (empty tree)
print(depthFirstValuesRecursive(None))


