'''
This module provides access to the mathematical functions defined by the C standard.
These functions cannot be used with complex numbers.
use the functions of the same name from the cmath module if you require support for complex numbers. 
The distinction between functions which support complex numbers and those which don’t is made 
since most users do not want to learn quite as much mathematics as required to understand complex numbers. 
Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number 
used as a parameter, so that the programmer can determine how and why it was generated in the first place.
The following functions are provided by this module. Except when explicitly noted otherwise, 
all return values are floats.
'''
import math    
'''
#Constants
'''
'''
1- math.pi
The mathematical constant π = 3.141592…, to available precision.
'''
print("math.pi :", math.pi)                                      #math.pi : 3.141592653589793
'''
2- math.e
The mathematical constant e = 2.718281…, to available precision.
'''
print("math.e :", math.e)                                        #math.e : 2.718281828459045
'''
3- math.tau
The mathematical constant τ = 6.283185…, to available precision. Tau is a circle constant equal to 2π, 
the ratio of a circle’s circumference to its radius. To learn more about Tau, 
check out Vi Hart’s video Pi is (still) Wrong, and start celebrating Tau day by eating twice as much pie!
'''
print("math.tau :", math.tau)                                    #math.tau : 6.283185307179586
'''
4- math.inf
A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').
'''
print("math.inf :", math.inf)                                    #math.inf : inf
'''
5- math.nan
A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').
'''
print("math.nan :", math.nan)                                    #math.nan : nan
'''
#Number-theoretic and representation functions
'''
'''
1- math.ceil(x)
Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float
'''
print("math.ceil(15.2) :", math.ceil(15.2))                      #math.ceil(15.2) : 16
print("math.ceil(15.7) :", math.ceil(15.7))                      #math.ceil(15.7) : 16
print("math.ceil(-15.2) :", math.ceil(-15.2))                    #math.ceil(-15.2) : -15
print("math.ceil(-15.7) :", math.ceil(-15.7))                    #math.ceil(-15.7) : -15
'''
2- math.floor(x)
Return the floor of x, the largest integer less than or equal to x. If x is not a float
'''
print("math.floor(15.2) :", math.floor(15.2))                    #math.floor(15.2) : 15
print("math.floor(15.7) :", math.floor(15.7))                    #math.floor(15.7) : 15
print("math.floor(-15.2) :", math.floor(-15.2))                  #math.floor(-15.2) : -16
print("math.floor(-15.7) :", math.floor(-15.7))                  #math.floor(-15.7) : -16
'''
3- math.factorial(x)
Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
'''
print("The factorial of 0 is :", math.factorial(0))              #The factorial of 0 is : 1
print("The factorial of 4 is :", math.factorial(4))              #The factorial of 4 is : 24
print("The factorial of 7 is :", math.factorial(7))              #The factorial of 7 is : 5040
print("The factorial of 9 is :", math.factorial(9))              #The factorial of 9 is : 362880
print("The factorial of 15 is :", math.factorial(15))            #The factorial of 15 is : 1307674368000
'''
4- math.perm(n, k=None)
Return the number of ways to choose k items from n items without repetition and with order.
Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.
If k is not specified or is None, then k defaults to n and the function returns n!.
'''
print("math.perm(10, 2) :", math.perm(10, 2))                    #math.perm(10, 2) : 90
print("math.perm(5, 3) :", math.perm(5, 3))                      #math.perm(5, 3) : 60
'''
5- math.comb(n, k)
Return the number of ways to choose k items from n items without repetition and without order.
Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
Also called the binomial coefficient because it is equivalent to the coefficient 
of k-th term in polynomial expansion of the expression (1 + x) ** n
'''
print("math.comb(10, 2) :", math.comb(10, 2))                    #math.comb(10, 2) : 45
print("math.comb(5, 3) :", math.comb(5, 3))                      #math.comb(5, 3) : 10
'''
6- math.copysign(x, y)
Return a float with the magnitude (absolute value) of x but the sign of y. 
On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.
'''
print("math.copysign(10, -2) :", math.copysign(10, -2))          #math.copysign(10, -2) : -10.0
print("math.copysign(-10, 2) :", math.copysign(-10, 2))          #math.copysign(-10, 2) : 10.0
print("math.copysign(10, 2) :", math.copysign(10, 2))            #math.copysign(10, 2) : 10.0
print("math.copysign(-10, -2) :", math.copysign(-10, -2))        #math.copysign(-10, -2) : -10.0
'''
7- math.fabs(x)
Return the absolute value of x.
'''
print("math.fabs(15.3) :", math.fabs(15.3))                      #math.fabs(15.3) : 15.3
print("math.fabs(-15.3) :", math.fabs(-15.3))                    #math.fabs(-15.3) : 15.3
'''
8- math.fsum(iterable)
Return an accurate floating point sum of values in the iterable. 
Avoids loss of precision by tracking multiple intermediate partial sums:
'''
print("math.fsum([1, 4, 6]) :", math.fsum([1, 4, 6]))            #math.fsum([1, 4, 6]) : 11.0
print("math.fsum([2.5, 3.9]) :", math.fsum([2.5, 3.9]))          #math.fsum([2.5, 3.9]) : 6.4
print("math.fsum((1, 4, 6)) :", math.fsum((1, 4, 6)))            #math.fsum((1, 4, 6)) : 11.0
print("math.fsum((2.5, 3.9)) :", math.fsum((2.5, 3.9)))          #math.fsum((2.5, 3.9)) : 6.4
'''
9- math.gcd(a, b)
Return the greatest common divisor of the integers a and b. If either a or b is nonzero, 
then the value of gcd(a, b) is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.
'''
print("math.gcd(60, 48) :", math.gcd(60, 48))                    #math.gcd(60, 48) : 12
print("math.gcd(44, 8) :", math.gcd(44, 8))                      #math.gcd(44, 8) : 4
print("math.gcd(65, 45) :", math.gcd(65, 45))                    #math.gcd(65, 45) : 5
print("math.gcd(5, 45) :", math.gcd(5, 45))                      #math.gcd(5, 45) : 5
'''
10- math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
Return True if the values a and b are close to each other and False otherwise.
Whether or not two values are considered close is determined according to given absolute and relative tolerances.
'''
print("math.isclose(2.005, 2.005) :", math.isclose(2.005, 2.005))                                     #True
print("math.isclose(2.005, 2.007) :", math.isclose(2.005, 2.007))                                     #False
print("math.isclose(2.005, 2.007, abs_tol=0.01) :", math.isclose(2.005, 2.007, abs_tol=0.01))         #True
print("math.isclose(2.005, 2.017, abs_tol=0.01) :", math.isclose(2.005, 2.017, abs_tol=0.01))         #False
print("math.isclose(-2.005, -2.005) :", math.isclose(-2.005, -2.005))                                 #True
print("math.isclose(-2.005, -2.007) :", math.isclose(-2.005, -2.007))                                 #False
print("math.isclose(-2.005, -2.007, abs_tol=0.01) :", math.isclose(-2.005, -2.007, abs_tol=0.01))     #True
print("math.isclose(-2.005, -2.017, abs_tol=0.01) :", math.isclose(-2.005, -2.017, abs_tol=0.01))     #False
'''
11- math.isfinite(x)
Return True if x is neither an infinity nor a NaN, and False otherwise. (Note that 0.0 is considered finite.)
'''
print("math.isfinite(5) :", math.isfinite(5))                            #math.isfinite(5) : True
print("math.isfinite(-5) :", math.isfinite(-5))                          #math.isfinite(-5) : True
print("math.isfinite(math.inf) :", math.isfinite(math.inf))              #math.isfinite(math.inf) : False
print("math.isfinite(-math.inf) :", math.isfinite(-math.inf))            #math.isfinite(-math.inf) : False
print("math.isfinite(float('nan')) :", math.isfinite(float("nan")))      #math.isfinite(float('nan')) : False
print("math.isfinite(float('inf')) :", math.isfinite(float("inf")))      #math.isfinite(float('inf')) : False
print("math.isfinite(float('-inf')) :", math.isfinite(float("-inf")))    #math.isfinite(float('-inf')) : False
'''
12- math.isinf(x)
Return True if x is a positive or negative infinity, and False otherwise.
'''
print("math.isinf(5) :", math.isinf(5))                                  #math.isinf(5) : False
print("math.isinf(-5) :", math.isinf(-5))                                #math.isinf(-5) : False
print("math.isinf(math.inf) :", math.isinf(math.inf))                    #math.isinf(math.inf) : True
print("math.isinf(-math.inf) :", math.isinf(-math.inf))                  #math.isinf(-math.inf) : True
print("math.isinf(float('nan')) :", math.isinf(float("nan")))            #math.isinf(float('nan')) : False
print("math.isinf(float('inf')) :", math.isinf(float("inf")))            #math.isinf(float('inf')) : True
print("math.isinf(float('-inf')) :", math.isinf(float("-inf")))          #math.isinf(float('-inf')) : True
'''
13- math.isnan(x)
Return True if x is a NaN (not a number), and False otherwise.
'''
print("math.isnan(5) :", math.isnan(5))                                  #math.isnan(5) : False
print("math.isnan(-5) :", math.isnan(-5))                                #math.isnan(-5) : False
print("math.isnan(math.inf) :", math.isnan(math.inf))                    #math.isnan(math.inf) : False
print("math.isnan(-math.inf) :", math.isnan(-math.inf))                  #math.isnan(-math.inf) : False
print("math.isnan(float('nan')) :", math.isnan(float("nan")))            #math.isnan(float('nan')) : True
print("math.isnan(float('inf')) :", math.isnan(float("inf")))            #math.isnan(float('inf')) : False
print("math.isnan(float('-inf')) :", math.isnan(float("-inf")))          #math.isnan(float('-inf')) : False
'''
14- math.isqrt(n)
Return the integer square root of the nonnegative integer n. This is the floor of the exact square root of n, 
or equivalently the greatest integer a such that a² ≤ n.
For some applications, it may be more convenient to have the least integer a such that n ≤ a², 
or in other words the ceiling of the exact square root of n. 
For positive n, this can be computed using a = 1 + isqrt(n - 1).
'''
print("math.isqrt(100) :", math.isqrt(100))                              #math.isqrt(100) : 10
print("math.isqrt(10) :", math.isqrt(10))                                #math.isqrt(10) : 3
'''
15- math.frexp(x)
Return the mantissa and exponent of x as the pair (m, e). m is a float and e is an integer 
such that x == m * 2**e exactly. If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. 
This is used to “pick apart” the internal representation of a float in a portable way.
'''
print("math.frexp(3) :", math.frexp(3))                                  #math.frexp(3) : (0.75, 2)
print("math.frexp(-3) :", math.frexp(-3))                                #math.frexp(-3) : (-0.75, 2)
print("math.frexp(15.7) :", math.frexp(15.7))                            #math.frexp(15.7) : (0.98125, 4)
print("math.frexp(-15.7) :", math.frexp(-15.7))                          #math.frexp(-15.7) : (-0.98125, 4)
'''
16- math.ldexp(x, i)
Return x * (2**i). This is essentially the inverse of function frexp().
'''
print("math.ldexp(0.75, 2) :", math.ldexp(0.75, 2))                      #math.ldexp(0.75, 2) : 3
print("math.ldexp(-0.75, 2) :", math.ldexp(-0.75, 2))                    #math.ldexp(0.75, 2) : -3
print("math.ldexp(0.98, 4) :", math.ldexp(0.98, 4))                      #math.ldexp(0.98, 4) : 15.68
print("math.ldexp(-0.98, 4) :", math.ldexp(-0.98, 4))                    #math.ldexp(-0.98, 4) : -15.68
'''
17- math.modf(x)
Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
'''
print("math.modf(100.12) :", math.modf(100.12))                          #math.modf(100.12) : (0.12, 100.0)
print("math.modf(-25.5) :", math.modf(-25.5))                            #math.modf(-25.5) : (-0.5, -25.0)
'''
18- math.prod(iterable, *, start=1)
Calculate the product of all the elements in the input iterable. The default start value for the product is 1.
When the iterable is empty, return the start value. 
This function is intended specifically for use with numeric values and may reject non-numeric types.
'''
print("math.prod((0.5, 0.6, 0.7)) :", math.prod((0.5, 0.6, 0.7)))        #math.prod((0.5, 0.6, 0.7)) : 0.21
print("math.prod((5, 6, 7)) :", math.prod((5, 6, 7)))                    #math.prod((5, 6, 7)) : 210
print("math.prod([0.5, 0.6, 0.7]) :", math.prod([0.5, 0.6, 0.7]))        #math.prod([0.5, 0.6, 0.7]) : 0.21
print("math.prod([5, 6, 7]) :", math.prod([5, 6, 7]))                    #math.prod([5, 6, 7]) : 210
'''
19- math.fmod(x, y)
Return fmod(x, y), as defined by the platform C library. 
Note that the Python expression x % y may not return the same result. 
The intent of the C standard is that fmod(x, y) be exactly (mathematically; to infinite precision) 
equal to x - n*y for some integer n such that the result has the same sign as x and magnitude less than abs(y). 
Python’s x % y returns a result with the sign of y instead, and may not be exactly computable for float arguments. 
For example, fmod(-1e-100, 1e100) is -1e-100, but the result of Python’s -1e-100 % 1e100 is 1e100-1e-100, 
which cannot be represented exactly as a float, and rounds to the surprising 1e100. 
For this reason, function fmod() is generally preferred when working with floats, 
while Python’s x % y is preferred when working with integers.
'''
print("math.fmod(5, 2) :", math.fmod(5, 2))                              #math.fmod(5, 2) : 1.0
print("math.fmod(5, 1.5) :", math.fmod(5, 1.5))                          #math.fmod(5, 1.5) : 0.5
print("math.fmod(9.5, 3) :", math.fmod(9.5, 3))                          #math.fmod(9.5, 3) : 0.5
print("math.fmod(9.5, 3.5) :", math.fmod(9.5, 3.5))                      #math.fmod(9.5, 3.5) : 2.5
'''
20- math.remainder(x, y)
Return the IEEE 754-style remainder of x with respect to y. For finite x and finite nonzero y, 
this is the difference x - n*y, where n is the closest integer to the exact value of the quotient x / y. 
If x / y is exactly halfway between two consecutive integers, the nearest even integer is used for n. 
The remainder r = remainder(x, y) thus always satisfies abs(r) <= 0.5 * abs(y).
Special cases follow IEEE 754: in particular, remainder(x, math.inf) is x for any finite x, and remainder(x, 0) 
and remainder(math.inf, x) raise ValueError for any non-NaN x. If the result of the remainder operation is zero, 
that zero will have the same sign as x. On platforms using IEEE 754 binary floating-point, 
the result of this operation is always exactly representable: no rounding error is introduced.
'''
print("math.remainder(5, 2) :", math.remainder(5, 2))                    #math.remainder(5, 2) : 1.0
print("math.remainder(5, 1.5) :", math.remainder(5, 1.5))                #math.remainder(5, 1.5) : 0.5
print("math.remainder(9.5, 3) :", math.remainder(9.5, 3))                #math.remainder(9.5, 3) : 0.5
print("math.remainder(9.5, 3.5) :", math.remainder(9.5, 3.5))            #math.remainder(9.5, 3.5) : -1.0
'''
21- math.trunc(x)
Return the Real value x truncated to an Integral (usually an integer). Delegates to x.__trunc__().
Note that frexp() and modf() have a different call/return pattern than their C equivalents: 
they take a single argument and return a pair of values, 
rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).
For the ceil(), floor(), and modf() functions, 
note that all floating-point numbers of sufficiently large magnitude are exact integers. 
Python floats typically carry no more than 53 bits of precision (the same as the platform C double type), 
in which case any float x with abs(x) >= 2**52 necessarily has no fractional bits.
'''
print("math.trunc(15.2) :", math.trunc(15.2))                            #math.trunc(15.2) : 15
print("math.trunc(15.7) :", math.trunc(15.7))                            #math.trunc(15.7) : 15
print("math.trunc(-15.2) :", math.trunc(-15.2))                          #math.trunc(-15.2) : -15
print("math.trunc(-15.7) :", math.trunc(-15.7))                          #math.trunc(-15.7) : -15
'''
#Power and logarithmic functions
'''
'''
1- math.exp(x)
Return e raised to the power x, where e = 2.718281… is the base of natural logarithms. 
This is usually more accurate than math.e ** x or pow(math.e, x).
'''
print("math.exp(4) :", math.exp(4))                                      #math.exp(4) : 54.598150033144236
print("math.exp(-3) :", math.exp(-3))                                    #math.exp(-3) : 0.049787068367863944
print("math.exp(4.2) :", math.exp(4.2))                                  #math.exp(4.2) : 66.68633104092515
print("math.exp(-3.2) :", math.exp(-3.2))                                #math.exp(-3.2) : 0.04076220397836621
'''
2- math.expm1(x)
Return e raised to the power x, minus 1. Here e is the base of natural logarithms. For small floats x, 
the subtraction in exp(x) - 1 can result in a significant loss of precision
'''
print("math.expm1(4) :", math.expm1(4))                                  #math.expm1(4) : 53.598150033144236
print("math.expm1(-3) :", math.expm1(-3))                                #math.expm1(-3) : -0.950212931632136
print("math.expm1(4.2) :", math.expm1(4.2))                              #math.expm1(4.2) : 65.68633104092515
print("math.expm1(-3.2) :", math.expm1(-3.2))                            #math.expm1(-3.2) : -0.9592377960216338
'''
3- math.log(x[, base])
With one argument, return the natural logarithm of x (to base e).
With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
'''
print("math.log(math.e) :", math.log(math.e))                            #math.log(math.e) : 1.0
print("math.log(math.e ** 2) :", math.log(math.e ** 2))                  #math.log(math.e ** 2) : 2.0
print("math.log(11) :", math.log(11))                                    #math.log(11) : 2.3978952727983707
print("math.log(10, 10) :", math.log(10, 10))                            #math.log(10, 10) : 1.0
print("math.log(100, 10) :", math.log(100, 10))                          #math.log(100, 10) : 2.0
print("math.log(150, 10) :", math.log(150, 10))                          #math.log(150, 10) : 2.176091259055681
print("math.log(64, 2) :", math.log(64, 2))                              #math.log(64, 2) : 6.0
print("math.log(35, 2) :", math.log(35, 2))                              #math.log(35, 2) : 5.129283016944966
print("math.log(125, 5) :", math.log(125, 5))                            #math.log(125, 5) : 3.0000000000000004
'''
4- math.log1p(x)
Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.
'''
print("math.log1p(math.e - 1) :", math.log1p(math.e - 1))                #math.log1p(math.e - 1) : 1.0
print("math.log1p(math.e**2 - 1) :", math.log1p(math.e**2 - 1))          #math.log1p(math.e**2 - 1) : 2.0
print("math.log1p(10) :", math.log1p(10))                                #math.log1p(10) : 2.3978952727983707
print("math.log1p(5) :", math.log1p(5))                                  #math.log1p(5) : 1.791759469228055
'''
5- math.log2(x)
Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).
'''
print("math.log2(64) :", math.log2(64))                                  #math.log2(64) : 6.0
print("math.log2(35) :", math.log2(35))                                  #math.log2(35) : 5.129283016944966
'''
6- math.log10(x)
Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
'''
print("math.log10(10) :", math.log10(10))                                #math.log10(10) : 1.0
print("math.log10(100) :", math.log10(100))                              #math.log10(100) : 2.0
print("math.log10(150) :", math.log10(150))                              #math.log10(150) : 2.176091259055681
'''
7- math.pow(x, y)
Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. 
If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
Unlike the built-in ** operator, math.pow() converts both its arguments to type float. 
Use ** or the built-in pow() function for computing exact integer powers.
'''
print("math.pow(10, 2) :", math.pow(10, 2))                              #math.pow(10, 2) : 100.0
print("math.pow(10, -2) :", math.pow(10, -2))                            #math.pow(10, -2) : 0.01
print("math.pow(-2, 4) :", math.pow(-2, 4))                              #math.pow(-2, 4) : 16.0
print("math.pow(-3, -1) :", math.pow(-3, -1))                            #math.pow(-3, -1) : -0.3333333333333333
'''
8- math.sqrt(x)
Return the square root of x.
'''
print("math.sqrt(0) :", math.sqrt(0))                                    #math.sqrt(0) : 0.0
print("math.sqrt(4) :", math.sqrt(4))                                    #math.sqrt(4) : 2.0
print("math.sqrt(14.5) :", math.sqrt(14.5))                              #math.sqrt(14.5) : 3.8078865529319543
'''
#Angular conversion
'''
'''
1- math.degrees(x)
Convert angle x from radians to degrees.
'''
print("math.degrees(0) :", math.degrees(0))                              #math.degrees(0) : 0.0
print("math.degrees(math.pi/6) :", math.degrees(math.pi/6))              #math.sin(math.pi/6) : 30.0
print("math.degrees(math.pi/4) :", math.degrees(math.pi/4))              #math.sin(math.pi/4) : 45.0
print("math.degrees(math.pi/3) :", math.degrees(math.pi/3))              #math.sin(math.pi/3) : 60.0
print("math.degrees(math.pi/2) :", math.degrees(math.pi/2))              #math.degrees(math.pi/2) : 90.0
print("math.degrees(math.pi) :", math.degrees(math.pi))                  #math.degrees(math.pi) : 180.0
print("math.degrees(3*math.pi/2) :", math.degrees(3*math.pi/2))          #math.degrees(3*math.pi/2) : 270.0
print("math.degrees(2*math.pi) :", math.degrees(2*math.pi))              #math.degrees(2*math.pi) : 360.0
'''
2- math.radians(x)
Convert angle x from degrees to radians.
'''
print("math.radians(0) :", math.radians(0))                              #math.radians(0) : 0.0
print("math.radians(30) :", math.radians(30))                            #math.radians(30) : 0.5235987755982988
print("math.radians(45) :", math.radians(45))                            #math.radians(45) : 0.7853981633974483
print("math.radians(60) :", math.radians(60))                            #math.radians(60) : 1.0471975511965976
print("math.radians(90) :", math.radians(90))                            #math.radians(90) : 1.5707963267948966
print("math.radians(180) :", math.radians(180))                          #math.radians(180) : 3.141592653589793
print("math.radians(270) :", math.radians(270))                          #math.radians(270) : 4.71238898038469
print("math.radians(360) :", math.radians(360))                          #math.radians(360) : 6.283185307179586
'''    
#Trigonometric functions    
'''    
'''    
1- math.sin(x)    
Return the sine of x radians.    
'''    
print("math.sin(0) :", math.sin(0))                                      #math.sin(0) : 0.0
print("math.sin(math.pi/6) :", math.sin(math.pi/6))                      #math.sin(math.pi/6) : 0.49999999999999994
print("math.sin(math.pi/4) :", math.sin(math.pi/4))                      #math.sin(math.pi/4) : 0.7071067811865475
print("math.sin(math.pi/3) :", math.sin(math.pi/3))                      #math.sin(math.pi/3) : 0.8660254037844386
print("math.sin(math.pi/2) :", math.sin(math.pi/2))                      #math.sin(math.pi/2) : 1.0
print("math.sin(math.pi) :", math.sin(math.pi))                          #math.sin(math.pi) : 0.0
print("math.sin(3*math.pi/2) :", math.sin(3*math.pi/2))                  #math.sin(3*math.pi/2) : -1.0
print("math.sin(2*math.pi) :", math.sin(2*math.pi))                      #math.sin(2*math.pi) : 0.0
'''
2- math.cos(x)
Return the cosine of x radians.
'''
print("math.cos(0) :", math.cos(0))                                      #math.cos(0) : 1.0
print("math.cos(math.pi/6) :", math.cos(math.pi/6))                      #math.cos(math.pi/6) : 0.8660254037844387
print("math.cos(math.pi/4) :", math.cos(math.pi/4))                      #math.cos(math.pi/4) : 0.7071067811865476
print("math.cos(math.pi/3) :", math.cos(math.pi/3))                      #math.cos(math.pi/3) : 0.5000000000000001
print("math.cos(math.pi/2) :", math.cos(math.pi/2))                      #math.cos(math.pi/2) : 0.0
print("math.cos(math.pi) :", math.cos(math.pi))                          #math.cos(math.pi) : -1.0
print("math.cos(3*math.pi/2) :", math.cos(3*math.pi/2))                  #math.cos(3*math.pi/2) : 0.0
print("math.cos(2*math.pi) :", math.cos(2*math.pi))                      #math.cos(2*math.pi) : 1.0
'''    
3- math.tan(x)    
Return the tangent of x radians.    
'''    
print("math.tan(-math.pi/2) :", math.tan(-math.pi/2))                    #math.tan(-math.pi/2) : -inf
print("math.tan(-math.pi/3) :", math.tan(-math.pi/3))                    #math.tan(-math.pi/3) : -1.7320508075688767
print("math.tan(-math.pi/4) :", math.tan(-math.pi/4))                    #math.tan(-math.pi/4) : -0.9999999999999999
print("math.tan(-math.pi/6) :", math.tan(-math.pi/6))                    #math.tan(-math.pi/6) : -0.5773502691896257
print("math.tan(0) :", math.tan(0))                                      #math.tan(0) : 0.0
print("math.tan(math.pi/6) :", math.tan(math.pi/6))                      #math.tan(math.pi/6) : 0.5773502691896257
print("math.tan(math.pi/4) :", math.tan(math.pi/4))                      #math.tan(math.pi/4) : 0.9999999999999999
print("math.tan(math.pi/3) :", math.tan(math.pi/3))                      #math.tan(math.pi/3) : 1.7320508075688767
print("math.tan(math.pi/2) :", math.tan(math.pi/2))                      #math.tan(math.pi/2) : inf
'''
4- math.asin(x)
Return the arc sine of x, in radians.
'''
print("math.asin(-1) :", math.asin(-1))                                  #math.asin(-1) : -1.5707963267948966
print("math.asin(-0.8) :", math.asin(-0.8))                              #math.asin(-0.8) : -0.9272952180016123
print("math.asin(-0.6) :", math.asin(-0.6))                              #math.asin(-0.6) : -0.6435011087932844
print("math.asin(-0.4) :", math.asin(-0.4))                              #math.asin(-0.4) : -0.41151684606748806
print("math.asin(-0.2) :", math.asin(-0.2))                              #math.asin(-0.2) : -0.2013579207903308
print("math.asin(0) :", math.asin(0))                                    #math.asin(0) : 0.0
print("math.asin(0.2) :", math.asin(0.2))                                #math.asin(0.2) : 0.2013579207903308
print("math.asin(0.4) :", math.asin(0.4))                                #math.asin(0.4) : 0.41151684606748806
print("math.asin(0.6) :", math.asin(0.6))                                #math.asin(0.6) : 0.6435011087932844
print("math.asin(0.8) :", math.asin(0.8))                                #math.asin(0.8) : 0.9272952180016123
print("math.asin(1) :", math.asin(1))                                    #math.asin(1) : 1.5707963267948966
'''    
5- math.acos(x)    
Return the arc cosine of x, in radians.    
'''    
print("math.acos(-1) :", math.acos(-1))                                  #math.acos(-1) : 3.141592653589793
print("math.acos(-0.8) :", math.acos(-0.8))                              #math.acos(-0.8) : 2.498091544796509
print("math.acos(-0.6) :", math.acos(-0.6))                              #math.acos(-0.6) : 2.214297435588181
print("math.acos(-0.4) :", math.acos(-0.4))                              #math.acos(-0.4) : 1.9823131728623846
print("math.acos(-0.2) :", math.acos(-0.2))                              #math.acos(-0.2) : 1.7721542475852274
print("math.acos(0) :", math.acos(0))                                    #math.acos(0) : 1.5707963267948966
print("math.acos(0.2) :", math.acos(0.2))                                #math.acos(0.2) : 1.369438406004566
print("math.acos(0.4) :", math.acos(0.4))                                #math.acos(0.4) : 1.1592794807274085
print("math.acos(0.6) :", math.acos(0.6))                                #math.acos(0.6) : 0.9272952180016123
print("math.acos(0.8) :", math.acos(0.8))                                #math.acos(0.8) : 0.6435011087932843
print("math.acos(1) :", math.acos(1))                                    #math.acos(1) : 0.0
'''
6- math.atan(x)
Return the arc tangent of x, in radians.
'''
print("math.atan(math.inf) :", math.atan(math.inf))                      #math.atan(math.inf) : 1.5707963267948966
print("math.atan(-1) :", math.atan(-1))                                  #math.atan(-1) : -0.7853981633974483
print("math.atan(-0.8) :", math.atan(-0.8))                              #math.atan(-0.8) : -0.6747409422235527
print("math.atan(-0.6) :", math.atan(-0.6))                              #math.atan(-0.6) : -0.5404195002705842
print("math.atan(-0.4) :", math.atan(-0.4))                              #math.atan(-0.4) : -0.3805063771123649
print("math.atan(-0.2) :", math.atan(-0.2))                              #math.atan(-0.2) : -0.19739555984988078
print("math.atan(0) :", math.atan(0))                                    #math.atan(0) : 0.0
print("math.atan(0.2) :", math.atan(0.2))                                #math.atan(0.2) : 0.19739555984988078
print("math.atan(0.4) :", math.atan(0.4))                                #math.atan(0.4) : 0.3805063771123649
print("math.atan(0.6) :", math.atan(0.6))                                #math.atan(0.6) : 0.5404195002705842
print("math.atan(0.8) :", math.atan(0.8))                                #math.atan(0.8) : 0.6747409422235527
print("math.atan(1) :", math.atan(1))                                    #math.atan(1) : 0.7853981633974483
print("math.atan(-math.inf) :", math.atan(-math.inf))                    #math.atan(-math.inf) : -1.5707963267948966
'''
7- math.atan2(y, x)
Return atan(y / x), in radians. The result is between -pi and pi. 
The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. 
The point of atan2() is that the signs of both inputs are known to it, 
so it can compute the correct quadrant for the angle. 
For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
'''
print("math.atan2(1.2, 1.5) :", math.atan2(1.2, 1.5))                    #math.atan2(1.2, 1.5) : 0.6747409422235526
print("math.atan2(-1.2, -1.5) :", math.atan2(-1.2, -1.5))                #math.atan2(-1.2, -1.5) : -2.4668517113662407
print("math.atan2(1.2, -1.5) :", math.atan2(1.2, -1.5))                  #math.atan2(1.2, -1.5) : 2.4668517113662407
print("math.atan2(-1.2, 1.5) :", math.atan2(-1.2, 1.5))                  #math.atan2(-1.2, 1.5) : -0.6747409422235526
'''
8- math.dist(p, q)
Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates. 
The two points must have the same dimension.
'''
print("math.dist([4, 7], [1, 3]) :", math.dist([4, 7], [1, 3]))                    #math.dist([4, 7], [1, 3]) : 5.0
print("math.dist([4, 7, 0], [1, 3, 0]) :", math.dist([4, 7, 0], [1, 3, 0]))        #math.dist([4, 7, 0], [1, 3, 0]) : 5.0
'''
9- math.hypot(*coordinates)
Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)). 
This is the length of the vector from the origin to the point given by the coordinates.
For a two dimensional point (x, y), this is equivalent to computing the hypotenuse of a right triangle 
using the Pythagorean theorem, sqrt(x*x + y*y).
Changed in version 3.8: Added support for n-dimensional points. Formerly, only the two dimensional case was supported.
'''
print("math.hypot(-3, 4) :", math.hypot(-3, 4))                          #math.hypot(-3, 4) : 5.0
print("math.hypot(12, 9) :", math.hypot(12, 9))                          #math.hypot(12, 9) : 15.0
'''
#Hyperbolic functions
'''
'''
1- math.acosh(x)
Return the inverse hyperbolic cosine of x.
'''

'''
2- math.asinh(x)
Return the inverse hyperbolic sine of x.
'''

'''
3- math.atanh(x)
Return the inverse hyperbolic tangent of x.
'''

'''
4- math.cosh(x)
Return the hyperbolic cosine of x.
'''

'''
5- math.sinh(x)
Return the hyperbolic sine of x.
'''

'''
6- math.tanh(x)
Return the hyperbolic tangent of x.
'''

