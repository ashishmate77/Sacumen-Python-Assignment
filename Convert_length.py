num1 = input('Enter the value: ')
unit1 = input('Which unit do you want it converted from:  ')
unit2 = input('Which unit do you want it converted to: ')

if unit1 == "m" and unit2 == "yd":
    ans = float(num1)*1.094
    print(ans,'yd')
    
elif unit1 == "m" and unit2 == "in":
    ans = float(num1)*39.37
    print(ans,'in')
    
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans,'km')

elif unit1 == "m" and unit2 == "ft":
    ans = float(num1)*  3.281
    print(ans,'ft')
    
elif unit1 == "yd" and unit2 == "m":
    ans = float(num1)/1000
    print(ans,'m')
    
elif unit1 == "yd" and unit2 == "in":
    ans = float(num1)*36
    print(ans,'in')
    
elif unit1 == "yd" and unit2 == "km":
    ans = float(num1)/1094
    print(ans,'km')
    
elif unit1 == "yd" and unit2 == "ft":
    ans = float(num1)*3
    print(ans,'ft')
    
elif unit1 == "in" and unit2 == "m":
    ans = float(num1)/39.37
    print(ans,'m')
    
elif unit1 == "in" and unit2 == "yd":
    ans = float(num1)/36
    print(ans,'yd')
    
elif unit1 == "in" and unit2 == "ft":
    ans = float(num1)/12
    print(ans,'ft')
    
elif unit1 == "in" and unit2 == "km":
    ans = float(num1)/39370
    print(ans,'km')
    
elif unit1 == "ft" and unit2 == "in":
    ans = float(num1)*12
    print(ans,'in')
