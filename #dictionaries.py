#dictionaries
#student = {1: 'alish', 'age':19, 'courses':['math', 'computer']}
#student['phone']='333-5555'
#student['name']='alishnaz'
#student.update({'name':'naz','age':20, 'phone':'333-3333'})
#print(student['name'])
#print(student[1])
#print(student['courses'])
#print(student.get('phone','not found'))
#del student['age']
#age= student.pop('age')
#print(student)
#print(age)
#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())

#for key ,value in student.items():
#     print(key,value)

#grades = {'ana':'A', 'john':'A+','Harry':'C','kam':'B'}
#grades['sylvan']='A'
#print(grades)
#print(grades['john'])

#using dictionaries counting frequencies of words in song lyrics
#def lyrics_frequencies(lyrics):
#     mydict={}
#     for word in lyrics:
#          if word in mydict:
#               mydict[word] += 1
#          else:
#               mydict[word] = 1
#     return mydict
#    
#    
#she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
#'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#
#'you', 'think', "you've", 'lost', 'your', 'love',
#'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
#"it's", 'you', "she's", 'thinking', 'of',
#'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

#'she', 'says', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',

#'she', 'said', 'you', 'hurt', 'her', 'so',
#'she', 'almost', 'lost', 'her', 'mind',
#'and', 'now', 'she', 'says', 'she', 'knows',
#"you're", 'not', 'the', 'hurting', 'kind',

#'she', 'says', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',

#'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',

#'you', 'know', "it's", 'up', 'to', 'you',
#'i', 'think', "it's", 'only', 'fair',
#'pride', 'can', 'hurt', 'you', 'too',
#'pologize', 'to', 'her',

#'Because', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'Yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',

#'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'yeah', 'yeah', 'yeah',
#'yeah', 'yeah', 'yeah', 'yeah'
#]

#beatles = lyrics_frequencies(she_loves_you)
#print(beatles)

#def most_common_words(freqs):
#    values = freqs.values()
#    best = max(freqs.values())
#    words = []
#    for k in freqs:
#        if freqs[k] == best:
#            words.append(k)
#    return (words, best)

#comparing fibonacci using memoization
#def fib(n):
#     if n == 1:
#          return 1
#     elif n == 2:
#          return 2
#     else:
 #         return fib(n-1) + fib(n-2)
#result =fib(4)
#print(result)

#def fib_efficient(n, d):
#     if n in d:
#          return d[n]
#     else:
#          ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#          d[n] = ans
#    return ans
     
#d= {1:1, 2:2}
#arg = 34
#print(" ")
#print('using fib')
#print(fib(arg))
#print(" ")
#print('using fib_efficient')
#print(fib_efficient(arg, d))
 

#recursion 
#def factorial(n):
#    if (n==0 or n==1):
#          return 1
#     else:
#          return n * factorial(n-1)

#print(factorial(3))
#print(factorial(4))
#print(factorial(5))
#5 * factorial(4)
#5 * 4 * factorial(3)
#5 * 4 * 3 * factorial(2)
#5 * 4 * 3 * 2 * factorial(1)
#5 * 4 * 3 * 2 * 1 


