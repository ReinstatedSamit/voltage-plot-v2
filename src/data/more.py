import csv
with open("sample.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for num in range(0, 10):
        writer.writerow([num])