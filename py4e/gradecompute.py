s = input("input a score between 0 and 10 to get a grade:")

s = float(s)

def computegrade(score):
    grade = "F"
    if score >= 0.6:
        print("score >= 0.6")
        grade = "D"
    if score >= 0.7:
        print("score >= 0.7")
        grade = "C"
    if score >= 0.8:
        print("score >= 0.8")
        grade = "B"
    if score >= 0.9:
        print("score >= 0.9")
        grade = "A"


computegrade(s)
