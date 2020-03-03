def preorder_iterative(root):
    result = []
    stack = []
    curr = root
    while curr != None or len(stack) > 0:
        while curr != None:
            result.append(curr.val)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop().right
    return result

def inorder_iterative(root):
    result = []
    stack = []
    curr = root
    while curr != None or len(stack) > 0:
        while curr != None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

def postorder_iterative(root):
    result = []
    if not root:
        return result
    stack = [[root,-1]]
    while len(stack) > 0:
        curr = stack[-1][0]
        state = stack[-1][1]
        stack[-1][1] += 1
        if state == -1 and curr.left != None:
            stack.append([curr.left,-1])
        elif state == 0 and curr.right != None:
            stack.append([curr.right,-1])
        elif state == -1:
            result.append(stack.pop()[0].val)
    return result
