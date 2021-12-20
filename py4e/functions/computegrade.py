# This version uses elif, which makes it more efficient

s = input("input a score between 0 and 1 to get a grade: ")

def computegrade(score):
    try:
        score = float(score)
        if not(0 <= score < 1):
            return "Bad score"

        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"

        return grade
    except:
        return "Bad score"

ans = computegrade(s)
print(ans)
