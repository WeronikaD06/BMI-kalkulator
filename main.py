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
   #bmi input
    return  0

def bmi_charts():
    #bmi charts
    return 0

if __name__ == '__main__':
    main()