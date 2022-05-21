
def division(a,b):
    if(b!=0):
        divide = a / b
        error = False
    else:
        divide = 0
        error=True
    return divide,error

def validity(divide,error):

    if error==False:
        divide=divide+10
        error=True
    else:
        divide=divide-10
        error=False
    return divide,error

def parathaMaker(divide,error):

    if error==True:
        divide=divide*2
        error=False
    else:
        divide=divide*-2
        error=True
    return divide,error










