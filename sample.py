import csv_to_database

a = csv_to_database.CsvToDatabase("sample","a,b,c")
a.create_table()

print(a.select_all())

a.get_column_no("a")