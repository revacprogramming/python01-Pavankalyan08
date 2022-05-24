def computepay(hours , rate):
    print("in computepay",hours,rate)
    if hours>40:
        a=hours*rate
        b=(hours-40.0)*(rate*1.5)
        pay=a+b
    else :
        pay=hours*rate
    print("returning",pay)
    return pay
sh=input("enter the hours:")
sr=input("enter the rate:")
fh=float(sh)
fr=float(sr)

xp=computepay(fh,fr)
print("pay:",xp)
