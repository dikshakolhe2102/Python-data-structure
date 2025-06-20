# to take a declare a integer list and calculate sum of all elements of list ,find minimum and maximum value od list 



a=[99,6,9,88,22,4,5]


print(max(a))
print(min(a))
print(sum(a))


# 2# to take number from user and check given number is in list or not.
# if yes= find sum of all list elements and sort given list ascending order
# else:
#     convert given list into descending order


a=[5,6,8,9,4,3]
num=int(input("Enter a number:"))

if num in a:
    print(sum(a))
    print(sorted(a))
    print(sorted(reversed(a)))

else:
     print(sorted(a,reverse=True))




#3 # ddeclare two list 
# if both ==
# then repeat it 3 times
# else : concate

a=[5,6,8,9,4,3]
b=[5,6,8,9,4,2]

if a==b:
     print(a*3,b*3)
    
else:
     print(a+b)


# 
l=[1,2,10,2,4,5]
l=[]


# exapmles
# to declare one list and form second list from one which contain even number using list comprehension


# even numbers
l=[1,2,10,2,4,5]
o=(i for i in l if i%2==0) #in l print(i))
print(o)

#  at even index
l=[1,2,10,2,4,5]
l1=[]
o=[l[i]for i in range(len(l))if i%2==0]
print(o)



#  write a program take a list from given list which contain words ,
# return only those less than 5 character

words=['abc','dfgh','asdfghj']
word=[]

for i in words:
     if len(i)<5:
          word.append(i)
print(word)

# another way

word=[i.title() for i in words if len(i)<5]

print(word)





# 2to find second largest number from list 

l=[20,30,11,2,3,55,7]
l1=(l.sort())
print(l[-2])


#3  to take a elemet of a list from a user 

b=[]
for i in range(5):
     a= int(input("Enter a number:"))
     b.append(a)
print(b)

# 4 to remove duplicates # question





# 03/06/2025

# append function

l=[1,2,3,4,5]
print("Append(element):",l.append(6))
print("Append(element)")

# 
b1=[]
b=[]
for i in range(5):
     a=int(input("Enter a list:"))
     b.append("Original list:",a)
print(b)

for i in b:
     if i not in b1:
          b1.append(i)
print("Remove duplicate numbers:",b1)




#question #  to take a value from user and find  that a value in list 
# # if it present then replace it with python
# only updte first occurence of an element


l=[3,4,5,6,8,9]

num=int(input("Enter a list:"))
index=l.index(num)
l[index]="python"
print(l)




l=['abca','aba','abcd','xyx']
count=0
for i in l:
  if len(i)>2 and i[0]==i[-1]:
     # print(l)
     count+=1
print("count of length having more than 2 and alpha is same at 0 and -1:",count)

     

# swapping the [0] with [-1]
l=['abca','aba','abcd','xyx']
# b=['xyx','abcd','abca','abca']
l[0],l[-1],l[1],l[-2]=l[-1],l[0],l[-2],[3]
print(l)






l=[]  
while True:  
    print("1.Add a name to list:")
    print("2.Remove from list:")
    print("3.show:")
    print("0.Exit:")
    choice =input("Enter a choice:")
    if choice =='1':
         a=(input("1.Add a name to list:"))
         l.append(a)
    elif choice=='2':
         a=(input("2.Remove from list:"))
         l.remove(a)
    elif choice=='3':
        
         print(l)
    elif choice=='4':
         break
    else:
         print("enter a correct choice")

print(l) 








# program to tske s inout from user and printn its hexadecimal value

s=int(input("Enter a number:"))
print(hex(s))


#  to swap two values taken from values 


a=int(input("Enter value:"))
b=int(input("Enter value:"))
print(a,b==b,a)


#  two values from user and shit first number by second number

a=int(input("Enter value:"))
b=int(input("Enter value:"))
print(a>>b)
print(a<<b)



print("\u2443")