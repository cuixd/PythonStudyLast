import itertools

'''
组合
'''

l1 = list(itertools.combinations("abcd",1))

print(l1)
print(len(l1))

'''
4 4  1
4 3  4
4 2  6
4 1  4

n! / m!(n-m)!
'''