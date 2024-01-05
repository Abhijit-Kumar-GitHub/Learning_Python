n = int(input("no. of elements in set s: "))
s = set(map(int, input("set s elements separated be space: ").split()))
N = int(input("no. of operations performed: "))
print("the original set:",s)


for count in range(N):
    operation = input("enter the operation no.",N,": ")
    li = list(operation) 
    i = li[-1]
    if "pop" in operation:
        print("The set before operation",N,":",s)
        s.pop()
        print("The set after operation",N,":",s)
    elif "remove" in operation:
        print("The set before operation",N,":",s)
        s.remove(i)
        print("The set after operation",N,":",s)
    else:
        print("The set before operation",N,":",s)
        s.discard(i)
        print("The set after operation",N,":",s)

print("The final set:", s)
print(sum(s))

