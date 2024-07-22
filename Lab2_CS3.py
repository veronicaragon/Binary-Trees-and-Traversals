#Problem 1. Given the roots of two binary trees of integers, write a python function to 
#           check if the two trees are the same or not. Note: two trees are the same if they
#           have the same structure and the same values stored at each node.
def isSameTree(t1, t2):
    if t1 is None and t2 is None: # if both trees are empty
        return True
    if t1 is None or t2 is None: # if one of the trees is empty
        return False
    if t1.key != t2.key: # if the values at the nodes are different
        return False
    return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right) # recursive call to check the left and right subtrees


#Problem 2. Given the root of a binary tree, return the zigzag level order traversal of its
#           nodes’ values (i.e., from left to right, then right to left for the next level and
#           alternate between).
def zigzagLevelOrder(root): 
    if not root: # if the tree is empty
        return []
    res, temp, stack, level = [], [], [root], 1 # one stack to store the nodes and one list to store the result
    while stack: # while there are nodes in the stack
        for i in range(len(stack)): 
            node = stack.pop(0) # remove the first node from the stack
            if node: 
                if len(res) < level: # length of the result list is less than the current level
                    res.append([]) # add a new list to the result list
                if level % 2 == 0: # if the level is even
                    res[level-1].insert(0, node.key) # insert the value at the beginning of the list
                else:
                    res[level-1].append(node.key) # insert the value at the end of the list
                stack.append(node.left) # add the left & right child to the stack
                stack.append(node.right) 
        level += 1 
    return res 


#Problem 3. Given an array of integers that are sorted in increasing order,convert it to an AVL tree.
def sortedArrayToAVL(nums):
    if not nums:
        return None
    mid = len(nums) // 2   # Find the middle index of the array
    root = TreeNode(nums[mid])  # Create a new TreeNode with the value at middle index
    root.left = sortedArrayToAVL(nums[:mid])    # build left subtree with elements to the left of middle index
    root.right = sortedArrayToAVL(nums[mid+1:]) # do the same to right of middle index
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))  # Update the height of the current node

    balance = getBalance(root)  # Perform rotation if needed to balance the tree
    if balance > 1 and nums[mid] < root.left.val:    # Left Left Case
        return rightRotate(root)
    if balance < -1 and nums[mid] > root.right.val: # Right Right Case
        return leftRotate(root)
    if balance > 1 and nums[mid] > root.left.val:   # Left Right Case
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and nums[mid] < root.right.val: # Right Left Case
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(z):
    y = z.left
    T2 = y.right

    y.right = z # Perform rotation
    z.left = T2

    z.height = 1 + max(getHeight(z.left), getHeight(z.right)) # Update heights
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

def leftRotate(y):
    x = y.right
    T2 = x.left

    x.left = y # Perform rotation
    y.right = T2

    y.height = 1 + max(getHeight(y.left), getHeight(y.right)) # Update heights
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    return x


#Problem 4. Given a binary tree, determine whether it is (height-)balanced.
def isBalanced(root):
    def check(root):
        if not root:
            return 0    #empty subtree
        left = check(root.left) #calculate the height of the left and right subtrees
        right = check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:  #either subtree is unbalanced or
            return -1                                       #the height difference is more than 1, return -1
        return 1 + max(left, right) #Return the height of the current subtree
    return check(root) != -1    #Check if the overall tree is balanced


#Problem 5. Given an integer n, return the first n rows of Pascal’s triangle.
#           In Pascal’s triangle (see below), each number is the sum of the two
#           numbers directly above.
#           Example:
#           Input: n = 5, Output = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
def pascalsTriangle(numRows):
    res = []    # empty list to store the rows of Pascal's triangle
    for i in range(numRows):
        res.append([1]) # Initialize a new row with the first element always being 1
        for j in range(1, i):   ## Calculate each element by summing the two numbers directly above it in the previous row
            res[i].append(res[i-1][j-1] + res[i-1][j])
        if i != 0:  # Add the last element of the row, which is always 1 (except for the first row)
            res[i].append(1)
    return res



#Challenge. You are given a perfect binary tree, where all leaves are on the same
#           level, and every parent has two children. The binary tree has the following
#           definition:
#           Each node consists of:
#               • A value: int
#               • A node – left: pointer to left child
#               • A node – right: pointer to right child
#               • A node – next: pointer to node immediately to its right, at the same
#                 level (possibly null if this is the right-most node of a level)
#           Initially, all next pointers are set to NULL. Write a program that, given a
#           binary tree with all next pointers set to null, populates each next pointer
#           to point to its next right node.
def challenge(root):
    if not root:
        return root
    leftmost = root # Initialize the leftmost node of the current level
    while leftmost.left:
        head = leftmost  # 'head' is used to traverse the nodes at the current level
        while head: # Traverse the nodes at the current level and set the 'next' pointers
            head.left.next = head.right # Connect the left child's 'next' pointer to the right child
            if head.next:      
                head.right.next = head.next.left
            head = head.next     # Move to the next node in the current level
        leftmost = leftmost.left    # Move to the leftmost node of the next level
    return root


# Testing
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.next = None  # added next pointer for the challenge

# Function to test the given problems
def test_problems():
    # Problem 1
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)

    print("Problem 1 Test \nExpected: True")
    print("Result:  " , isSameTree(t1, t2))

    # Problem 2
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("\nProblem 2 Test \nExpected: [[3], [20, 9], [15, 7]]")
    print("Result:  " , zigzagLevelOrder(root))

    # Problem 3
    def in_order_traversal(root, result):
        if root:
            in_order_traversal(root.left, result)
            result.append(root.key)
            in_order_traversal(root.right, result)
    
    arr = [1, 4, 7, 23, 26, 29, 80, 100, 103, 107]
    result = sortedArrayToAVL(arr)

    print("\nProblem 3 Test \nExpected: [1, 4, 7, 23, 26, 29, 80, 100, 103, 107]")
    result_order = []
    in_order_traversal(result, result_order)
    print("Result:  ", result_order)

    # Problem 4
    unbalanced_tree = TreeNode(1)
    unbalanced_tree.left = TreeNode(2)
    unbalanced_tree.right = TreeNode(2)
    unbalanced_tree.left.left = TreeNode(3)
    unbalanced_tree.left.left.left = TreeNode(4)

    print("\nExpected: False")
    print("Result:  " , isBalanced(unbalanced_tree))

    # Problem 5
    print("\nProblem 5 Test  \nExpected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]")
    print("Result:  " , pascalsTriangle(5)) 

    # Challenge
    challenge_tree = TreeNode(1)
    challenge_tree.left = TreeNode(2)
    challenge_tree.right = TreeNode(3)
    challenge_tree.left.left = TreeNode(4)
    challenge_tree.left.right = TreeNode(5)
    challenge_tree.right.left = TreeNode(6)
    challenge_tree.right.right = TreeNode(7)

    print("\nChallenge Test:")
    print("Before Populating Next Pointers:")
    print_next_pointers(challenge_tree)
    challenge(challenge_tree)
    print("\nAfter Populating Next Pointers:")
    print_next_pointers(challenge_tree)


# Helper function to print next pointers
def print_next_pointers(root):
    current = root
    while current:
        temp = current
        while temp:
            print(temp.key, end=" -> ")
            temp = temp.next
        print("None")
        current = current.left


# Run the test
test_problems()