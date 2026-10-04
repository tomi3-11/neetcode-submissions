class Solution:
    # def isAnagram(self, s, t):
    #     return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = len(strs)
        # res = []
        # visited = [False] * n

        # for i in range(n):
        #     if visited[i]:
        #         continue # ignore if the list member has been visited

        #     group = [strs[i]]
        #     visited[i] = True

        #     for j in range(n):
        #         if not visited[j] and self.isAnagram(strs[i], strs[j]):
        #             visited[j] = True
        #             group.append(strs[j])

        #     res.append(group)
        # return res

        res = []
        mp = {}

        for i in range(len(strs)):
            s = strs[i]

            s = ''.join(sorted(s))

            if s not in mp:
                mp[s] = len(res)
                res.append([])

            res[mp[s]].append(strs[i])
        return res

        
        