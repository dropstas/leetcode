class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        f = []
        for i in range(len(s)):
            if s[i] in ('([{'):
                f.append(s[i])
            else:
                if  (f == [] and s[i] in (')]}') ) or \
                    (s[i] == ')' and f[-1] != '(') or \
                    (s[i] == '}' and f[-1] != '{') or \
                    (s[i]== ']' and f[-1] != '['):
                    return False
                else:
                    f.pop()

        return f == []