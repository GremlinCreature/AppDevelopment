def average_args(*gr):
    score=0
    for i in gr:
        score=score+i
    avg=score/len(gr)
    return avg
def pass_or_fail(score):
    if score <50:
        res="Fail"
    else:
        res="Pass"
    return res
print(pass_or_fail(average_args(45,56,34,67,76,87,34,56)))
print(average_args(45,56,34,67,76,87,34,56))

