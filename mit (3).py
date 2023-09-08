t = (2,"mit",3)
tuple = t[0]
print(tuple)
tu = (2,"mit",3)+(5,6)
print(tu)
tu = t[1:2]
print(tu) 
tu = t[1:3]
print(tu)
tu = len(t)
print(tu)
#tu = t[1] = 4
#print(tu)


def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
       nums = nums + (t[0],)
       if t[1] not in words:
          words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

#list
L = [2, 'a', 4, [1,2]]
list = len(L)
print(list) 
list = L[0]
print(list) 
list = L[2]+1
print(list) 
list = L[3]  
i = 2
list = L[i-1]
print(list)

#mutates the list (operation on list)
l = [2,1,3]
l[1] = 5
print(l)
l.append(5)
print(l)

#operation on list
l1 = [2,3,1]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)
l1.extend([0,6])
print(l1)

l = [2,3,4,5,6,7,0]
l.remove(2)
print(l)
del(l[1])
print(l)
l.pop()
print(l)

#What is the value of L after you run the code below?
L = ["life", "answer", 42, 0]
for thing in L:
 if thing == 0:
  L[thing] = "universe"
  print(L[thing])
 elif thing == 42:
  L[1] = "everything"
  print(L[1])
print(L)
  
#What is the value of L3 after you execute all the operations in the code below?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.extend(L4)
L3.sort()
del(L3[0])
L3.append(['fa','la'])
print(L3)

#What is the value of brunch after you execute all the operations in the code below?
L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]
brunch = L1
L1.append("juice")
brunch.extend(L2)
print(brunch)