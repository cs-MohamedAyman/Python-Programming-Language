'''
This module implements pseudo-random number generators for various distributions.
For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, 
a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, 
gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.
Almost all module functions depend on the basic function random(), which generates a random float uniformly 
in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. 
It produces 53-bit precision floats and has a period of 2**19937-1. 
The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of 
the most extensively tested random number generators in existence. However, being completely deterministic, 
it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.
The functions supplied by this module are actually bound methods of a hidden instance of the random. 
Random class. You can instantiate your own instances of Random to get generators that don’t share state.
'''
import random    
'''
#Bookkeeping functions
'''
'''
1- random.seed(a=None, version=2)
Initialize the random number generator.
If a is omitted or None, the current system time is used. 
If randomness sources are provided by the operating system, they are used instead of the system time 
(see the os.urandom() function for details on availability).
If a is an int, it is used directly.
'''
random.seed(5)
'''
2- random.getrandbits(k)
Returns a Python integer with k random bits. This method is supplied with the Mersenne Twister generator 
and some other generators may also provide it as an optional part of the API. When available, getrandbits() 
enables randrange() to handle arbitrarily large ranges.
'''
print("random.getrandbits(1) :", random.getrandbits(1))							#random.getrandbits(1) : 0
print("random.getrandbits(1) :", random.getrandbits(1))							#random.getrandbits(1) : 1
print("random.getrandbits(2) :", random.getrandbits(2))							#random.getrandbits(2) : 2
print("random.getrandbits(2) :", random.getrandbits(2))							#random.getrandbits(2) : 0
print("random.getrandbits(3) :", random.getrandbits(3))							#random.getrandbits(3) : 7
print("random.getrandbits(3) :", random.getrandbits(3))							#random.getrandbits(3) : 3
print("random.getrandbits(6) :", random.getrandbits(6))							#random.getrandbits(6) : 57
print("random.getrandbits(6) :", random.getrandbits(6))							#random.getrandbits(6) : 48
print("random.getrandbits(6) :", random.getrandbits(6))							#random.getrandbits(6) : 22
print("random.getrandbits(6) :", random.getrandbits(6))							#random.getrandbits(6) : 6
'''
#Functions for integers
'''
'''
1- random.randrange(stop)
random.randrange(start, stop[, step])
Return a randomly selected element from range(start, stop, step). 
This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
The positional argument pattern matches that of range(). 
Keyword arguments should not be used because the function may use them in unexpected ways.
'''
print("random.randrange(3) :", random.randrange(3)) 							#random.randrange(3) : 0 
print("random.randrange(3) :", random.randrange(3)) 							#random.randrange(3) : 1 
print("random.randrange(3) :", random.randrange(3)) 							#random.randrange(3) : 2 
print("random.randrange(3) :", random.randrange(3)) 							#random.randrange(3) : 0 
print("random.randrange(12, 15) :", random.randrange(12, 15)) 					#random.randrange(12, 15) : 14
print("random.randrange(12, 15) :", random.randrange(12, 15)) 					#random.randrange(12, 15) : 13
print("random.randrange(12, 15) :", random.randrange(12, 15)) 					#random.randrange(12, 15) : 12
print("random.randrange(12, 15) :", random.randrange(12, 15)) 					#random.randrange(12, 15) : 13
print("random.randrange(22, 28, 2) :", random.randrange(22, 28, 2)) 			#random.randrange(22, 28, 2) : 26
print("random.randrange(22, 28, 2) :", random.randrange(22, 28, 2)) 			#random.randrange(22, 28, 2) : 22
print("random.randrange(22, 28, 2) :", random.randrange(22, 28, 2)) 			#random.randrange(22, 28, 2) : 24
print("random.randrange(22, 28, 2) :", random.randrange(22, 28, 2)) 			#random.randrange(22, 28, 2) : 26
print("random.randrange(28, 22, -1) :", random.randrange(28, 22, -1)) 			#random.randrange(28, 22, -1) : 23
print("random.randrange(28, 22, -1) :", random.randrange(28, 22, -1)) 			#random.randrange(28, 22, -1) : 23
print("random.randrange(28, 22, -1) :", random.randrange(28, 22, -1)) 			#random.randrange(28, 22, -1) : 26
print("random.randrange(28, 22, -1) :", random.randrange(28, 22, -1)) 			#random.randrange(28, 22, -1) : 28
'''
2- random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
'''
print("random.randint(0, 3) :", random.randint(0, 3))							#random.randint(0, 3) : 1
print("random.randint(0, 3) :", random.randint(0, 3))							#random.randint(0, 3) : 3
print("random.randint(0, 3) :", random.randint(0, 3))							#random.randint(0, 3) : 2
print("random.randint(0, 3) :", random.randint(0, 3))							#random.randint(0, 3) : 0
'''
#Functions for sequences
'''
'''
1- random.choice(seq)
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
'''
print("random.choice([5, -3.2, 'abc']) :", random.choice([5, -3.2, 'abc']))		#random.choice([5, -3.2, 'abc']) : -3.2
print("random.choice([5, -3.2, 'abc']) :", random.choice([5, -3.2, 'abc']))		#random.choice([5, -3.2, 'abc']) : 5
print("random.choice((5, -3.2, 'abc')) :", random.choice((5, -3.2, 'abc')))		#random.choice((5, -3.2, 'abc')) : abc
print("random.choice((5, -3.2, 'abc')) :", random.choice((5, -3.2, 'abc')))		#random.choice((5, -3.2, 'abc')) : 5
'''
2- random.choices(population, weights=None, *, cum_weights=None, k=1)
Return a k sized list of elements chosen from the population with replacement. 
If the population is empty, raises IndexError.
If a weights sequence is specified, selections are made according to the relative weights. 
Alternatively, if a cum_weights sequence is given, the selections are made according to the cumulative weights 
(perhaps computed using itertools.accumulate()). 
For example, the relative weights [10, 5, 30, 5] are equivalent to the cumulative weights [10, 15, 45, 50]. 
Internally, the relative weights are converted to cumulative weights before making selections, 
so supplying the cumulative weights saves work.
If neither weights nor cum_weights are specified, selections are made with equal probability. 
If a weights sequence is supplied, it must be the same length as the population sequence. 
It is a TypeError to specify both weights and cum_weights.
The weights or cum_weights can use any numeric type that interoperates with the float values returned by random() 
(that includes integers, floats, and fractions but excludes decimals). Weights are assumed to be non-negative.
For a given seed, the choices() function with equal weighting typically produces a different sequence 
than repeated calls to choice(). The algorithm used by choices() uses floating point arithmetic 
for internal consistency and speed. The algorithm used by choice() defaults to integer arithmetic 
with repeated selections to avoid small biases from round-off error.
'''
print(random.choices(['a', 'b', 'c'], [6, 1.5, 2.5], k=10))			#['c', 'a', 'b', 'a', 'a', 'c', 'a', 'a', 'a', 'c']
print(random.choices(['a', 'b', 'c'], [6, 1.5, 2.5], k=10))			#['c', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'c', 'a']
print(random.choices(['a', 'b', 'c'], [6, 1.5, 2.5], k=10))			#['a', 'a', 'a', 'c', 'a', 'c', 'a', 'a', 'b', 'a']
print(random.choices(['a', 'b', 'c'], [6, 1.5, 2.5], k=10))			#['a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'c', 'a']
'''
3- random.shuffle(x[, random])
Shuffle the sequence x in place.
The optional argument random is a 0-argument function returning a random float in [0.0, 1.0); 
by default, this is the function random().
To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.
Note that even for small len(x), the total number of permutations of x can quickly grow larger than 
the period of most random number generators. This implies that most permutations of a long sequence can never 
be generated. For example, a sequence of length 2080 is the largest that can fit within the period of 
the Mersenne Twister random number generator.
'''
x = ['b', 'a', 3.5]
random.shuffle(x)
print(x)						#['a', 3.5, 'b']
random.shuffle(x)
print(x)						#[3.5, 'a', 'b']
random.shuffle(x)
print(x)						#[3.5, 'a', 'b']
random.shuffle(x)
print(x)						#['a', 3.5, 'b']
'''
4- random.sample(population, k)
Return a k length list of unique elements chosen from the population sequence or set. 
Used for random sampling without replacement.
Returns a new list containing elements from the population while leaving the original population unchanged. 
The resulting list is in selection order so that all sub-slices will also be valid random samples. 
This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).
Members of the population need not be hashable or unique. If the population contains repeats, 
then each occurrence is a possible selection in the sample.
To choose a sample from a range of integers, use a range() object as an argument. 
This is especially fast and space efficient for sampling from a large population: sample(range(10000000), k=60).
If the sample size is larger than the population size, a ValueError is raised.
'''
print(random.sample([5.2, 2, 1.6, 4, -5], 3)) 							#[-5, 1.6, 2]
print(random.sample([5.2, 2, 1.6, 4, -5], 3)) 							#[5.2, -5, 4]
print(random.sample([5.2, 2, 1.6, 4, -5], 3)) 							#[2, -5, 1.6]
print(random.sample([5.2, 2, 1.6, 4, -5], 3)) 							#[5.2, 1.6, 2]
'''
#Real-valued distributions
The following functions generate specific real-valued distributions. 
Function parameters are named after the corresponding variables in the distribution’s equation, 
as used in common mathematical practice; most of these equations can be found in any statistics text.
'''
'''
1- random.random()
Return the next random floating point number in the range [0.0, 1.0).
'''
print("random.random() :", random.random()) 							#random.random() : 0.13643821384653154
print("random.random() :", random.random()) 							#random.random() : 0.5808364090140392
print("random.random() :", random.random()) 							#random.random() : 0.7880128089993633
print("random.random() :", random.random()) 							#random.random() : 0.30273604106811236
'''
2- random.uniform(a, b)
Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
The end-point value b may or may not be included in the range depending on floating-point 
rounding in the equation a + (b-a) * random().
'''
print("random.uniform(3, 5) :", random.uniform(3, 5)) 					#random.uniform(3, 5) : 4.849814175620888
print("random.uniform(3, 5) :", random.uniform(3, 5)) 					#random.uniform(3, 5) : 4.249325992783081
print("random.uniform(3, 5) :", random.uniform(3, 5)) 					#random.uniform(3, 5) : 3.4934536146666026
print("random.uniform(3, 5) :", random.uniform(3, 5)) 					#random.uniform(3, 5) : 3.0400059289682564
'''
3- random.triangular(low, high, mode)
Return a random floating point number N such that low <= N <= high and with 
the specified mode between those bounds. The low and high bounds default to zero and one. 
The mode argument defaults to the midpoint between the bounds, giving a symmetric distribution.
'''
print("random.triangular(5, 20, 18) :", random.triangular(5, 20, 18)) 	#random.triangular(5, 20, 18) : 9.12119697527266
print("random.triangular(5, 20, 18) :", random.triangular(5, 20, 18))   #random.triangular(5, 20, 18) : 15.051128394436743
print("random.triangular(5, 20, 18) :", random.triangular(5, 20, 18))   #random.triangular(5, 20, 18) : 15.831803304486217
print("random.triangular(5, 20, 18) :", random.triangular(5, 20, 18))   #random.triangular(5, 20, 18) : 17.014855771945996
print("random.triangular(5, 20, 7) :", random.triangular(5, 20, 7))     #random.triangular(5, 20, 7) : 8.021484983799377
print("random.triangular(5, 20, 7) :", random.triangular(5, 20, 7))     #random.triangular(5, 20, 7) : 8.461733959079835
print("random.triangular(5, 20, 7) :", random.triangular(5, 20, 7))     #random.triangular(5, 20, 7) : 9.579946520047496
print("random.triangular(5, 20, 7) :", random.triangular(5, 20, 7))     #random.triangular(5, 20, 7) : 14.17509040921485
'''
4- random.betavariate(alpha, beta)
Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.
'''

'''
5- random.expovariate(lambd)
Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero. 
(The parameter would be called “lambda”, but that is a reserved word in Python.) 
Returned values range from 0 to positive infinity if lambd is positive, 
and from negative infinity to 0 if lambd is negative.
'''

'''
6- random.gammavariate(alpha, beta)
Gamma distribution. (Not the gamma function!) Conditions on the parameters are alpha > 0 and beta > 0.
The probability distribution function is:
          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha
'''

'''
7- random.gauss(mu, sigma)
Gaussian distribution. mu is the mean, and sigma is the standard deviation. 
This is slightly faster than the normalvariate() function defined below.
'''

'''
8- random.lognormvariate(mu, sigma)
Log normal distribution. If you take the natural logarithm of this distribution, 
you’ll get a normal distribution with mean mu and standard deviation sigma. 
mu can have any value, and sigma must be greater than zero.
'''

'''
9- random.normalvariate(mu, sigma)
Normal distribution. mu is the mean, and sigma is the standard deviation.
'''

'''
10- random.vonmisesvariate(mu, kappa)
mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, 
which must be greater than or equal to zero. If kappa is equal to zero, 
this distribution reduces to a uniform random angle over the range 0 to 2*pi.
'''

'''
11- random.paretovariate(alpha)
Pareto distribution. alpha is the shape parameter.
'''

'''
12- random.weibullvariate(alpha, beta)
Weibull distribution. alpha is the scale parameter and beta is the shape parameter.
'''

'''
#Notes on Reproducibility
Sometimes it is useful to be able to reproduce the sequences given by a pseudo random number generator. 
By re-using a seed value, the same sequence should be reproducible from run to 
run as long as multiple threads are not running.
Most of the random module’s algorithms and seeding functions are subject to change across Python versions, 
but two aspects are guaranteed not to change:
If a new seeding method is added, then a backward compatible seeder will be offered.
The generator’s random() method will continue to produce the same sequence 
when the compatible seeder is given the same seed.
'''
