filename = "group.txt"
import csv
import glob 
import sys
import os

print ("Оберіть дію для виконання: \n1. Читання файлів \n2. запис та дозапис у файл \n3. пошук файлів у каталозі \n4. пошук даних у файлі")
choise = input()
if choise == "1":
    fd = open (filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print (row)

elif choise == "2":
    fd = open (filename, "a+")
    dani = input("Введіть дані які хочете додати: ")
    fd.write(dani + "\n")

elif choise == "3":
    maskafile = input("Введіть назву або маску файлу, який потрібно знайти: ")
    for filename in glob.glob(maskafile):
        print(filename)

elif choise == "4":
    poshuk = input ("Введіть дані які потрібно знайти у файлі: ")

    filedata = open(filename, "r").readlines()
        
    for row in filedata:
        if poshuk in row:
            print(row)
