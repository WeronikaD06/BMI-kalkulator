import pandas as pd

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
    prompt = input("Podaj nazwę pliku xlsx (bez rozszerzenia np. dane.xlsx jako dane): ")
    file_name = f"{prompt}.xlsx"
    df = pd.read_excel(file_name)
    data = df.values.tolist()
    f = open("dane.txt", "a")
    for x in data:
        waga = int(x[0])
        wzrost = float(x[1])
        bmi = waga / (wzrost ** 2)
        print(f"Waga: {waga}")
        print(f"Wzrost: {wzrost}")
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
        f.write(f"{str(format(bmi, '.2f'))}\n")
    f.close()

def bmi_input():
    f=open("dane.txt", 'a')
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
    f.write(f"{str(format(bmi, '.2f'))}\n")
    f.close()

def bmi_charts():
    #bmi charts
    return 0

if __name__ == '__main__':
    main()