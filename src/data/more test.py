import csv
filename= 'V123.csv'
filename2="V123new"
with open(filename, 'w+', newline='') as f, open(filename2, 'w') as csvoutput:
    csv_writer = csv.writer(f)
    writer = csv.writer(csvoutput, lineterminator="\n")
    row = ['Title']
    csv_writer.writerow(row)
    row.append('Added or Deleted Files')
    writer.writerow(row)

    for prs in repo.pull_requests():
        ...
        row = [changes['title']]
        csv_writer.writerow(row)
        csv_writer.writerow([changes['title']])
        ...
        if 'added' in (data.status for data in repo.pull_request(prs.number).files()) or 'removed' in (data.status for data in repo.pull_request(prs.number).files()):
            row.append('True')
        else:
            row.append('False')
            writer.writerow(row)