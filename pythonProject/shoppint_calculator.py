def purchases_total (**purch):
    total=0
    for key in purch.keys():
        total=total+purch.get(key)
    return total
def discount (**purch):
    v = ['a', 'e', 'i', 'o', 'u']
    V = ['A', 'E', 'I', 'O', 'U']
    for key in purch.keys():
        letters=list(key)
        for i in v:
            if letters[0]==i:
                new_value=purch.get(key)*0.95
                purch.update({key:new_value})
        for i in V:
            if letters[0]==i:
                new_value = purch.get(key) * 0.95
                purch.update({key:new_value})
    return purch
