def Sort_Down(list):
    list.sort(reverse=True)

a = []
for i in range(0,3):
    a.append(int(input()))

Sort_Down(a)

print(a)
