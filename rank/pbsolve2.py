


def f( a ) :
    soma = 0
    for el, i in enumerate(sorted( a ) , 1):
        soma += i * el
    return soma

def sortedSum(a):
    tmp = []
    result = 0
    for i in a:
        tmp.append(i)
        result += f( tmp )
    
    return int( result % ( 1e9 + 7) )
