# P3
s = 'ouqxzbmm'
ls = ''
longest = ''
for i,c in enumerate(s):
    if (c >= s[i-1]) or (i ==0):
        ls += c
    else:
        longest = max(longest,ls,key=len)
        ls = c
print("Longest substring in alphabetical order is:", max(longest,ls,key=len))
