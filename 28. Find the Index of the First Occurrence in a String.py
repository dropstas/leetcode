class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        o = haystack.find(needle)

        if o == -1:
            return -1
        else:
            return o
        