# Author:   Cesar Vicente
# Date:     Feb 09, 2018
# Tells the user what their astrological sign is.

month = int(input("What is your birth month (1-12)? "))

day = int(input("What is your birth day (1-31)? "))

if (month == 3 and day >= 21 and day <= 31) or (month == 4 and day >= 1 and day <=20):
    print("Your astrological sign is Aries.")

elif (month == 4 and day >= 21 and day <= 31) or (month == 5 and day >= 1 and day <=20):
    print("Your astrological sign is Taurus.")

elif (month == 5 and day >= 21 and day <= 31) or (month == 6 and day >= 1 and day <=20):
    print("Your astrological sign is Gemini.")

elif (month == 6 and day >= 21 and day <= 30) or (month == 7 and day >= 1 and day <=21):
    print("Your astrological sign is Cancer.")

elif (month == 7 and day >= 22 and day <= 31) or (month == 8 and day >= 1 and day <=22):
    print("Your astrological sign is Leo.")

elif (month == 8 and day >= 23 and day <= 31) or (month == 9 and day >= 1 and day <=21):
    print("Your astrological sign is Virgo.")

elif (month == 9 and day >= 22 and day <= 30) or (month == 10 and day >= 1 and day <=21):
    print("Your astrological sign is Libra.")

elif (month == 10 and day >= 22 and day <= 31) or (month == 11 and day >= 1 and day <=21):
    print("Your astrological sign is Scorpio.")

elif (month == 11 and day >= 22 and day <= 30) or (month == 12 and day >= 1 and day <=21):
    print("Your astrological sign is Sagittarius.")

elif (month == 12 and day >= 22 and day <= 31) or (month == 1 and day >= 1 and day <=20):
    print("Your astrological sign is Capricorn.")

elif (month == 1 and day >= 21 and day <= 31) or (month == 2 and day >= 1 and day <=19):
    print("Your astrological sign is Aquarius.")

elif (month == 2 and day >= 20 and day <= 29) or (month == 3 and day >= 1 and day <=20):
    print("Your astrological sign is Pisces.")

else: print("Not a valid birth date.")
