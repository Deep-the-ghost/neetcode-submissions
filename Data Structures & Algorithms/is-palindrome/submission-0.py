class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split(" ")
        s = "".join(s)
        n = len(s)
        i = 0
        j = n-1
        k = [",",".","?","!"]
        while i <= j:
            if s[i] in k:
                i += 1
            if s[j] in k:
                j -= 1
            if s[i].lower() != s[j].lower() :
                return False
            else:
                i += 1
                j -= 1
        return True                    
