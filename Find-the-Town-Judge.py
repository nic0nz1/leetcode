class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = {}
        judges = []
        for rel in trust:
            if rel[0] not in hashmap:
                hashmap[rel[0]] = [rel[1]]
            else:
                hashmap[rel[0]].append(rel[1])
        for i in range(1,n+1):
            if i not in hashmap:
                judges.append(i)
        if len(judges) != 1:
            return -1
        count = 0            
        for i in range(len(trust)):
            if trust[i][1] == judges[0]:
                count += 1
        if count != n-1:
            return -1

        return judges[0]