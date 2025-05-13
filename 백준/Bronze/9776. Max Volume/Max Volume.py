pi = 3.14159
n = int(input())
max_val = 0
for _ in range(n):
    info = list(input().split())
    figure = info[0]
    if figure == 'S':
        max_val = max(max_val, pow(float(info[1]),3)*pi*(4/3))
    elif figure == 'C':
        max_val = max(max_val, pi*pow(float(info[1]),2)*float(info[2]))
    else:
        max_val = max(max_val, pi*float(info[2])*pow(float(info[1]),2)*1/3)
print(f"{max_val:.3f}")