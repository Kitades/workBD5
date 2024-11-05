import psycopg2

from course_work5.db.managers.base import DBManager


class PostgresDBManager(DBManager):

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_companies_and_vacancies_count(self) -> list[tuple[str, int]]:
        sql = """
            SELECT e.name, COUNT(*) as vacancies_count
            FROM employers as e
            LEFT JOIN vacancies as v ON e.id = v.employer_id 
            GROUP BY e.name
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_all_vacancies(self):
        sql = """
        SELECT name, url, type,salary_from FROM vacancies
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_avg_salary(self):
        sql = """
        SELECT AVG(salary_from), AVG(salary_to)
        FROM vacancies
        WHERE salary_from IS NOT NULL
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            min_salary, max_salary = cursor.fetchone()
            average_salary = (min_salary + max_salary) / 2
            return round(average_salary, 2)

    def get_vacancies_with_higher_salary(self):
        sql = """
        SELECT name, url, type, salary_from
        FROM vacancies
        WHERE salary_from > AVG(salary_from)
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_vacancies_with_keyword(self):
        keyword = "Python"
        sql = f"""
        SELECT name, url, type, salary_from
        FROM vacancies
        WHERE LOWER(name) LIKE LOWER(%s)
        """
        self.connect()

        with self.connection.cursor() as cursor:
            cursor.execute(sql, (f'%{keyword}%',))
            return cursor.fetchall()

