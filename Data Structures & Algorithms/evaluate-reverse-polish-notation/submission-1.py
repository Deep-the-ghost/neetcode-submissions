class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        op = ["+","-","/","*"]
        for ch in tokens:
            if ch not in op:
                nums.append(int(ch))
            else:
                if ch == "+":
                    a = nums[-1] + nums[-2]
                    nums.clear()
                    nums.append(a)
                elif ch == "-":
                    a = nums[-1] - nums[-2]
                    nums.clear()
                    nums.append(a)
                elif ch == "/":
                    a = nums[-1] / nums[-2]
                    nums.clear()
                    nums.append(a)
                elif ch == "*":
                    a = nums[-1] * nums[-2]
                    nums.clear()
                    nums.append(a)
    
        return nums[-1]           


