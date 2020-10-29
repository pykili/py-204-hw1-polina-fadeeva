for smth in 'a'*10:
    ID = int(input())
    FORM = input()
    LEMMA = input()
    CHTO_TO = input()
    condition = FORM == LEMMA
    if condition == False:
      print(FORM, LEMMA)
    else:
        continue
