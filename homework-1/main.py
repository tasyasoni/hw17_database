"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
from pprint import pprint

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Antoniya2308"
)
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data\employees_data.csv', 'r') as file_csv:
                next(file_csv)  # пропускаем заголовок
                for line in file_csv:
                    line = line.replace('"', '')
                    file1 = open('north_data\employees.txt', 'a')
                    file1.write(line)
                file1.close()
            with open('north_data\employees.txt', 'r') as file_final:
                cur.copy_from(file_final, 'employees', sep=',')
            open('north_data\employees.txt','w').close()
            with open('north_data\customers_data.csv', 'r') as file_csv:
                next(file_csv)  # пропускаем заголовок
                for line in file_csv:
                    line = line.replace('"', '')
                    file1 = open('north_data\customers.txt', 'a')
                    file1.write(line)
                file1.close()
            with open('north_data\customers.txt', 'r') as file_final:
                cur.copy_from(file_final, 'customers', sep=',')
            open('north_data\customers.txt', 'w').close()
            with open('north_data\orders_data.csv', 'r') as file_csv:
                next(file_csv)  # пропускаем заголовок
                for line in file_csv:
                    line = line.replace('"', '')
                    file1 = open('north_data\orders.txt', 'a')
                    file1.write(line)
                file1.close()
            with open('north_data\orders.txt', 'r') as file_final:
                cur.copy_from(file_final, 'orders', sep=',')
            open('north_data\orders.txt', 'w').close()
finally:
    conn.close()