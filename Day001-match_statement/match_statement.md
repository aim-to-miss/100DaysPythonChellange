# `match` Statement
> `match` Statement checks for an object, and takes decisions base on consecutive outcome.

`match` takes a subject, and after that it tries to match with some patterns. Patterns can be literal values, guard and also unpacking. It executes the first matched `case`. A simple `match` statement syntax:
```python3
match subject
    case var1:
        statement
    case var2:
        statement

```

> The `_` variable is a wildcard. It never fails. If none of the case executes, It will.

You can combine multiple literals in one `case`. For this you need to add `|` between the literals.
```python3
match subject
    case var1:
        statement
    case var2 | var3:
        statement
```
```python3
def matchMe(val):
    match val:
        case 404:
            print("Sorry! No Resource found.")
        case "Winner":
            print("Congratulations!")
        case "Rose" | "Lily" | "Sunflower" as flower:
            print("Great! I like ", flower)
        case _:
            print("If nothing matches! Still there is hope.")
cases = [
        404,
        "Loser",
        "Rose",
        70
        ]
for case in cases:
    matchMe(case)
```
Of-course you can write multiline statement in each case statement. Teat it as like a normal code block. We also can capture the value of the literal or element using the `as` keyword. The value than can be used in the scope of the case statement.
```python3
match subject
    case var1:
        statement
    case var2 | var3 as var:
        print(var)
```
If a conditional statement is needed apart form the case, you can add that. the syntax will be: 

```python3
match subject
    case var1 if condition:
        statement
    case var2 | var3 as var:
        print(var)
```
```python3
def matchMe(val):
    requestSent = True
    match val:
        case 200 if requestSent:
            print("Tada!! Hello world.")
        case "Rose" | "Lily" | "Sunflower" as flower:
            print("Great! I like ", flower)
        case _:
            print("If nothing matches! Still there is hope.")
cases = [
    200,
    "Winner",
    "Rose"
    ]
for case in cases:
    matchMe(case)
```

Pattern matching for `case` also support unpacking assignments and dynamic binding. lets say I have a tuple `t=(x,y)` where, `x` abd `y` is variable. if I assign the value like this, `x,y=5,6` than the tuple `t` now look like this `(5,6)`. Similarly pattern matching in `case` takes value from `match` unpack the values and bind them dynamically. check the code below:
```python3
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```
You can do do a lot of things when it's comes for data structure. `case (1,2,3,4)` exactly matches `(1,2,3,4)`. On the other hand you can expect any of multiple values in position 2, you also can do that. take this as an example, `case (1, (2,3,4),5)` will match `(1,2,5)`, `(1,4,5)`, `(1,3,5)`. How about you don't care about the second value at all, well `case (1,_,5)` will not care about what is in the 2nd position at all, it will match say `(1,100,5)` or even `(1,"OMG",5)`. You can also easily capture the value if you want with `as` keyword `case (1,2, _ as val)` Funny right? Let's dive deep. Let's say you are not sure about the length of the "I don't care" values. No worries. `case (1, *other, 4)` will match anything that comes in the middle, I mean anything with any length, ofcourse except `4`. It will even match this `(1,"OMG", "I", "am", "rich", [1,2,3],4)`. And you should not worry about the position also, `*other` can be any position, `case (1,2,*others)` can also be a pattern if you not sure/care about the items after `2` or the number of items.
```python3
def matchMe(val):
    match val:
        case (0,0):
            print("Its the center.")
        case (0,y):
            print("Horizontal line with distance: ", y)
        case (x, 0):
            print("Vertical line with distance: ", x)
        case (x,y):
            print("Diagonal line with slop: ", x,y)
        case (1,2,3,4):
            print("I am just a boring tuple.")
        case (1, (2|3) as val, 4):
            print("I am not that boring. I can get Dynamic value, now I am holding: ", val)
        case (1, *others, 4):
            print("I am more dynamic, I got a whole list of others. ", others)
        case (1, 4, *others):
            print("I am also dynamic with different position. I got ", others)
        case val if val< 100:
            print("The initial journey is hard.")
        case _:
            print("If nothing matches! Still there is hope.")
cases = [
    (0,0),
    (5,0),
    (7,9),
    (1,2,3,4),
    (1,2,4),
    (1,3,4),
    (1,"OMG",4),
    (1,"OMG", "I", "am", "rich", [1,2,3],4),
    (1,4,"OMG", "I", "am", "rich", [1,2,3])
    ]
for case in cases:
    matchMe(case)
```
> Don't take `other` word as granted . It's just a name that looks good. You can use anything but python dedicated keywords. You can name as `*IDK`, `*YourName`, `*dog`, `*yourEx`. Can't be more creative than that. You can text your wife like this: Hy love! Check the only pattern that matches me - `case (you, ourDaughter, ourSon, *MyEx's)` 

Enough with the tuple, let's take with a tour with dictionary, shall we?
Ok, yes of course case can match patters for dictionary. Lets take an example dictionary: `{1: 'val1', 2: 'val2', 3: 'val3'}`. One thing to note for dictionary is that it does not consider the exact match of the pattern and case. If any number of items of the matching dictionary have all the items defined in `case` then the case will be matched. So if `case {1: 'val1', 2: 'val2'}` is a case than `{1: 'val1', 2: 'val2'}` will match that case, so does `{1: 'val1', 2: 'val2', 3: 'val3'}`. Also the order also does not matter. I mean `{1: 'val1', 3: 'val3', 2: 'val2'}` will also match the case. Unpacking and ignoring other element feature is also available for dictionary. `case ({1: val, 2: 'val2', 3: 'val3', **other})` is also a valid case. 

```python3
def matchMe(val):
    match val:
        case {1: 'val1', 2: 'val2'} as currentValue:
            print("I judge less. I am a match is exact, or all item, or all item in any sequence. current sequence: ", currentValue)
        case _:
            print("If nothing matches! Still there is hope.")
cases = [
    {1: 'val1', 2: 'val2'},
    {1: 'val1', 2: 'val2', 3: 'val3'},
    {1: 'val1', 3: 'val3', 2: 'val2'}
    ]
for case in cases:
    matchMe(case)
```


> The position `**others` should be in the end. Because it doesn't matter to the pattern on where you put `**others` in. Matching dictionary does not consider position, remember?

Smooth! right?

Yeah! Ok, Let's go matching object. We take a easy python object. We name it `Car`. How the car looks like?
```python3
class Car:
    def __init__(self, brand, model, milage):
        self.brand = brand
        self.model = model
        self.milage = milage
```
It's time for a match. Let's set three example. I am poor, So I don't have a car. So my car is `Car('','',0)`. My friend does better job, so he have a `Car('Toyota', 'Allion',35)`. And you my rich friend have `Car('Audi','A8',10)`. So with case I want to define the owner of the car. The cases should be like this.
```python3
match car:
    case Car(brand='Toyota',model='Allion', milage=25):
        print('My Friend\'s Car!')
    case Car(brand='Audi',model='A8', milage=10):
        print('Your Car!')
    case Car():
        print("My parking space but no Car!")
    case _:
        print("If nothing matches! Still there is hope.")
```
See here, you need to specify the arguments name in the `Car()` of `case`. If we want to skip using the argument names and bind them dynamically, we can do something called defining `__match_args__`in the class. The class now should look like this.

```python3
class Car:
    __match_args__ = ('brand', 'model','milage')
    def __init__(self, brand, model, milage):
        self.brand = brand
        self.model = model
        self.milage = milage
```
And we ca re-write the cases like this:
```python3
match car:
    case Car('Toyota','Allion',25):
        print('My Friend\'s Car!')
    case Car('Audi','A8', 10):
        print('Your Car!')
    case Car (var1, var2, var3) if var1 != "":
        print('Others car: Brand ', var1, 'Model ', var2,' Milage ', var3)
    case Car():
        print("My parking space but no Car!")
    case _:
        print("If nothing matches! Still there is hope.")
```
Take some time, and try by yourself! Peace.