from datetime import date
import Animal
f=[]
sell=[]
acu=0
def Buy():
    t=("chicken","pig","cow")
    c=input("animal's code: ")
    confirm=True
    if f: #true si la lista no está vacía, false si está vacía
        for x in f:
            if(x.GetCode()==c):
                confirm=False
    if confirm:
        trae=int(input("Price: "))
        w=int(input("Weigth: "))
        tipe=input("What is the animal to buy: ").lower()
        o = True
        for s in t:
            if(s==tipe):
                o=True
        if(o):
            if(tipe=='chicken'):
                ts=input("¿Fattening or Laying: ").lower()
                e=int(input("age in months: "))
                print(date.today())
                a=Animal.Chicken(c,w,trae,tipe,str(date.today()))
                a.Chicken(ts,e)
                a.ToString()
                f.append(a)
            elif (tipe=='pig'):
                sex=input("sex: ")
                a=Animal.Pig(c,w,trae,tipe,str(date.today()))
                a.Pig(sex)
                a.ToString()
                f.append(a)
            elif (tipe=='cow'):
                mp=input("milker or production: ").lower()
                a=Animal.Cow(c,w,trae,tipe,str(date.today()))
                a.Cow(mp)
                a.ToString()
                f.append(a)
            else:
                print("in this momento you can't buy this animal")
        print("Thanks for your bought")
    else:
        print("Sorry, the code typed has already been created")
def Sell():
    if f:
        print("this the animal's list to sell, please pay attencion to the parameters of the each animal according your need")
        global acu
        for x in f:
            x.Information()
        print("type the animal's code to buy")
        code=input("Code: ")
        for x in f:
            if x.GetCode()==code:
                r=x
                f.remove(x)
        if (r.GetTipe()== 'chicken'):
            if(a.Chicken.type=='fattening'):
                print("The price of this animal is ",r.GetPrice()*1.45)

                acu=acu+r.GetPrice()*1.45
            else:
                print("The price of this animal is ",r.GetPrice()*1.30)

                acu = acu + r.GetPrice() * 1.30
        elif (r.GetTipe()== 'pig'):
            print("The price of this animal is ", r.GetPrice() * 1.50)
            acu = acu + r.GetPrice() * 1.50
        elif (r.GetTipe()== 'cow'):
            print("The price of this animal is ", r.GetPrice() * 5000)
            acu = acu + r.GetPrice() * 5000
        r.SetDateSell(str(date.today()))
        sell.append(r)
    else:
        print("In this moment there is not animals for to sell")

def Calculate():
    global acu
    print("The profit obtained at until moment is: ",acu)
def Change():
    if f:
        choise=input("change weight or age of the an animal?: ").lower()
        if choise=='weight':
            print("choose the animal's code: ")
            for x in f:
                x.Information()
            code=input("code: ")
            for x in f:
                if x.GetCode()==code:
                    print("Remember that you only can change the weight in a 'x' valor")
                    w=int(input("x valor: "))
                    x.SetWeight(w)
                    a=x
            print("Update successful, this is the new weight->",a.GetWeight())
        elif choise=='age':
            print("choose the animal's code: ")
            for x in f:
                if x.GetTipe()=='chicken':
                    x.Information()
            code = input("code: ")
            for x in f:
                if x.GetCode() == code:
                    a = int(input("new age: "))
                    x.SetAge(a)
            print("Update successful")
        else:
            print("Please write weight or age to change")
    else:
        print("There is not animals in the list")
def Determ():
    if sell or f:
        print("Input a date in this format AAAA-MM-DD")
        ds=input("Date: ")
        bought=0
        soled=0
        for x in sell:
            if x.GetDateBought()==ds:
                bought=bought+1
            if x.GetDateSell()==ds:
                soled=soled+1
        for x in f:
            if x.GetDateBought()==ds:
                bought=bought+1
        print(" animals bought in ",ds,"=",bought,'\n'+
        "animals soled in ",ds,"=",bought)
    else:
        print("There is not animals soled or bought")
s=True
d={'1': Buy, '2': Sell, '3': Calculate, '4': Change,'5':Determ}
while s==True:
    print("------------------------")
    print("""THIS IS THE FARM'S MENU
    1.register a purchase
    2.Register a sale
    3.Calculate profit
    4.Change age or weight
    5.Determ
    6.exit
    """)
    print("-------------------------")
    a=input("Choose your option: ")
    try:
        if a=='6':
            s=False
            print("thank you for visit us")
        else:
            d[a]();
    except:
        print("Please choose a right option")
