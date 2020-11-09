import csv
import random

''' Create a new dataset which includes the full range of value combinations out of the ranges 

It does this by looping through each row and its items.
If we find an item with a range in it, we need to create a few versions of that row. 

For each range in the row, we randomly sample from each. 
''' 

# row 1 = 1, 2-3, 3, 3-5, 4
# randomly sample each range for an item. If we do a random sample enough times, we'll have atleast covered most scenarios


def csv_wrangle(file):
    ''' wrangles with the csv file -> returns list of each row '''
    dataset_list = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # print(row)
            dataset_list.append(row)
    # print(dataset_list)
    return dataset_list


def write_to_csv(data):

    for i, row in enumerate(data):
        print(i, row)

        if i == 0:
            continue

        # FIND THE LARGEST RANGE
        # get all the ranges
        ranges = {}
        for index, item in enumerate(row):
            # print(index, item)
            # if the row has a dash in it, it's a range
            if '-' in item and index != 7:
                # add the item to our ranges
                ranges[index] = item
        # print('Ranges: ', ranges)

        # get the largest range
        largest = None
        for key, value in ranges.items():
            # print(value, value.index('-'))
            dash = value.index('-')
            # print(value[0:dash], value[dash+1:])

            if value[0:dash].isdigit():
                difference = int(value[dash+1:]) - int(value[0:dash])
                # print('difference ', difference, ' from ', value[0:dash], value[dash+1:])

                if largest == None:
                    largest = difference 
                elif difference > largest:
                    largest = difference 
            
        print('largest: ', largest)

        # RANDOMLY SAMPLE EACH RANGE and ADD THAT NEW ROW TO A NEW LIST
        counter = 0
        sample_size = 5

        while counter < sample_size:
            print('counter: ', counter)
            new_row = []
            
            for index, item in enumerate(row):

                if item[0:dash].isdigit():
                    # create a new row
                    if '-' in item and index != 7:
                        # sample the range
                        print('range ', item[dash+1:], item[0:dash])
                        sampled_value = random.sample(range(int(item[0:dash]), int(item[dash+1:])), 1)
                        print('sampled: ', sampled_value, ' from ', int(item[dash+1:]), int(item[0:dash]))
                        new_row.append(sampled_value)
                    else:
                        new_row.append(item)
                    print('NEW ROW: ', new_row)

                else:
                    break 

            print('hello?', value[0:dash])
            counter += 1
        # ADD THEM TO OUR NEW DATASET


    # with open('mycsv.csv', 'w', newline = '') as f:
    #     thewriter = csv.writer(f)

    #     thewriter.writerow(['col1', 'col2', 'col3'])
 
    #     for i in range(1, 10):
    #         thewriter.writerow(['one', 'two', 'three'])


    return 

if __name__ == "__main__":
    
    file = 'Datasets/UserToPack.csv'
    as_list = csv_wrangle(file)
    write_to_csv(as_list)