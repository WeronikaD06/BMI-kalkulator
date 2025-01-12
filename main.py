def main():
    print("Witaj! Czas obliczyć Twoje BMI!!!")
    flag = True
    while(flag):
        print("""
Wybierz opcję:
    1. BMI text
    2. BMI input
    3. BMI charts""")
        prompt = input()
        if prompt == '1':
            bmi_text()
        elif prompt == '2':
            bmi_input()
        elif prompt == '3':
            bmi_charts()
        print("Kontynuować? (t/n)")
        prompt = input()
        if prompt!='t':
            flag=False

def bmi_text():
    #bmi text
    return 0

def bmi_input():
    waga = int(input("Ile ważysz? (podaj w kilogramach): "))
    wzrost = float(input("Ile masz wzrostu? (podaj w metrach)"))
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {format(bmi, '.2f')}")
    print("Twoja diagnoza: ")
    if bmi <= 0:
        print("Błąd. Sprawdź jeszcze raz!")
    elif bmi > 0 and bmi < 16:
        print("wygłodzenie")
    elif bmi >= 16 and bmi < 17:
        print("wychudzenie")
    elif bmi >= 17 and bmi < 18.5:
        print("niedowaga")
    elif bmi >= 18.5 and bmi < 25:
        print("pożądana masa ciała")
    elif bmi >= 25 and bmi < 30:
        print("nadwaga")
    elif bmi >= 30 and bmi < 35:
        print("otyłość 1 stopnia")
    elif bmi >= 35 and bmi < 40:
        print("otyłość 2 stopnia")
    else:
        print("otyłość 3 stopnia")

def bmi_charts():
    #bmi charts
    return 0

if __name__ == '__main__':
    main()