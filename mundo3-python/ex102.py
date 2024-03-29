def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero
    :parametro n: O numero que vai ser calculado
    :parametro show: (opcional) Mostrar ou nao a conta.
    :return: O valor do fatorial de um numero n.      
    """  
    f = 1          
    for c in range(n, 0 , -1): 
        if show:        #Se show 
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c               
    return f

print(fatorial(5,True))
print(fatorial(3))

