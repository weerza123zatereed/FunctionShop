def login():
    Username = input("Username : ")
    Password = input("Password : ")
    if Username == "admin" and Password == "1234":
        print("!done!")
        return True
    else:
        print("login Fail")
        return login()
def showMenu():
    print("---CalculatorForShop---")
    print("1.VatCalculator")
    print("2.PriceCalculator")
def menuSelect():
    Userinput = int(input(">>"))
    if Userinput == 1:
        print("result: ", vatCalculator(int(input("price: "))))
    elif Userinput == 2:
        print("result: ",priceCalculator())
    else:
        print("Please select again")
        return menuSelect()
def vatCalculator(totalprice):
    vat=7
    result=totalprice+(totalprice*vat/100)
    return result
def priceCalculator():
    price1=float(input("First product price: "))
    price2=float(input("Second product price: "))
    return vatCalculator(price1+price2)

login()
showMenu()
menuSelect()



