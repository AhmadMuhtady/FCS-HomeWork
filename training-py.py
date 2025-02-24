# session 1
# please type Hello World
# print("hello world")

name= input("Enter your name: ")
date= input("Enter the date: ")
item=[ item_1:=input("Enter the first item: "), 
      price_1:=int(input("Enter the price of the first item: ")), 
      item_2:=input("Enter the second item: "), 
        price_2:=int(input("Enter the price of the second item: ")),
      item_3:=input("Enter the third item: "), 
        price_3:=int(input("Enter the price of the third item: ")),]
total= price_1 + price_2 + price_3

recite_1 = {
"Name": name,
"Date": date,
"Item_1": item_1, "Price_1": price_1,
"Item_2": item_2, "Price_2": price_2,
"Item_3": item_3, "Price_3": price_3,
total: total
}
print(recite_1)