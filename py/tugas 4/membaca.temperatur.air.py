temperatur = float(input("Masukkan temperatur air dalam derajat Celsius: "))

if temperatur <= 0:
    print("Wujud air pada temperatur tersebut adalah padat (es).")
elif 0 < temperatur < 100:
    print("Wujud air pada temperatur tersebut adalah cair.")
else:
    print("Wujud air pada temperatur tersebut adalah gas (uap).")
