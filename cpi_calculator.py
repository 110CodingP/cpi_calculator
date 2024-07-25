from sys import stdin

totCredits = 0
totGrade = 0
mp = {"A":10,"B":9,"b":8,"C":7,"c":6,"D":5}
print("Please enter grade and credits in following format:")
print("grade credits")
print("Please write B+ as B and B as b, similarly for C+ and C")
for line in stdin:
    # as line ends in newline
    line.rstrip('\n') 
    grade, credits = line.split("\\s+")
    credits = int(credits)
    totCredits += credits
    totGrade += mp[grade]*credits
print(totGrade/totCredits)

# EOF is put in stdin by doing Ctrl-D once if at beginning or twice if at end of line