from application.salary import calculate_salary
from application.db.people import get_employees
from dirty_main import *
from datetime import datetime as dt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dt_temp = dt.today()
    print(f"Текущая дата: {(dt_temp.day)}.{(dt_temp.month)}.{(dt_temp.year)}")
    calculate_salary()
    get_employees()
    dirty_funk0()
    dirty_funk1()
    dirty_funk2()