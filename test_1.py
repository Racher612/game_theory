def option1(s):
    return s + 1



def option2(s):
    return s * 2



def option3(s):
    return s * 5



def win(s):
    return (option1(s) >= varwin) or (option2(s) >= varwin)



def steps(s, step, winner):
    if step in winstep:
        if win(s):
            return True
        else:
            if step == max(winstep):
                return False
    if step % 2 == winner:
        if win(s):
            return False
        else:
            return steps(option1(s), step + 1, winner) or steps(option2(s), step + 1, winner)
    else:
        if win(s):
            return False
        else:
            return steps(option1(s), step + 1, winner) and steps(option2(s), step + 1, winner)



pete = 1
van = 0
winstep = [2,4]
varwin = 102

for i in range(1, 100):
    if steps(i, 1, van):
        print(i)
