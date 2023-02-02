import argparse
import sqlite3
import pandas as pd

# Создание аргументов
parser = argparse.ArgumentParser(description='Convert a SQLite database to an Excel file')
parser.add_argument('-i', '--input', type=str, required=True, help='Input SQLite database file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output Excel file')
parser.add_argument('-t', '--table', type=str, required=True, help='Table name to convert')
args = parser.parse_args()

# Подключение к SQLite таблице
conn = sqlite3.connect(args.input)

# Чтение всех данных из таблицы
df = pd.read_sql_query(f"SELECT * from {args.table}", conn)

# запись датафрейма в файл 
df.to_excel(args.output, index=False)

# Закрытие соединения с БД
conn.close()