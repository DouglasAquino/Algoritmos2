m1=[[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

i = 0
while i < 3:
     j = 0
     t = 0
     while j < 3:
          t += m1[i][j]
          j += 1
     print(i, '---', t)
     i += 1
print()
