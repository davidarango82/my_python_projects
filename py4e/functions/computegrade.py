# Added this locally
s = input("input a score between 0 and 1 to get a grade: ")

def computegrade(score):
    try:
        score = float(score)
        if not(0 <= score < 1):
            return "Bad score"
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
        return grade
    except:
        return "Bad score"

ans = computegrade(s)
print(ans)