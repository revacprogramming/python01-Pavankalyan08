num=0
tot=0.0
while True:
    sval=input("enter a number")
    if sval=='done':
        break
    try:
        sval=float(sval)
    except:
        print("invalid input")
        continue
    num=num+1
    tot=tot+sval
print(tot,num,tot/num)