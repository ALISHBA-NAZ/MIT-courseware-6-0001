#Recursion
#Multiplication iteration solution
def mult_iter(a,b):
    result = 0
    #iteration
    while b>0:
        #current value of computation a running sum
        result += a
        #current value of iteration variable
        b -= 1
    return result


def mult(a, b):
    #base case
    if b == 1:
        return a
    #recursion step
    else:
        return a + mult(a, b-1) 
print(mult_iter(4,3))
    
#recursion function scope example
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))


def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

#fibonacci
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
print(fib(5))

#testing for palindromes
def ispalindrome(s):

    def tochars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def ispal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])
    return ispal(tochars(s))
                 
print(ispalindrome('eve'))
print(ispalindrome('Able was I, ere I saw Elba'))
print(ispalindrome('Is this a palindrome'))

