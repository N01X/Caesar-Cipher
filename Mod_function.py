def mod(a, b):  
    try:
        if 0 < a < b:
            return a

        elif a > b > 0:
            t1 = a//b
            t2 = a - t1*b
            return t2
    

        elif a<0 or b<0 :
            t1 = (a*-1)//b

            if a*-1 == t1*b:   
                return 0
            else:
                t2 = b - (a*-1 - t1*b)
                return t2

        elif a == 0 and b != 0 or a == b and b !=0:
            return 0

        else: 
            return "undefined"

    except ZeroDivisionError:
        return "undefined"


