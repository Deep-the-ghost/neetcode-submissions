class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        op = ["+","-","/","*"]
        for ch in tokens:
            if ch not in op:
                nums.append(int(ch))
            else:
                a = nums.pop()
                b = nums.pop()

                if ch == "+":
                    nums.append(a+b)
                elif ch == "*":
                    nums.append(a*b)
                elif ch == "-":
                    nums.append(b-a)
                elif ch == "/":
                    nums.append(b/a)

    
        return nums.pop()          


