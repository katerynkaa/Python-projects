import numpy as np
TEST = 10000

check = np.array(['1', '2', '3', '4', '5', '6'])

def game():
    ar = np.random.choice(check,4, replace = True)
    for i in range(1, TEST):
        get = np.random.choice(check, 4, replace = True)
        ar = np.hstack((ar, get))

    ar.shape = (TEST, 4)
    get = ar
    a = np.ones(4)
    money = 1
    wins = 0
    for i in range(TEST):
        summ = 0
        c = get[i, :]
        money -= 1
        for j in range(4):
            summ += int(c[j])
        if summ < 9:
            wins += 1
            money += 25
            a = np.vstack((a, c))
    aa = a[1:len(a), :]
    print (aa)
    return money, len(aa)/TEST, ('fair game fare %d' % (1/(len(aa)/TEST)))
print(game())

