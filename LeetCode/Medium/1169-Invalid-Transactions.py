class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        The approach here is to use a dict as an additional data structure when compared to the solution below. In the initial solution, we were comparing each transaction with all the 
        other transactions after it in the list even if they were not from the same person, we still had to iterate through it. But with this, we can iterate through only the transactions for a 
        particular person
        we check for Rule 1 when we populate the parsed and mapping, a
        rule 2, is checked for each transaction, we loop through all other transactions made by the same person, this reduces the work we do rather than having to check
        even with other people's own

        note that we should not use "continue" after invalidating a transaction cos of the amount is greater than 1000, if we use continue that means that transacttion would not in parsed and our ddictionary
        we do not want this, because that transaction can still be the cause why another transaction is invalidated through Rule 2

        TC: O(N.M), worst case O(N^2). where N is the size of the transactions and M is the average size of a transaction per person.
        in worse case, all transactions are carried out by the same person, so we end up doing N.N
        SC: O(N)

        """
        mapping = defaultdict(list)
        invalid = set()

        parsed = []
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(',')
            parsed.append((name, int(time), int(amount), city, i))

            if int(amount) > 1000: 
                invalid.add(i)

            mapping[name].append([int(time), int(amount), city, i])

        for i in range(len(parsed)):
            name = parsed[i][0]
            nameTransactions = mapping[name]
            for trans in nameTransactions:
                if abs(parsed[i][1] - trans[0]) <= 60 and parsed[i][3] != trans[2]:
                    invalid.add(parsed[i][4])
                    break

        return [transactions[i] for i in invalid]

        '''
        Approach here is we parse the input strings to make it more easier to understand working with. for each string, we split and put in a tuple,
        also including its position in the transactions list. we use a set to keep track of indexes of invalid transacctions. we do not store the invalid transaction
        string itself because we could have same strings that both are invalid, using this would condense them into one string. if we use a list to store them, we risk end up 
        storing a transaction that is invalid from two conditions, so we would end up storing it twice. storing the index in a set is better, if we have same strings we have different indexes in the 
        set and if a single string is invalid for two reasons, we do not count it twice.

        note that we have no guarantee that the strings are ordered by their time of transaction, so we need to take abs when doing the subtraction in order not to get negative cos a transaction that happened earlier 
        could be down the list. note that we add both transactions as invalid if they fall under the second rule.

        then we return the strings using the indexes, we can return answer in any order so this is fine as sets are unordered.

        TC: O(N^2)
        SC: O(N)
        '''
        parsed = []

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            parsed.append((name, int(time), int(amount), city, i))

        invalid = set()

        for i in range(len(parsed)):
            if parsed[i][2] > 1000:
                invalid.add(i)

            for j in range(i+1, len(parsed)):
                if parsed[i][0] == parsed[j][0]:
                    if abs(parsed[i][1] - parsed[j][1]) <= 60 and parsed[i][3] != parsed[j][3]:
                        invalid.add(i)
                        invalid.add(j)

        return [transactions[i] for i in invalid]
