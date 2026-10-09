'''
question is to provide all possible products of prime numbers given
1 is not a prime number
'''

def generateProducts(primes):
    '''
    question can be modelled like getting subsets and finding the products of these subsets, and that is what we do
    we use the take or not take, so include number to get product, or not include number
    we do not want 1 to be included in our result that is why there is an explicit check for it

    TC: O(2^n)
    SC: O(2^n + N) extra N is for the recursion stack
    '''
    result = []
    def getProducts(index, product):
        if index == len(primes):
            if product != 1:
                result.append(product)
            return
                
        getProducts(index + 1, product * primes[index])
        
        getProducts(index + 1, product)
        
    getProducts(0, 1)
    return result
