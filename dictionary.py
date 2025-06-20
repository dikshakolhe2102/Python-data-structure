# #creation of dictionary using {} bracets
#keys are inmutable and values are mutable

# d={}
# print(type(d))
# d1={'Name':'abc','roll':20}
# print(d1)
# d2={1:{'a':'b'}, 2:{'c':'d'}}
# print(d2)
# #d3={[1,2]:10}
# #print(d3)
# d4={10:[1,2]}
# print(d4)
# d5={'Name':'abc','roll':20,'Name':'pqr'}
# print(d5)
# d6={'Name':'abc','roll':20,'name':'pqr'}
# print(d6)

#creation of dictionary using dict() constructor
# d=dict()
# print(d)
# d1=dict(['abc',10])
# print(d1)
d2=dict(name='abc',roll=1)
print(d2)
d3=dict([(1,'one'),(2,'two')])
print(d3)


#accessing dictionary
# d={1:'a',2:'b'}
# print(d[1])

# d1={'Name':'pqr','Mark':20}
# print(d1['Name'])

# #update value
# d1['Name']="abc"
# print(d1)
# d1['Rollno']=10
# print(d1)

# #delete 
# d={1:'a',2:'b'}
# print(d[1])
# del d[1]
# print(d)

#traversing using for loop
d={1:'a',2:'b'}
print(d)
for i in d:
    print(i)

for i in d:
    print(d[i])

for i,j in enumerate(d):
    print(j,d[j])

# #using while loop

# d={1:'a',2:'b'}
# print(d)
# i=0
# while(i<len(d)):
#     print(d[i])
#     i+=i


    

    