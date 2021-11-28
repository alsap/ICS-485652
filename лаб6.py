class Library:
 def __init__(self, name, genre, year, author):
  self.name = name
  self.grade = genre
  self.year = year
  self.author = author


bookX = ("Хіба ревуть воли, як ясла повні?", "роман", "2012", "Панас Мирный, Иван Рудченко")
bookE = ("Енеїда", "поєма", "1989", "Радняська школа")
bookK = ("Кайдашева сім'я", "повість", "1883", "І.Нечуй-Левицький")

print("Домашня бібліотека")

while True:
 print("1. Бібліотека.\n2. Пошук.\n3. Додати книгу.\n4. Видалити книгу.\n5. Вихід.\n")
 userInput = str(input())

 if userInput == "1":
  print(bookX)
  print(bookE)
  print(bookK)

 elif userInput == "2":
  while True:
   choice = input("Пошук книги за допомогою...\n1. name.\n2. genrе.\n3. year.\n4. author.\n")
   if choice == "1":
    while True:
     choice = input("Уведіть дані для пошуку.\n")
     if choice == 'Панас Мирный, Иван Рудченко':
      print("Хіба ревуть воли, як ясла повні?", "роман", "2012")
     else:
      print("Уведіть дані для пошуку.")
      if choice == "Енеїда":
       print("поєма", "1989", "Радняська школа")
      elif choice == "Кайдашева сім'я":
       print("повість,1878,І.Нечуй-Левицький")
   if choice == "2":
    while True:
     choice = input("ВВедіть дані для пошуку.\n")
     if choice ==  "роман":
      print("Хіба ревуть воли, як ясла повні?", "2012", "Панас Мирный, Иван Рудченко")
     else:
      print("Уведіть дані для пошуку.")
      if choice == "поєма":
       print("Енеїда", "1989", "Радняська школа")
      elif choice == "повість":
       print("Кайдашева сім'я,1878,І.Нечуй-Левицький")
   if choice == "3":
    while True:
     choice = input("Уведіть дані для пошуку.\n")
     if choice == "2012":
      print("Хіба ревуть воли, як ясла повні?", "роман", "Панас Мирный, Иван Рудченко")
     else:
      print("Уведіть дані для пошуку")
      if choice == "1989":
       print("Енеїда", "поєма", "Радняська школа")
      elif choice == "1878":
       print("Кайдашева сім'я,повість,І.Нечуй-Левицький")
   if choice == "4":
    while True:
     choice = input("ВВедіть дані для пошуку.\n")
     if choice == "Панас Мирный, Иван Рудченко":
      print("Хіба ревуть воли, як ясла повні?", "роман", "2012")
     else:
      print("ВВедіть дані для пошуку.")
      if choice == "Радняська школа":
       print("Енеїда", "поєма", "1989",)
      elif choice == "І.Нечуй-Левицький":
       print("Кайдашева сім'я,повість,1878")

 elif userInput == "3":
  print("Додайте книгу.")
  filename = input()
  print("Операція успішна.")
 elif userInput == "4":
  import os

  os.remove(" D:\\booktext.txt")
 elif userInput == "5":
  break