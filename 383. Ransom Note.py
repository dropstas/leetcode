ransomNote = "abded" 
magazine = "abcdeefewd"

# alphabet = [0] * 26

for i in ransomNote :
    if i not in magazine :
        continue
    magazine = magazine.replace(i,'',1)
    print(magazine)


# def exc(ransomNote, magazine):
#     ransomNote = list(ransomNote)
#     magazine = list(magazine)
#     check = []
#     for i in ransomNote:
#         for j in magazine:
#             if i == j:
#                 check.append(j)
#                 magazine.remove(j)
#                 break
    
#     if check == ransomNote:
#         return True
#     else:
#         return False

# print(exc(ransomNote, magazine))
            