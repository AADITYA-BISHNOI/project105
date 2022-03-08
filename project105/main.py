import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)

tm = [60+61+65+63+98+99+90+95+91+96]
tml = len(file_data)

for marks in file_data:
    tm += float(marks[1])

mean = tm / tml

print("Mean = ", str(mean))


