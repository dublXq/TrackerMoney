import os

import Categories_class

# Общий бюджет
TOTAL_BUDJET = 10000

# Список всех транзакций
general_list = []

# Объект класса категорий (Categories_class)
category_oblect = Categories_class


def add_transaction_method():
    global TOTAL_BUDJET
    add_summa = int(input("Введите сумму доходов: "))
    TOTAL_BUDJET += add_summa

    # Выводится список категорий для добавления по порядку ключ - значение
    for key, value in category_oblect.salary_dict.items():
        print(f"{key}. {value}")

    category = int(input("Введите категорию добавления: "))

    if add_summa and category > 0:
        general_list.append(category_oblect.salary_dict.get(category) + "|" + str(add_summa))


def minus_transaction_method():
    global TOTAL_BUDJET
    add_summa = int(input("Введите сумму расходов: "))
    TOTAL_BUDJET -= add_summa

    # Выводится список категорий для добавления по порядку ключ - значение
    for key, value in category_oblect.transaction_dict.items():
        print(f"{key}. {value}")

    category = int(input("Введите категорию добавления: "))

    if add_summa and category > 0:
        general_list.append(category_oblect.transaction_dict.get(category) + "|" + str(add_summa))


if __name__ == "__main__":

    while True:
        print("Добро пожаловать :)\n"
              "Выберите действие:"
              "\n1.Добавление транзакций"
              "\n2.Мой Баланс"
              "\n3.Отчет"
              "\n4.Выход")

        a = input("Ввод: ")

        match a:
            case "1":
                while True:
                    print("Вы хотите добавить Доход или Расход?\n1.Доход\n2.Расход ")
                    v = input("Ввод: ")
                    if v == "1":
                        add_transaction_method()
                        print("Доходы успешно добавлены")
                        break
                    elif v == "2":
                        minus_transaction_method()
                        print("Расходы успешно добавлены")
                        break
                    else:
                        print("Вы ввели что-то не то. Попробуйте еще раз! ")
            case "2":
                print(f"Ваш текущий баланс --> {TOTAL_BUDJET}" + " UAH")
            case "3":
                print("Ваш отчет генерируется...")

                # Разделяем транзакции на доходы и расходы
                income_list = []
                expense_list = []

                for i in general_list:
                    category, amount = i.split("|")
                    if category in category_oblect.salary_dict.values():
                        income_list.append(f"Категория: {category}, Сумма: {amount}")
                    elif category in category_oblect.transaction_dict.values():
                        expense_list.append(f"Категория: {category}, Сумма: -{amount}")

                # Записываем данные в файл
                with open("text.txt", "a", encoding="utf-8") as txt:
                    if income_list:
                        txt.write("Доходы:\n")
                        for income in income_list:
                            txt.write(income + "\n")

                    if expense_list:
                        txt.write("\nРасходы:\n")
                        for expense in expense_list:
                            txt.write(expense + "\n")

                print("Ваш отчет готов. Путь отчета --> " + os.path.abspath("text.txt"))

            case "4":
                print("Выход успешен")
                break
