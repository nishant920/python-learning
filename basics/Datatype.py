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

"""
    3. Core types vs Java
    Java	                Python	            Notes
    int, long, BigInteger	int	                Arbitrary precision. No overflow.
    double	              float	              64-bit, same floating-point issues
    BigDecimal	          decimal.Decimal	    Critical for billing. Never use float for money.
    boolean	              bool	              True/False (capitalized)
    null	                None	              Compare with is None, not == None
    String	              str	                Immutable, like Java

"""
item = [];

if not item:                     # Pythonic. Not: if len(items) == 0
    print("empty"); 

name = "Nishant"
f"Hello {name}, total: {19.5 * 2:.2f}"   # f-string, replaces String.format. the f stands for "formatted" and tells Python to evaluate any variables, math, or expressions inside {} directly within the string. Without the f prefix, Python treats {name} and {19.5 * 2:.2f} as plain literal text instead of executing them
name[0]       # 'N'
name[-1]      # 't' (negative index counts from the end)
name[1:4]     # 'ish' (slice: start inclusive, end exclusive)
name[::-1]    # reversed
name.upper(), name.strip(), name.split(","), ",".join(["a", "b"])