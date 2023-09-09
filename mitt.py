#returning a tuple
def quotient_and_remainder(x, y):
    q = x//y
    r = x % y
    return(q, r)
(quot , reman)= quotient_and_remainder(5, 3)
print(quot)
print(reman)
#iterating over tuples
def get_data(aTuple):
    nums =()
    words =()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    return(min_n, max_n, unique_words)
test = ((1,"a"),(2,"b"),(1,"a"),(6,"b"))
(a,b,c)=get_data(test)
print("a:",a,"b:",b,"c:",c)
#apply any data you want!
tswift = ((2022,"harry"),
          (2021,"koe"),
          (2020,"jam"),
          (2019,"hans"),
          (2018,"alish"))
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!")

#list
L =[2,1,3,4,5]
total = 0
for i in L:
    total += i
    print(i)

#operations
l = [2,1,3,6,3,7,0]
l.remove(2)
print(l)
l.pop()
print(l)
del(l[1])
print(l)

s = "hey < alish"
d = list(s)
print(d)
a = s.split('<')
print(a)
L = ['a','b','c','d','e']
e = ''.join(L)
print(e)
f = '_'.join(L)
print(f)

L = [9,6,0,3]
l1=sorted(L)
print(l1)
l2 = L.sort()
print(l2)
l3 = L.reverse()
print(l3)

#ALIASING
a=5
b=a
print(a)
print(b)
warm = ['red','yellow','orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)

#cloning
cool = ['red','yellow','blue','grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool)

#sorting list
warm = ['red','yellow','blue','grey']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cool = ['grey','green','brown']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)

#lists of lists of lists of...
warm = ['green','brown']
hot = ['red']
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)
hot.append('pink')
print(hot)
print(brightcolors)

#Mutations and iteration
#
def remove_data(l1, l2):
    for i in l1:
        if i in l2:
            l1.remove(i)
        
def remove_dups_new(l1, l2):
    l1 = l1[:]
    for i in l1:
        if i in l2:
            l1.remove(i)
            
l1 = ['red', 'orange' , 'green']
l2 = ['orange', 'blue', 'purple']
remove_data(l1, l2)
print(l1,l2)

l1 = [1,2,3,4,5]
l2 = [1,2,5,7,8]
remove_dups_new(l1 ,l2)
print(l1, l2)

#exercise
cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)
print(warm)

colors1 = [cool]
print(colors1)
colors1.append(warm)
print('colors1 = ', colors1)

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)

warm.remove('red') 
print('colors1 = ', colors1)
print('colors2 =', colors2)

for e in colors1:
    print('e =', e)

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)

flat = cool + warm
print('flat =', flat)

print(flat.sort())
print('flat =', flat)

new_flat = sorted(flat, reverse = True)
print('flat =', flat)
print('new_flat =', new_flat)

cool[1] = 'black'
print(cool)
print(colors1)