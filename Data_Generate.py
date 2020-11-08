import csv

def read_file():

    dataFile = open('Datasets/UserToPack.csv')
    dataReader = csv.reader(dataFile)
    # data = list(dataReader)
    for row in dataReader():
        print(str(row))

    return 




if __name__ == "__main__":
    
    read_file()