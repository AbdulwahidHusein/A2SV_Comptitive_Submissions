def is_good(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True
    
def can_be_good(s1, s2):
    if is_good(s1):
        print("YES")
        return
    if not is_good(s2):
        print("NO")
        return
    else:
        left = s2[0]
        right = s2[-1]
        for i in range(len(s1)-1):
            if s1[i] == s1[i+1] and (s1[i] == left or s1[i+1]==right):
                print("NO")
                return
        print("YES")
tc = int(input())

for _ in range(tc):
    input()
    s1 = input().strip()
    s2 = input().strip()
    can_be_good(s1, s2)
                
            
        