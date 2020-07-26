# P1
s = 'azcbobobegghakl'
vow_count = 0
for c in s:
    vow_count += int(c in "aeiou")
print("Number of vowels: ", vow_count)
