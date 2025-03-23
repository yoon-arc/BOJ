N = int(input())
tree = {}
#트리에 값 입력
for _ in range(N):
    root,left, right = input().split()
    tree[root] = [left, right]
#전위 순회
def print_pre(n):
    if n == '.':
        return
    #현재 노드
    print(n, end="")
    print_pre(tree[n][0])
    print_pre(tree[n][1])
    
#중위 순회
def print_now(n):
    if n == '.':
        return
    print_now(tree[n][0])
    print(n, end="")
    print_now(tree[n][1])
#후위 순회
def print_post(n):
    if n == '.':
        return
    print_post(tree[n][0])
    print_post(tree[n][1])
    print(n,end="")

print_pre('A')
print()
print_now('A')
print()
print_post('A')