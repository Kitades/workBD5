from prettytable import PrettyTable

from course_work5.db.managers import PostgresDBManager


def print_employers():
    db_manager = PostgresDBManager
    try:
        res = db_manager.get_companies_and_vacancies_count()

    finally:
        db_manager.disconnect()

    table = PrettyTable(field_names=['Название компании', 'количество выкансий'])
    for data in res:
        table.add_row([data[0], data[1]])
    print(table)


def print_avg_salary():
    db_manager = PostgresDBManager
    try:
        salary = db_manager.get_avg_salary()

    finally:
        db_manager.disconnect()

    print(f'средняя зарплата : {salary}')


def print_all_vacancies():
    db_manager = PostgresDBManager
    try:
        vacancies = db_manager.get_all_vacancies()

    finally:
        db_manager.disconnect()

    print(vacancies)


def print_get_vacancies_with_higher_salary():
    db_manager = PostgresDBManager
    try:
        vacancies = db_manager.get_vacancies_with_higher_salary()

    finally:
        db_manager.disconnect()

    print(vacancies)


def print_vacancies_with_keyword():
    db_manager = PostgresDBManager
    try:
        vacancies = db_manager.get_vacancies_with_keyword()

    finally:
        db_manager.disconnect()

    print(vacancies)


def run_interation():
    while True:
        print("""
            выберите что делать 
            1 - получить список     
            2 - средняя зарплата
            3 - все вакансии
            4 - вакансии с высокой зарплатой
            5 - вакансии с определенным ключевым словом
            0 - выйти
            """)

        user_input = input()

        if user_input == "0":
            break

        elif user_input == "1":
            print_employers()

        elif user_input == "2":
            print_avg_salary()

        elif user_input == "3":
            print_all_vacancies()

        elif user_input == "4":
            print_get_vacancies_with_higher_salary()

        elif user_input == "5":
            print_vacancies_with_keyword()
