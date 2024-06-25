class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = ''
        c = ''

        for i in strs:
            if i == '':
                return ''

        for i in range(len(min((word for word in strs if word), key=len))):
            for l in strs:
                if f == l[i]:
                    pass
                elif f =='':
                    f = l[i]
                else: 
                    f = ''
                    break
                    
            else:
                c = c + f
                f = ''  # only executed if the inner loop did NOT break
                continue
            break  # only executed if the inner loop DID break

        return c