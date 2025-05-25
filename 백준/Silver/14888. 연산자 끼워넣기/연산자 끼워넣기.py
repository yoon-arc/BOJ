import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
p,s,m,d = map(int, input().split())
ops = {'+':p, '-':s, '*':m, '//':d}

min_val = sys.maxsize
max_val = -sys.maxsize

def dfs(ci, cv):
    global min_val, max_val
    if ci == N:
        #최대, 최소 갱신
        min_val = min(cv, min_val)
        max_val= max(cv, max_val)
        return
       
    for op in ops:
        if ops[op]:
            ops[op] -= 1
            #계산
            if op == '+':
                nv =  cv + nums[ci]
            elif op == '-':
                nv = cv - nums[ci]
            elif op == '*':
                nv = cv * nums[ci]
            elif op == '//':
                if cv < 0:
                    nv = -(abs(cv)//nums[ci])
                else:
                    nv = cv//nums[ci]
            #재귀
            dfs(ci+1, nv)
            ops[op] += 1

dfs(1, nums[0])
print(max_val)
print(min_val)