import csv
def read_csv(file):
    site = []
    with open('names.csv') as file:
        data = csv.reader(file)
        for row in data:
            sites = {}
            sites['names'] = row[0]
            sites['age']   = row[1]
            sites['sex']   = row[2]
            site.append(sites)
    return site
if __name__ == "__main__" :
    print(read_csv('names.csv'))            