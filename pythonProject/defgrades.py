def pass_or_fail(score):
    if score <50:
        res="Fail"
    else:
        res="Pass"
    return res
#defining a function to find out if it's pass or fail
def average(grades):
    score=0
    for i in grades:
        score=score+i
    avg=score/len(grades)
    return avg
#defining a function to calculate average
def main():
    grades=[]
    total_grades=int(input("Input total amount of grades you'd like to put in: "))
    for i in range(total_grades):
        gr=(int(input("Input a grade: ")))
        grades.append(gr)
    avg=average(grades)
    res=pass_or_fail(avg)
    print(res)
main()

