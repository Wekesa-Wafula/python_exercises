while True:
    grade1 = int(input('Enter your English score: '))
    grade2 = int(input('Enter your Swahili score: '))
    grade3 = int(input('Enter your Math score: '))
    grade4 = int(input('Enter your Social Studies score: '))
    grade5 = int(input('Enter your Religious Education score: '))

    average = (grade1 + grade2 + grade3 + grade4 + grade5)/5

    if average > 100:
        print('Kindly input your grades correctly')
    elif average >= 70 and average <=100:
        print('You got an A')
    elif average >= 60 and average < 70:
        print('You got a B')
    elif average >= 50 and average < 60:
        print('You got a C')
    elif average >= 40 and average < 50:
        print('You got a D')
    else:
        print('You failed bruv')