class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        for s in string:
            if s == "(" or s == "[" or s == "{":
                stack.append(s)
            elif s == ")":
                if len(stack)==0 or stack.pop() != "(":
                    return False
            elif s == "]":
                if len(stack)==0 or stack.pop() != "[":
                    return False
            elif len(stack)==0 or s == "}":
                if len(stack)==0 or stack.pop() != "{":
                    return False
        return (stack == [])
                    

        