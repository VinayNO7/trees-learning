# class Node:
#     def __init__(self,data=0,left=None,right=None):
#         self.data = data
#         self.left = left
#         self.right = right

# def preorder(root):
#     if root:
#         print(root.data, end=" ")
#         preorder(root.left)
#         preorder(root.right)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data,end=" ")
#         inorder(root.right)

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data,end=" ")

# root = Node(1)
# root.left = Node(3)
# root.right = Node(5)
# root.left.left = Node(2)
# root.left.right = Node(4)
# root.right.right = Node(8)

# preorder(root)
# print("\n")
# inorder(root)
# print("\n")
# postorder(root)

#BINARY SEARCH TREE
class Node:
    def __init__(self,data=0):
        self.data = data
        self.left = None
        self.right = None

def insertNode(root,data):
    if not root:
        return Node(data)
    if root.data == data:
        return root
    if root.data > data:
        root.left = insertNode(root.left, data)
    else:
        root.right = insertNode(root.right, data)
    
    return root

def search(root,data):
    if not root:
        print("Element not found!.",end="\n")
        return
    if root.data == data:
        print("Element found.",end="\n")
        return
    if root.data > data:
        search(root.left, data)
    else:
        search(root.right, data)
    
    return root

def delete(root,data):
    if not root:
        return root
    if root.data > data:
        root.left = delete(root.left,data)
    elif root.data < data:
        root.right = delete(root.right,data)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right,succ.data)
    return root

def get_successor(root):
    root = root.right
    while root and root.left :
        root = root.left

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

root = insertNode(None,20)
root = insertNode(root,30)
root = insertNode(root,40)
root = insertNode(root,12)
root = insertNode(root,18)
root = insertNode(root,25)
root = insertNode(root,50)
root = insertNode(root,15)

inorder(root)
delete(root,40)
print("\n")
inorder(root)
