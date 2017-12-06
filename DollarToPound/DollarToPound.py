dollars = []
done = False
dollarToPound = .74
while not done:
    x = input("Give dollar amount, say \"quit\" to stop ")
    if x == "quit":
        done = True
    else:
        try:
            dollars += [float(x)]
        except ValueError:
            print("Must be numbers")
for i in range(0,len(dollars)): dollars[i] = chr(163)+str(round(dollars[i]*dollarToPound,2))
print(dollars)
