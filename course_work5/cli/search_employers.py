
from prettytable import PrettyTable

from course_work5.api_clients import HeadHunterAPIClient

hh_client = HeadHunterAPIClient()


def run():
    """https://api.hh.ru/openapi/redoc"""
    print("Введите текст для поиска работодателя")
    search = input()
    employers = hh_client.search_employers(search)
    if not employers:
        print("Ничего не найдено")
        return

    table = PrettyTable(field_names=['ID', 'Название клмпании', 'URL', 'COUNT'])
    table.sortby = 'COUNT'
    table.reversesort = True
    for emp in employers:
        table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])

    print(table)


if __name__ == "__main__":
    run()
