import sqlite3
from employees import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )''')


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {
                  'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


empl_1 = Employee('John', 'Doe', 30000)
empl_2 = Employee('Jane', 'Doe', 90000)

insert_emp(empl_1)
insert_emp(empl_2)

emp = get_emps_by_name('Doe')
print(emp)

update_pay(empl_2, 95000)
remove_emp(empl_1)

emp = get_emps_by_name('Doe')
print(emp)

conn.close()
