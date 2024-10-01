#!/usr/bin/env python3

#User inputs their birth date and their zodiac sign is given to them.

def main():
    
    zodiac = input('What is your birth day mm/dd?')
    month, day = map(int, zodiac.split('/'))

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print('Your zodiac sign is: Aries')

    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print('Your zodiac sign is: Taurus') 

    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print('Your zodiac sign is: Gemini')

    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print('Your zodiac sign is: Cancer')

    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print('Your zodiac sign is: Leo')

    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print('Your zodiac sign is: Virgo')

    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print('Your zodiac sign is: Libra')

    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print('Your zodiac sign is: Scorpio')

    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print('Your zodiac sign is: Sagitarrius')

    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print('Your zodiac sign is: Capricorn')

    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print('Your zodiac sign is: Aquarius')

    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print('Your zodiac sign is: Pieces')

    else:
        print('Invalid date')


if __name__== '__main__':
    main()
