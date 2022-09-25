print("Day 16 Learning Reading and Writing CSV file")

"""What is a CSV? 
    CSV (Comma Separated Values) is a simple file format used to store tabular data,
    such as a spreadsheet or database."""

import  csv

print(" Reading a CSV file\n")
filename = "employees.csv" #  downloaded from https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784
fields, rows = [], []
with open(filename ,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # csvreader = csv.reader(csvfile,  delimiter = "\t") # to remove spaces in simple

    # fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
        # print(row)

    print("total num of rows :",csvreader.line_num)
    print("field names :".join(field for field in fields))

print('First 5 rows are:')
for row in rows[:5]:     # parsing each column of a row
    for col in row:
        print("\t",col,end=" "),
    print('\n')




print(" Writing to a CSV file")

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Ali', 'COE', '2', '9.0'],
        ['John', 'COE', '2', '9.1'],
        ['Sara', 'IT', '2', '9.3'],
        ['Azhar', 'SE', '1', '9.5'],
        ['Zohaib', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

filenam = "university_records.csv"

with open(filenam, "a") as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open(filenam, "r") as csvfile:
    readcsv = csv.reader(csvfile)
    rows = []
    for row in readcsv:
        rows.append(row)

    for r in rows:
        print(r)





















