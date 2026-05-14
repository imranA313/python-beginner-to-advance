s1 = "abaaba"
s2 = "amaama"
s3 = "abcba"

s1Half = len(s1) // 2
s2Half = len(s2) // 2
s3Half = len(s3) // 2

# check string is symmetrical or not

if len(s1) % 2 != 0:
    s1Sym = s1[:s1Half] == s1[s1Half + 1:]
else:
    s1Sym = s1[:s1Half] == s1[s1Half:]

print(f"string {s1} is symmetrical: ", s1Sym)

if len(s1) % 2 != 0:
    s2Sym = s2[:s2Half] == s2[s2Half + 1:]
else:
    s2Sym = s2[:s2Half] == s2[s2Half:]

print(f"string {s2} is symmetrical: ", s2Sym)

if len(s1) % 2 != 0:
    s3Sym = s3[:s3Half] == s3[s3Half + 1:]
else:
    s3Sym = s3[:s3Half] == s3[s3Half:]

print(f"string {s3} is symmetrical: ", s3Sym)

# check string is palindrome or not
s1Pal = s1 == s1[::-1]
print(f"string {s1} is palindrome: ", s1Pal)
s2Pal = s2 == s2[::-1]
print(f"string {s2} is palindrome: ", s2Pal)
s3Pal = s3 == s3[::-1]
print(f"string c{s3} is palindrome: ", s3Pal)
