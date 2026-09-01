class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        seens1 = {}

        for ch in s1:
            seens1[ch] = 1 + seens1.get(ch,0)
        
        seens2 = {}

        for r in range(len(s2)):
            seens2[s2[r]] = 1 + seens2.get(s2[r],0)
            while (r-l+1) > n:
                seens2[s2[l]] -= 1
                if seens2[s2[l]] == 0:
                    del seens2[s2[l]]
                l += 1

            if seens1 == seens2 :
                return True

        return False                            

