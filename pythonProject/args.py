def average_args(*gr):
    score=0
    try:
        for i in gr:
            score=score+i
        avg=score/len(gr)
    except TypeError:
        return "Please, input only numbers."
    return avg
def pass_or_fail(score):
    try:
        if score <50:
            res="Fail"
        else:
            res="Pass"
    except TypeError:
        return "Please, input a valid score."
    return res
print(pass_or_fail(average_args(45,56,76,67,76,87,34,56)))
print(average_args(45,56,76,67,76,87,34,56))

