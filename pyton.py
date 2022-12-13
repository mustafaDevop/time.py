import datetime
currenttime = datetime.datetime.now()
currenttime.hour
if currenttime.hour < 12:
    import datetime
    print("Goodmorning")
elif 12 <= currenttime.hour < 18:
    import datetime
    print("Goodafternoon")
else:
    print("Goodevening")