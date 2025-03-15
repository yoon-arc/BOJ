K, D, N = input().split()
N = int(N)
#움직임
#행, 열로 저장
moves = {'R':[0,1], 'L':[0,-1],'B':[-1,0],'T':[1,0],'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1]}
#범위 확인
def in_range(h,y):
    return 0<=h<8 and 0<=y<8
#킹의 위치
kh,ky = int(K[1])-1, ord(K[0])-65
# print(kh, ky)
#돌의 위치
dh, dy = int(D[1])-1,ord(D[0])-65
#명령문 수행하기
for _ in range(N):
    n = input()
    nkh, nky = kh+moves[n][0],ky+moves[n][1]
    ndh, ndy = dh, dy
    # print(f"움직이기 전{kh}는 {nkh}으로, 움직이기 전 {ky}는 {nky}로")
    #돌의 위치와 겹치는지
    if nkh == dh and nky == dy:
        #겹친다면 돌 위치도 업데이트
        ndh, ndy = dh+moves[n][0],dy+moves[n][1]
        # print("돌 위치 업데이트에서 걸림")
    #돌과 킹 둘 다 범위 내에 있는지 확인
    if not in_range(nkh, nky) or not in_range(ndh, ndy):
        # print(f"범위 계산에서 걸림, 킹의 위치는 {nkh,nky} 돌의 위치는 {ndh, ndy}")
        continue
    #문제 없다면 값 업데이트
    kh, ky = nkh, nky
    dh, dy = ndh, ndy

updateK = chr(ky+65) + str(kh+1)
updateD = chr(dy+65) + str(dh+1)
print(updateK)
print(updateD)


    