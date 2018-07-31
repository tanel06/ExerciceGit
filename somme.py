def produit(a,b):
    return a*b

def somme(a,b):
    return a + b

def affiche_result(a,b,s):
    ch = '{} + {} = {}'.format(a,b,s)
    print(ch)


def somme_rec(a,b):
    if b==0:
        return a
    elif a== 0:
        return b
    else:
        return somme_rec(a+1,b-1)


affiche_result(4, 5, somme(4,5))
affiche_result(11, 10, somme(11,10))
affiche_result(3,3, somme(3,3))
affiche_result(7,3, somme_rec(7,3))
affiche_result(somme(2,2), somme(5,5), somme_rec(4,10))

