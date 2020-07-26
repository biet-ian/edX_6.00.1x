# P2
s = 'azcbobobegghakl'
word_count = 0
while len(s):
    if 'bob' in s:
        word_count += 1
        s = s[s.find('bob')+1:]
    else:
        break
print("Number of times bob occurs is:", word_count)