def matchMe(val):
    requestSent = True
    match val:
        case 404:
            print("Sorry! No Resource found.")
        case 200 if requestSent:
            print("Tada!! Hello world.")
        case "Winner":
            print("Congratulations!")
        case "Loser":
            print("Failure is the pillar of success!")
        case "Rose" | "Lily" | "Sunflower" as flower:
            print("Great! I like ", flower)
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
        case {1: 'val1', 2: 'val2'} as currentValue:
            print("I judge less. I am a match is exact, or all item, or all item in any sequence. current sequence: ", currentValue)
        case Car('Toyota','Allion') as car:
            print('My Friend\'s Car! Car: ', car.showCar())
        case Car(brand='Audi',model='A8'):
            print('Your Car!')
        case Car():
            print("My parking space but no Car!")
        case val if val< 100:
            print("The initial journey is hard.")
        case _:
            print("If nothing matches! Still there is hope.")
cases = [
    404,
    200,
    "Winner",
    "Loser",
    "Rose",
    (0,0),
    (5,0),
    (7,9),
    (1,2,3,4),
    (1,2,4),
    (1,3,4),
    (1,"OMG",4),
    (1,"OMG", "I", "am", "rich", [1,2,3],4),
    (1,4,"OMG", "I", "am", "rich", [1,2,3]),
    {1: 'val1', 2: 'val2'},
    {1: 'val1', 2: 'val2', 3: 'val3'},
    {1: 'val1', 3: 'val3', 2: 'val2'},
    Car(),
    Car(brand='Toyota'),
    Car('Audi','A8'),
    70
    ]
for case in cases:
    matchMe(case)

