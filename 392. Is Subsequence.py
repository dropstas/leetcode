s = "ab" 
t = "baab"
f = 0


for i in range(len(t)):
    if f <= len(s):
        if s[f] == t[i]:
            f +=1
print(f == len(s))


# for i in range(len(t)):
#     for j in s:
#         if t[i] == j:
#             f += str(t[i])

# print(f)



