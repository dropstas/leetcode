s = "A man, a plan, a canal: Pansama"

def tf(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    for i in range(len(s)):
        if s[i] == s[len(s) - i-1]:
            return  

print(tf(s))