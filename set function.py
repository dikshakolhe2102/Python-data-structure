# s={1,2,3,4,5,1,2}
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))
# print(all(s))
# print(any(s))
# print(sorted(s))
# print(sum(s,100))
# print(sorted(s,reverse=True))

# s1={1,2,3,4,5,6,7}
# print(list(reversed(list(s1))))

# #add function
s2={1,2,3,4,5,3,5}
print(s2.add(8))
# print(s2)
# #s2.add(10,20)
# s2.add("abc")
# s2.add(1)
# print(s2)
# s2.add((1,2,3))
# print(s2)
# #s2.add()
# print(s2)

# #update function
# s={1,4,6,8,6}
# #s.update(10)
# #print(s)
# s.update((1,2))
# print(s)
# s.update("hello")
# print(s)

# #remove function
# s={5,8,8,9,5,3,2,4}
# s.remove(9)
# print(s)
# #s.remove(1)
# print(s)

# #discard 
# s={3,5,7,57,54,4}
# s.discard(100)
# print(s)

# #Pop
# s1={1,2,3,57,46,75,12}
# removed=s1.pop()
# print("poped element",removed)
# print("after pop",s1)

# #clear all
# s1={12,23,42,41,3}
# s1.clear
# print(s1)

# #to take 5 element of a set from user
# s=set()
# for i in range(5):
#     a=input("Enter the element")
#     s.add(a)
# print(s)

# #to take a value from user and delete given value from set
# s1=set()
# for i in range(5):
#     a=input("enter element:")
#     s1.add(a)
# print(s1)
# s1.discard(100)
# print(s1)

#to take elements of set from user and convert given set into list if given element present in set
s=set()
for i in range(6):
    a=input("enter element:")
    s.add(a)
    print(s)
if i in s:
    print(list(s))
else:
    print(s)

# #to take iterable object 1st string 2nd list 3rd tuple from user and add all this in set as a set element 
# a=input("Enter string")
# s=set()
# s.add(a)
# print(s)


# b=input("enter list")
# s=set()
# print(list(b))
# s.add(b)
# print(s)

# a=input("Enter tuple")
# s=set()
# print(tuple(a))
# s.add(a)
# print(s)






