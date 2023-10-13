for index in range(5,15):
    print(index)


Mark=float(input('Put ur mark here :'))
if 80<=Mark<=100:
    print('A+')
elif 79>=Mark>=70:
    print('A')
elif Mark<=69:
    print('F')
else:
    print("Invalid value")


email=input('your email:').lower().strip()
Nam=input('Name :').title()
print(email,Nam)


def invoice(name,taka,date):
    print(f'{name} has {taka} taka due on {date}.')
Name=input('your name :')
invoice(Name,400,'13 Aug 2023')
invoice('Mili',4030,'30 aug 2023')



def name(Name): 
    print(f'Good morning {Name}')
name("Ann")


n=4**2
print(n)
n2=pow(3,2)
print(n2)


print('He said,"Hello Berbie."')
print('"Hi"\"Hello\"\"Hola"')


#converting pound to kg
Weight=float(input('Your weight in pound :'))
pound=10.56
print('your weight is ',Weight*pound,'kg.')
