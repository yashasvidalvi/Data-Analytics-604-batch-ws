n = [1,2,3,4,5]

l = int(input("Enter a number of position: "))
l= l% len(n)
n[:] = n[-l:]+n[:-l]
print(n)