def option1(x1, x2):
    return x1 + 1



def option2(x1, x2):
    return x1 * 3



def win(x, y):
    return any(list(map(lambda el: sum(el) >= varwin, variants(x, y))))



def variants(x, y):
    a = []
    for fun in fun_list:
        a.append([fun(x, y), y])
        a.append([x, fun(y, x)])
    return a



def steps(x, y, step, winner):
    if step in winarr:
        if win(x, y):
            return True
        else:
            if step == max(winarr):
                return False
    if win(x, y):
        return False
    if step % 2 == winner:
        return any(list(map(lambda el: steps(el[0], el[1], step + 1, winner), variants(x, y))))
    else:
        return all(list(map(lambda el: steps(el[0], el[1], step + 1, winner), variants(x, y))))


pete = 1
van = 0
fun_list = [option1, option2]

winarr = [2, 4]
varwin = 45
s0 = 4



for i in range(1, varwin+1):
    if steps(s0, i, 1, van):
        print(i, end = '')