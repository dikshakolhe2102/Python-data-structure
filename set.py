s={}
print("Empty set:",s)
print("type of s:",type(s))

s1={1,2,3,4,"hello"}
print("set s1:",s1)

s={1,2,3,4,1,2}
print("Set with duplicates",s)

#traversing
s={1,2,3,4,5,6,7,8}
for element in s:
    print("elements:",s)

s={1,2,3,4,5}
l=(list(s))
i=0
while (i<len(l)):
    print(l(i))
    i+=1

del s
print(s)

