from decimal import ROUND_HALF_UP, Decimal

print(type(10/2)) #the single slash operator (/) always performs true division, which returns a float
print(-9 // 4) #rounding down toward negative infinity gives -3 not -2 (Floor division (//) always rounds down toward negative infinity (the floor), rather than simply chopping off the decimal part toward zero)
print(bool(""))#"0" represents a string of lenth 1 so true if we use empty string it will be false
print("ab" * 3)#Python treats strings as sequences of characters, so multiplying "ab" by 3 concatenates "ab" + "ab" + "ab" together without any spaces
#You can only multiply a string by a whole number (int). Multiplying by a decimal like "ab" * 2.5 raises a TypeError
print(0.1 + 0.2 == 0.3)
a = [1, 2]; b = [1, 2]
print(a == b, a is b)#== checks whether two variables have the same value, while is checks whether they point to the exact same object in memory



price = 19.99;
quantity = 3;
total=price*quantity
gst=total*0.18;
print(total*gst);

price = Decimal("19.99");
quantity = Decimal("3");
total=price*quantity;
gst=total*Decimal("0.18");
complete = total+gst;
print(complete.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP));#.quantize(template): Formats a Decimal to match the decimal places of the template (Decimal('0.01') for 2 places, Decimal('0.1') for 1 place, Decimal('1') for whole numbers)
#ROUND_HALF_UP: Overrides Python's default Banker's Rounding (ROUND_HALF_EVEN) so .5 always rounds away from zero (standard school math).


s = "  Nishant,Java,Spring,Python  "
profile = s.strip().split(",")
skills=profile[1:]
print(f"Skilss: {", ".join(skills)}")#.join(skills) glues all items in the skills list together using that separator, producing the single string 'Java, Spring, Python'
# Step 1: ', '.join(skills)  -->  "Java, Spring, Python"
# Step 2: f"Skills: {...}"   -->  "Skills: Java, Spring, Python"
# Step 3: print(...)         -->  Prints: Skills: Java, Spring, Python


item = input("Item Name: ")
price = Decimal(input("Unit Price: "))
quantity = int(input("Quantity: "))

total = (price*quantity).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP);
print(f"{item:<1} x{quantity:<5} @ {price:>6.2f}  = {total:>8.2f}");