## Python Tutorial
### Build-in Types

Numeric types:

int
>Plain integers (also just called integers) are implemented using long in C, which gives them at least 32 bits of precision (sys.maxint is always set to the maximum plain integer value for the current platform, the minimum value is -sys.maxint - 1)

float
>Floating point numbers are usually implemented using double in C;

>Numeric literals containing a decimal point or an exponent sign yield floating point numbers.

long
>Long integers have unlimited precision.

>Integer literals with an 'L' or 'l' suffix yield long integers 

complex
>Complex numbers have a real and imaginary part, which are each a floating point number. To extract these parts from a complex number z, use z.real and z.imag.

>Appending 'j' or 'J' to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts.

```
a / b vs a // b
>>> 8//3.0
2.0
>>> 8/3.0
2.6666666666666665

divmod(x, y) = (x//y, x%y)
pow(x, y) = x**y

math.trunc(x) : take the integer part
round(x[, n]) : x rounded to n digits, n = 0 by default
math.floor(x) : the greatest integer as a float <= x
math.ceil(x)  : the least integer as a float >= x
```

Bitwise Operations:

Bitwise operations only make sense for integers.

```
~a = -a-1
Example:
~2 = -3
~(-3) = 2 
```

set vs frozenset:
>There are currently two built-in set types, set and frozenset.

>The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set.

>The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.

Class attributes vs Instance attributes:
> If we try to change class variable using object, a new instance (or non-static) variable for that particular object is created and this variable shadows the class variables.

### Build In functions
 
enumerate(sequence, start=0)

```python
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```


### Control Flow Tools

if statement

```python
if condition1:
	...
elif condition2:
	...
elif condition3:
	...
else:
	...
```

Unpacking argument Lists:

```python
def unpack_arguments(argument, *argumentList, **argumentDict):
	print "argument:", argument
	for arg in argumentList:
		print arg
	for key,value in argumentDict.items():
		print "%s : %s"%(key, value)
```

#### iterable


>An object capable of returning its members one at a time. 

>Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict and file and objects of any classes you define with an __iter__() or __getitem__() method.

>Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …).

>When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values.

>When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop.


#### iterator


>An object representing a stream of data.

>Repeated calls to the iterator’s next() method return successive items in the stream. When no more data are available a StopIteration exception is raised instead.

>At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. 

>Iterators are required to have an __iter__() method that returns the iterator object itself.

#### Class method vs Static Method

Class Method:
>A class method receives the class as implicit first argument

>It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

>If a class method is called for a derived class, the derived class object is passed as the implied first argument.

```python
class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
```

Static Method:
>A static method does not receive an implicit first argument.

>It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

```python
class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
```

Class method vs Static method:
>A class method takes cls as first parameter while a static method needs no specific parameters.

>A class method can access or modify class state while a static method can’t access or modify it.

>In general, static methods know nothing about class state. They are utility type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as parameter.

#### Decorator

```python
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

def example(a, b, *args, **kwargs):
    print "executed function example with args %s %s %s %s"%(a, b, args, kwargs)
```

### Errors and Exceptions

Example:

```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs. And an error here would NOT be caught
# This would be printed in every case.
```

#### Else Clause of For loop

for loops also have an else clause: The else clause executes after the loop completes normally.

```python
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```


Build in Exception:

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
	   +-- ImportWarning
	   +-- UnicodeWarning
	   +-- BytesWarning
```

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
```

