class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0 : return False
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        test = []
        ob = ["(","{","["]
        cb = ["]","}",")"]

        for ch in s:
            if ch in ob:
                test.append(ch)
            elif ch in cb and len(test) != 0 and pairs[ch] == test[-1]:
                test.pop()
            else:
                return False

        if len(test) == 0 :
            return True
        else:
            return False        



