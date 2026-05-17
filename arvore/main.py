import funcoes as fc

root = fc.TreeNode('R')
nodeA = fc.TreeNode('A')
nodeB = fc.TreeNode('B')
nodeC = fc.TreeNode('C')
nodeD = fc.TreeNode('D')
nodeE = fc.TreeNode('E')
nodeF = fc.TreeNode('F')
nodeG = fc.TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.left.data:", root.right.left.data)