# to generate fibonacci numbers both iteratively and recursively

# to get the fibonacci value at index n recursively
# TC: O(2^n), sC: O(n)
def fibonacciRec(n):
    if n <= 1:
        return n 
    return fibonacciRec(n - 1) + fibonacciRec(n - 2)

# to get the first n fibonacci numbers recursively
# TC: O(n), since the recursion is linear and we use only O(N) time, the appending too is like O(1) since we are just using the same list reference and not concatenating
def getFirstNFibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    previous = getFirstNFibonacci(n - 1)
    nextValue = previous[-1] + previous[-2]
    previous.append(nextValue)
    return previous


# get the fibonacci number at index n iteratively
def getFib(n):
    if n <= 1:
        return n
    
    # initialize a and b to be like the base case when we were using recursion
    # c represents the new sum we get, initially set to 0
    a, b, c = 0, 1, 0

    # go from 2 to n, since range() is exclusive of the right bounds
    for _ in range(2, n+1):
        c = a + b # add the element
        # readjust to be able to find the next fibonacci
        a = b 
        b = c

    return c # return the one we want after the loop is done


# get the first n fibonacci numbers iteratively
def getFibIteratively(n):
    ans = []
    for i in range(0, n):
        if i <= 1:
            ans.append(i)
        else:
            ans.append(ans[-1] + ans[-2])
    return ans


# usi



