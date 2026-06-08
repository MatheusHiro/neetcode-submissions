class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            l = dict()
            count_t = 0
            count_s = 0

            for i, letter in enumerate(s):          
                if letter not in l:
                    l[letter] = [0, 0]
                    
                if t[i] not in l:
                    l[t[i]] = [0, 0]
                    
                l[letter][0] = l[letter][0]+ 1
                l[t[i]][1] = l[t[i]][1]+ 1

            for i in l:
                if l[i][0] != l[i][1]:
                    return False
            return True