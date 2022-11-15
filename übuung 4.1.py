list1=list(range(1, 100))
def math(x):
    return x*x+x

list2=list(map(math, list1))
print(list2)
