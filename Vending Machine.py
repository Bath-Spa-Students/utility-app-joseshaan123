#First, we create a dictionary for both of the snacks and drinks
#Dictionary for snacks
snacks={"1":{"Snack":"Kurkure Small","RATE":"2","On the Market":10},
        "2":{"Snack":"Kurkure Large","RATE":"5","On the Market":10},
        "3":{"Snack":"Bugles  Small","RATE":"1.50","On the Market":10},
        "4":{"Snack":"Bugles  Large","RATE":"4.50","On the Market":10},
        "5":{"Snack":"Lays Maxx Large","RATE":"5","On the Market":10}
        }
#Dictionary for drinks
drinks={"1":{"Drink":"Al Rawabi Chocolate Milk","RATE":"2","On the Market":10},
        "2":{"Drink":"Al Rawabi Strawberry Milk","RATE":"2","On the Market":10},
        "3":{"Drink":"Sunfeast Dark Fantasy Chocolate Milk","RATE":"1.50","On the Market":10},
        "4":{"Drink":"Sunfeast Dark Fantasy Strawberry Milk","RATE":"4.50","On the Market":10},
        "5":{"Drink":"Laban Up","RATE":"1","On the Market":10}
        }
#Making a menu listing all the Snacks and drinks in the menu with its rate and stock
def print_menu():
 print("-----------------------------------------------------------------")
 print("""HELLO!

WELCOME TO SHAAN'S VENDING MACHINE 

WE HAVE VARIOUS VARIETIES OF SNACKS 
AND DRINKS TO YOUR LIKING""") 

 print("""+----------------------------------------------------------------------------+
|                            SHAAN'S VENDING MACHINE                         |
|                                                                            |
|                                    MENU                                    |
+----------------------------------------------------------------------------+
|                                    SNACKS                                  |
+----------------------------------------------------------------------------+
|Code|            ITEMS                 |       PRICE       |  ON THE MARKET |
+----------------------------------------------------------------------------+
| 01 | Kurkure Small                    |       2.00        |       10       | 
| 02 | Kurkure Large                    |       5.00        |       10       |
| 03 | Bugles Small                     |       1.50        |       10       |
| 04 | Bugles Large                     |       4.50        |       10       |
| 05 | Lays Maxx Chicago Hot Wings Small|       3.50        |       10       |  
+----------------------------------------------------------------------------+
|                                    DRINKS                                  |
+----------------------------------------------------------------------------+
|Code|              ITEMS               |      PRICE      |  ON THE MARKET   |
+----------------------------------------------------------------------------+
| 06 | Al Rawabi Chocolate Milk         |      2.00       |       10         |
| 07 | Al Rawabi Strawberry Milk        |      2.00       |       10         |
| 08 | Sunfeat Dark Fantasy Chocolate   |      1.50       |       10         |
| 09 | Sunfeast Dark Fantasy Strawberry |      4.50       |       10         |
| 10 | Laban Up                         |      3.50       |       10         | 
+----------------------------------------------------------------------------+""") 
#Making it in loop so users can use multiple times.
while True:
  
  snack_code=None
  drink_code=None
  TOTAL=0
  print_menu()
  
   
#Then we make a variable snack_code where you can input the snack you like to have
  while True:
   snack_code= input("Which Snack Would you like to have?:")
   if snack_code in snacks:
    break
   else:
     print("Wrong Code")
     
  current_snack=snacks[str(snack_code)]
#When you give the code to the preffered snack, it prints the name of the snack with the rate of the snack.
  print("You have chosen "+current_snack["Snack"]+".The prize is $"+current_snack["RATE"])
#You can select how much of the preffered item you want on the market.
  on_the_market= current_snack["On the Market"]
#user_quantity is the variable that inputs the number of snacks you want.
#The Output aldready shows the number of stock availbale on the market.
#If the input is more than that of the stock on the market, the output will show Out of Stock.
  while True:
    print("The stock available for "+current_snack["Snack"]+" is "+str(current_snack["On the Market"]))
    user_quantity= int(input("How many of "+current_snack["Snack"]+" Do you want?:"))
    if on_the_market - user_quantity>=0:
     current_snack["On the Market"] -= user_quantity
     TOTAL+=user_quantity*float(current_snack["RATE"]) 
     break
    else:
     print("Out of stock")
  
  else:
   print("Wrong input")
 
#This is the choice if you want to buy a drink.
  drink_required=input("Would you like a Drink?(enter 0 to continue or any other key to stop):")
#If the user inputs 0, it will continue the user to which drink he prefers or
#If the user doesnt want to buy drinks, they can input any key of thier preference 
#which directly takes them to the total amount of the snacks.
  if drink_required== "0":
#The user can input the code of the preffered drink.
#If the user inputs a wrong code, it will show Wrong code until 
#the user has input the correct code. 
   while True:
    drink_code=input("Which drink would you like to have?:")
    if drink_code in drinks:
       current_drink=drinks[str(drink_code)]
       break
    else:
      print("Wrong Code")
#The preffered item and the rate is shown after the user inputs the preffered item code.
   print("You have chosen "+current_drink["Drink"]+".The prize is $:"+current_drink["RATE"])
   on_the_market= current_drink["On the Market"]
   while True:
    print("The stock available for "+current_drink["Drink"]+" is "+str(current_drink["On the Market"]))
#The user can input how much of the preffered drink the user wants.
#If the user inputs more than the available stock on the market.
# it shows that its out of stock.
    user_quantity= int(input("How many of"+current_drink["Drink"]+"Do you want?:"))
    if on_the_market - user_quantity>=0:
     current_drink["On the Market"] -= user_quantity
#The total amount of the price of the drink is multiplied 
#by the number of times the user has brought
     TOTAL+=user_quantity*float(current_drink["RATE"]) 
     break 
    else:
     print("Out of stock")
          
   
#The total amount of the preffered items the user has input.  
  while True:
      TC=input("YOUR TOTAL IS $"+str(TOTAL)+".please enter the amount here to succesfuly complete the purchase:")
      if TC==str(TOTAL):
       print("Thank you for your purchase! We are happy to serve you.")
       break
      else:
         print("Sorry!You have entered the wrong amount.Please enter the correct amount.")


