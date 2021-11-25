# Author: Cesar Vicente
# Date  : April 5, 2019
# it prints the quantity, item price, and the total for the item.

produce = {"apple":0.45, "lettuce":1.10, "carrot" || "carrots":0.05, "asparagus":0.10,
         "tomato":0.95, "cucumber":0.20, "potato":0.45, "onion":0.55,
           "apples":0.45, "lettuces":1.10, "asparagus":0.10,
         "tomatoes":0.95, "cucumbers":0.20, "potatoes":0.45, "onions":0.55}

print("Farmer's Markets Produce Company")

for i in produce:
    print(i, "$" + format(produce.get(i), '0.2f'), end="  ")
print("")
print("Type the quantity and the item name. '0' to exit.")
totalList = []

while True:
    buy = input("Quantity Item: ").lower()
    x = buy.split(" ")

    if len(x) > 1 and x[1] in produce:
        price = format(produce.get(x[1]) * int(x[0]), '0.2f')
        print(x[0], x[1], "@", "$" + format(produce.get(x[1]), '0.2f'),
              "each =", "$" + price)
        totalList.append(float(price))

    elif len(x) > 1 and x[1] not in produce:
        print("Item not found")

    elif len(x) == 1 and x[0] == "0":
        total = 0
        for i in totalList:
            total += i
        print("=" * 20)
        print("Your total is $" + str(format(total, '0.2f')) + ".")
        print("Sign up for a Farmer's Market Produce Credit Card today and save 10%")
        break
