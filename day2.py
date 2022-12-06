a=[1,7,2,4,2,2,3,8,5]
print("Original List :",a)
print(".append(0) :",a.append(0))
print(".count(2) :",a.count(2),)
print(".sum():",sum(a))
print(".pop() :",a.pop())
print(".clear() :",a.clear())
print('')
print("Sets:")
a={1,7,2,4,2,2,3,8,5}
b={1,2,3,4,5}
print("Set 1 :",a)
print("Set 2 :",b)
a.add(0)
print("a.add(0) :",a)
print("a.difference(b) :",a.difference(b),)
print("a.union(b):",a.union(b))
print("a.intersection(b) :",a.intersection(b))
print(".clear() :",a.clear())
print('')
print("Dictionary:")
a={'A':1,'B':2,'C':3,'D':4,'E':5}
print("a.keys() :",a.keys())
print("a.values() :",a.values())
print("a.get():",a.get('D'))
a['F']=6
print("a.item :",a)
print(".clear() :",a.clear())




print('')
print("Factorial, Prime, Odd Even:")
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def prime(n):
    f=0;
    if n==2:
        print(n,"is a prime number")
    elif n==1:
        print(n,"is neither prime nor composite")
    elif n<1:
        print("Invalid input")
      
    else:
        for i in range(2,n):
            if n%i==0:
                f=1
                break
        if f==0:
            print(n,"is a prime number")
        else:
            print(n,"is a composite number")

def oddeven(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")


a=int(input("Enter a number: "))
print("Factorial of ",a," is ",factorial(a))
prime(a)
oddeven(a)