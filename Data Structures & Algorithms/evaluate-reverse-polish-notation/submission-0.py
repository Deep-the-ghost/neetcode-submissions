class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        res = []
        op = ["+","-","/","*"]
        for ch in tokens:
            if ch not in op:
                nums.append(int(ch))
            if ch in op and len(res) == 0:
                if ch == "+":
                    res.append(nums[-1] + nums[-2])
                elif ch == "-":
                    res.append(nums[-1] - nums[-2])
                elif ch == "/":
                   res.append(nums[-1] / nums[-2])
                elif ch == "*":              
                    res.append(nums[-1] * nums[-2])
            else:
                if ch == "+":
                    res.append(nums[-1] + res[-1])
                elif ch == "-":
                    res.append(nums[-1] - res[-1])
                elif ch == "/":
                   res.append(nums[-1] / res[-1])
                elif ch == "*":              
                    res.append(nums[-1] * res[-1])
        return res[-1]            


