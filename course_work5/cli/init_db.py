from course_work5.db.loader import load_employers, load_vacancies
from course_work5.db.migrations import create_database, apply_migrations


def run():
    print("создание схем")
    create_database()
    apply_migrations()

    load_employers()
    load_vacancies()


if __name__ == "__main__":
    run()
