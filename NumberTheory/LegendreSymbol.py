def QR3(a, b):
    if a%4==3 and b%4==3:
        return -1

    return 1


def QR1(b):
    if b%4==3:
        return -1
    return 1

def QR2(b):
    if b%8==3 or b%8==5:
        return -1
    return 1

def QR(a, b):
    a=a%b
     
    if a==1:
        return 1
    if a==b-1:
        return QR1(b)

    if a==2:
        return QR2(b)
    result=1
    while a%2==0:
        a//=2
        result*=QR2(b)
        if a==2:
            return result*QR2(b)   
    return result*QR3(a, b)*QR(b, a)
