a = '480K'

def unification(string):
    if ('K' in string) == True:
        remove_k = string.replace('K','')
        return float(remove_k)*0.001
    elif ('M' in string) == True:
        remove_m = string.replace('M','')
        return float(remove_m)
    else:
        return float(string)

print('ps3'.upper())
