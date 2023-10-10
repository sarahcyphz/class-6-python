from random import randint

def fair_coin(trials):
    success = 0
    for i in range(trials):     # increments for # of trials
        heads = 0
        for i in range(10):     # increments for # of tosses
            x = randint(1,2)    # 1 for heads 2 for tails
            if x == 1:
                heads += 1      # if heads add 1 to count
        if heads >= 7:
            success += 1
    return success / trials
print(fair_coin(10000))



def unfair_coin(trials):
    success = 0
    for i in range(trials):
        heads = 0
        for i in range(10):         # for 10 flips
            flip = randint(1,10)    
            if flip <= 6:           # if heads (bias of 60%)
                heads += 1
        if heads >= 7:
            success += 1
    return success / trials
print(unfair_coin(10000))

