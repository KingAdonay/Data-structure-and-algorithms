from typing import List
from collections import defaultdict

'''
721. Accounts Merge

Approach the problem as a disjoint set union, each account as a single set and when
similar emails exist in two different sets, merge the accounts.

Keep track of the representatives of each group (index as id) and by traverse through each email and assign each email a group, which initially will be the group it is in.
Keep track of the email-group dictionary and when an email appears twice, merge the group of the email in the email-group with the current group that you are looking at. 

Create a dictionary for each group with the list of email that they represent.

Get the name for the account from the original accounts list for each group, sort the emails, and add the name at the front of the list and add it to the results list.

Time complexity: O(MNlogMN)
'''
class DSU:
    def __init__(self, sz: int):
        self.representatives = []
        self.size = []
        for i in range(sz):
            self.representatives.append(i)
            self.size.append(1)

    
    def find_representative(self, node: int) -> int:
        if node == self.representatives[node]:
            return node
        
        # path compression
        self.representatives[node] = self.find_representative(self.representatives[node])
        return self.representatives[node]
    
    def union_by_size(self, a: int, b: int) -> None:
        representativeA = self.find_representative(a)
        representativeB = self.find_representative(b)

        if representativeA == representativeB:
            return
        
        if self.size[representativeA] >= self.size[representativeB]:
            self.representatives[representativeB] = representativeA
            self.size[representativeA] += self.size[representativeB]
        else: 
            self.representatives[representativeA] = representativeB
            self.size[representativeB] += self.size[representativeA]


class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        email_group = {}
        groups = defaultdict(list)
       
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in email_group:
                    dsu.union_by_size(i, dsu.find_representative(email_group[email]))
                else:
                    email_group[email] = i
           
                
        for email, group in email_group.items():
            group_rep = dsu.find_representative(group)
            groups[group_rep].append(email)
        
        results = []
        for group, emails in groups.items():
            name = accounts[group][0]
            ans = [name, *sorted(emails)]
            results.append(ans)

        return results
    
#Testcases:
s = Solution()
print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]) == [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
print(s.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]) == [["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])
print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]) == [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]])