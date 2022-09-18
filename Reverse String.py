ex_str = "12322"
rev = ''
for i in range(len(ex_str)-1,-1,-1):
    rev = rev + ex_str[i]
if rev == ex_str:
    print("It is a Palindrome")
else:
    print("No, its not a Palindrome")
