print('##################################################### CALCULATING YOUR WORTH #########################################')
print('CEEFOON - In this program, A robot called \'CEE-ROBOT\' is going to calculate your workrate to help you hit your target.\n')
print('CEEFOON - Please do well to provide the right information needed in order to get the right results too.\n')
print('CEEFOON - So over to you CEE-ROBOT\n')
while True:
    try:
        f = str(input('CEE-ROBOT: Follow my instructions till the end. Don\'t try to be stupid.\n\nCEE-ROBOT: Start the program by typing \'ceefoon\' \nYOU: '))
        if f == 'ceefoon':
            print()
            break
        else:
            print('CEE-ROBOT: That was a wrong command you dumb fuck!\n')
    except ValueError:
        print()
    except NameError:
        print('\n')

n = str(input('CEE-ROBOT: What is your name?\nYOU: '))
while True:
    try:
        g = str(input('CEE-ROBOT: Are you male or female?\nYOU: '))
        if g == 'male':
            print('CEE-ROBOT: Good day Mr', n, '\n')
            break
        elif g == 'female':
            print('CEE-ROBOT: Good day Mrs', n, 'It\'s a pleasure having you here.', '\n')
            break
        elif g == 'none':
            print('CEE-ROBOT: We will put your case in our daily prayer requests Mr or Mrs', n ,'. Lets\'s move.\n')
            break
        else:
            print('CEE-ROBOT: Are you inbetween or you don\'t know? You could say \'none\'\n')
    except:
        break

while True:
    try:
        timeworth=str(input('CEE-ROBOT: Do you know what your time is worth?\nYOU: '))
        if timeworth == 'yes':
            print('CEE-ROBOT: Great!\n')
            break
        elif timeworth == 'no':
            print('CEE-ROBOT: No problem. Let us continue. You will soon know.\n')
            break
        elif timeworth == 'maybe' or 'not really':
            print('CEE-ROBOT: You are confused but you will know soon.\n')
            break
        else:
            print('CEE-ROBOT: Please type yes or no. Or if you are not sure of your answer, you could say \'maybe\'\n')
    except:
        break

while True:
    try:
        hoursofwork=int(input('CEE-ROBOT: How many hours do you use to practice your skill each day?\nYOU: '))
        if hoursofwork in range(12, 24):
            print('CEE-ROBOT: You are a liar. Say the truth\n')
        elif hoursofwork < 3:
            print('CEE-ROBOT: You are a very lazy human being. You should consider changing or else...\n')
            break
        elif hoursofwork > 24:
            print('CEE-ROBOT: Don\'t be dumb. There are only 24 hours in a day.\n')
        else:
            print('CEE-ROBOT: You are making a good move. Keep it up!\n')
            break
    except ValueError:
        print('CEE-ROBOT: Numbers only please\n')
    except NameError:
        print('CEE-ROBOT: Numbers only please')

while True:
    try:
        daysofwork=int(input('CEE-ROBOT: Out of 365 days, how many days do you practice your skill?\nYOU: '))
        if daysofwork < 100:
            print('CEE-ROBOT: You are a very lazy human being. You should consider changing or else....\n')
            break
        elif daysofwork in range(250, 365):
            print('CEE-ROBOT: You are too lazy to perform for', daysofwork, 'days. Say the truth bitch!\n')
        elif daysofwork > 365:
            print('CEE-ROBOT: Don\'t be stupid you dumb fucker!. There are only 365 days in a year.\n')
        else:
            print('CEE-ROBOT: Awesome!\n')
            break
    except ValueError:
        print('CEE-ROBOT: Numbers only please you dumb motherfucker!\n')
    except NameError:
        print('CEE-ROBOT: Numbers only please you dumb motherfucker!')


while True:
    try:
        ammount=int(input('CEE-ROBOT: How much($) will you like to be making per year for the next 5 years?\nYOU: $'))
        if ammount < 100000:
            print('CEE-ROBOT: Please don\'t have a poverty mentality. Put a reasonable amount of money\n')
        elif ammount > 10000000:
            print('CEE-ROBOT: I know you will reach that stage. But please be realistic for now.\n')
        else:
            print()
            break
    except ValueError:
        print('CEE-ROBOT: Numbers only please you dumb asshole!\n')
    except NameError:
        print('CEE-ROBOT: Numbers only please you dumb asshole!')

time=hoursofwork*daysofwork
total = round(ammount/time)
totalstuff=round(ammount/time)*3
print('CEE-ROBOT: I have calculated how much you need to be earning per hour to be', total, 'dollars working the whole', hoursofwork, 'hour(s) without break.\n')
print('CEE-ROBOT: However, there are distractions around you such as your mobile phone and short breaks which you will be taking.\nYou will have to be earning', totalstuff, 'dollars per hour.\n')

if totalstuff > 1000:
    print('\nCEE-ROBOT: Getting a job will not make you this ammount. You need a high income skill or start up your own business.\n')
elif totalstuff < 1000:
    print('\nCEE-ROBOT: Good start anyway, but do not forget to aim higher than this on a long run.\n')

while True:
    try:
        f = str(input('CEE-ROBOT: End the program by typing \'ceefoon\' \nYOU: '))
        if f == 'ceefoon':
            print()
            break
        else:
            print('CEE-ROBOT: Wrong command pussy!\n')
    except ValueError:
        print()
    except NameError:
        print('\n')