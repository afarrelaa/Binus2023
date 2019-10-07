#%%
def shuffle_card():
    import itertools ,random
    cardnumbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    cardtype = list(itertools.product(cardnumbers,["heart","diamond","spade","club"]))
    print("You have these cards :")
    random.shuffle(cardtype)
    for i in range(52):
        print(cardtype[i][0], "of", cardtype[i][1])

shuffle_card()







#%%