# #5176번
# 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
# # 추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.
# 완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
# N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
# [입력]
#
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
#
# 다음 줄부터 테스트 케이스의 별로 N이 주어진다. 1<=N<=1000
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# main idea : making binary search tree follows same sequence of Inorder traversal
# but, Insert ascending numbers while traversal
# n : tree index / last : number of nodes
def Inorder(n,last):
    global cnt
    # because we use recursive function, this conditional statement means,
    # while tree index less than number of nodes -> Do:~~
    if n <= last:
        # left child's index = parent's index * 2
        Inorder(2*n,last)
        # we change node's value after escape from first recursive function
        tre[n] = cnt
        # and then, count up.
        cnt += 1
        # right child's index = (parent's index * 2) +1
        Inorder(2*n+1,last)



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # Create tree with list, size : N+1 (we don't use "0" index to make equal with node number and tree index)
    tre = [0] * (N+1)
    cnt = 1
    Inorder(1,N)
    print('#{0} {1} {2}'.format(tc,tre[1],tre[N//2]))