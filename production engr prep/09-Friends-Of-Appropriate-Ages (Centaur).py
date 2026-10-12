'''
A slight variation of Friends Of Appropriate Ages (leetcode 825)
A group of centaurs (mythical half-human, half-horse creatures) all sign up for Facebook accounts at the same time.
They immediately start sending each other friend requests, in accordance with the ancient rules that have governed centaur friendship since the dawn of time:

A centaur will only send a friend request to another centaur if the recipient is at least (X/2 + 7) of the sender's age. For example, a 200-year old centaur can only send friend requests to centaurs that are at least 107 years old.
A centaur will not send a friend request to another centaur that is older than it is.
A centaur over 100 years old will not send a friend request to a recipient under 100 years old. But centaurs under 100 years old can friend each other.
If any of the conditions for sending a friend request are not met, no friend request will be sent.
Write a function that, given an array of centaur ages, returns an integer of the total number of friend requests that the group of centaurs will send to each other.
c = [120, 110] # 1
c = [120,110,99] # 1
c = [120,45,230,400,88,300,101] # 4
c = [101, 120, 230, 400, 88, 45, 55, 300] # 6
c = [100,110,120] # 3

these are the conditions for a request to be made from A to B written out
B >= (0.5 * A) + 7
A >= B
A > 100, then B >= 100
'''

import collections
def count_requests(ages):
    '''
    This is an optimization over the bruteforce, here we know that ages can repeat ie we can have duplicate ages in the list representing different centaurs and we do not want to do repeated work
    so we get the count of each age, get the unique ages themselves in a list, and then we can iterate through the list, take an age, compare it with other ages including itself since that age can belong to
    multiple centaurs, then if the conditions are met ie it can send a request, then we consider:
    - if the age_A we took and the age_B we are comparing against are the same, we multiply count_A * (count_A - 1) 
    example: if the age is 110, and it has a count of 5, we do 5 * 4 which is 20, which represent each centaur of age 110 sending to 4 other centaurs with the same age, but it can't send to itself
    - if the ages are different, we simply multiply count_A by count_B, since the ages are different and everybody with age_A can send request to everybody in age_B

    TC: O(N + U^2) where N is the number of ages in input and cost is incurred when we build the map, U is the number of unique ages, if we go by the LC question, this is a maximum of 120
    so that U^2 is more or less constant time
    SC: O(U) or O(1) since U is constant  
    '''
    age_counts = collections.Counter(ages)
    unique_ages = list(age_counts.keys())
    
    requests = 0
    for age_A in unique_ages:
        count_A = age_counts[age_A]
        for age_B in unique_ages:
            count_B = age_counts[age_B]
            
            if not (age_B >= (0.5 * age_A) + 7):
                continue
            if age_B > age_A:
                continue
            if age_A > 100 and age_B < 100:
                continue
                
            if age_A == age_B:
                requests += (count_A * (count_A - 1))
            else:
                requests += (count_A * count_B)
    return requests



'''
bruteforce approach is to take each centaur, compare it against every other centaur available to see if it can send a request to each one of them
TC: O(N^2), SC: O(1)
'''
def count_requests(ages):
    requests = 0
    n = len(ages)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            centaur_A = ages[i]
            centaur_B = ages[j]
            
            if not (centaur_B >= (0.5 * centaur_A) + 7):
                continue
            if not (centaur_A >= centaur_B):
                continue
            if centaur_A > 100 and centaur_B < 100:
                continue
            requests += 1
    return requests 