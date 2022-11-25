'''
for/while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
'''
for x, y in enumerate(range(10, 1, -1)): # range(começo, fim, (progressivo ou regresivo))
    print(x, y)

# x = 10
# y = 0

# while x >= 0:
#     print(y, x)
#     y += 1
#     x -= 1