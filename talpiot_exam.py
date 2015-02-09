def max_find(my_list):
    my_list = my_list[:]
    if len(my_list) == 1: return my_list[0]
    if len(my_list) == 0: return
    l,r = 0, len(my_list) - 1
    while r - l > 0:
        mdl = (r + l) // 2
        if my_list[mdl] < my_list[mdl + 1]:
            l = mdl + 1
        elif my_list[mdl] > my_list[mdl + 1]:
            r = mdl
        else:
            if r == len(my_list) - 1: r -= 1
            my_list.pop(mdl)
            
    return my_list[r]

COINS = [200,100,50,20,10,5,2,1]
def change(n):
    for i in range(len(COINS)):
        val = n // COINS[i]
        if val: print(str(COINS[i]) + ': ' + str(val))
        n %= COINS[i]

PENS = [11, 9, 7]
def can_i_buy(x):
    if x in PENS: return True
    for pen in PENS:
        if x < pen: continue
        if can_i_buy(x - pen): return True
    return False
