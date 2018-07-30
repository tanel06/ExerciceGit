def somme(a,b):
    return a + b

def affiche_result(a,b):
    s = '{} + {} = {}'.format(a,b,somme(a,b))
    print(s)


affiche_result(4, 5)
affiche_result(11, 10)
