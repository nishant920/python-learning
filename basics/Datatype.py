from decimal import Decimal


x = 5;
x = "hello";
x = [1, 2, 3];
print(x);
print(type(x));
print(id(x));
a = str(5) + "5";
print(a);


print(0.1 + 0.2);#FLOATING POINT ERROR
"""
    • Preserving Exact Characters: A string like "0.3" is not meant for CPU math, so Python does not convert it to binary.
      It simply stores the exact characters you typed in memory, preserving the 0, the ., and the 3 untouched.
    • Why Decimal("0.3") Works: When you pass "0.3" into Decimal(), 
      the Decimal module reads the text characters directly from left to right and builds its own base-10 number in software. It completely bypasses Python's binary float parser.

"""
print(Decimal("0.1") + Decimal("0.2")); 