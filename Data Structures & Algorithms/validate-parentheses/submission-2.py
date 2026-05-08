class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if  p=='(' or p=='{' or p=='[':
                stack.append(p)
            else:
                if stack==[]:
                    return False
                if p==')' and stack[-1]=='(':
                    stack.pop()
                elif p=='}' and stack[-1]=='{':
                    stack.pop()
                elif p==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        return True if stack==[] else False