opcode_dic = {'ADD':'0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011', 'OR':'0100', 'NOT':"0101", 'MULT':"0110", 
              'LSFTL':'0111', 'LSFTR':'1000', 'ASFTR':'1001', 'RL':'1010', 'RR':'1011'}
N = int(input())
for _ in range(N):
    ans = ''
    op, rD, rA,s = input().split()
    rD,rA,s = map(int, [rD,rA,s])
    # C처리
    if op[-1] == 'C':
        ans += opcode_dic[op[:-1]] + '10'
    else:
        ans += opcode_dic[op] + '00'
    #이진법 앞에 두 글자 잘라내기 , 3자리 유지
    ans += str(bin(rD))[2:].zfill(3)
    ans += str(bin(rA))[2:].zfill(3)
    if ans[4] == '1':
        ans += str(bin(s))[2:].zfill(4)
    else:
        ans += str(bin(s))[2:].zfill(3) + '0'
    print(ans)