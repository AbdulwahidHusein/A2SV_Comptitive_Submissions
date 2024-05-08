# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

l = int(input())
vow = ["a", 'e','i',  'o','u','y']
w = input().strip()
s = []
for a in w:
    if s:
        if a in vow and s[-1] in vow:
            continue
        
    s.append(a)
    
s = "".join(s)
print(s)