class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl = list(s.split())
        
        if len(pattern) != len(sl):
            return False 

        se = set()
        dict = {}
        
        for i in range(len(pattern)):
            if pattern[i] in dict:
                if sl[i] != dict[pattern[i]]:
                    return False
            else:
                if sl[i] not in se:
                    dict[pattern[i]] = sl[i]
                    se.add(sl[i])
                else:
                    return False

        return True