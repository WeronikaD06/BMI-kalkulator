import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    # bmi text
    return 0

def bmi_input():
    # bmi input
    return 0

def bmi_charts():
    f = open('dane.txt', 'r')
    a = f.readlines()
    values = []
    names = []
    for x in a:
        values.append(float(x[0:-1]))
    f.close()
    for i in range(1, len(values)+1):
        names.append(int(i))
    plt.xticks(np.arange(min(names), max(names) + 1, 1.0))
    plt.yticks(np.arange(0, 80, 5.0))
    plt.scatter(np.array(names) , np.array(values))
    plt.show()

if __name__ == '__main__':
    main()