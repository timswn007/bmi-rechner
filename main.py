gewicht = int(input ("gebe hier dein gewicht in Kg ein: "))
größe = int(input ("gebe hier deine größe in cm ein: "))
bmi = gewicht/((größe * größe)/10000)
if bmi < 18.5:
    print("du bist untergewichtig du lauch geh ins fitness studio")
elif bmi >= 18.5 and bmi <= 24.9:
    print("du bist normal du kek")
else:
    print("du bist fett, geh abnehmen")
print("dein Bmi ist :", bmi)