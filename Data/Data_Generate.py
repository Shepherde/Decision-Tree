import csv
import random
import string

''' Create a new dataset which includes the full range of value combinations out of the ranges 

It does this by looping through each row and its items.
If we find an item with a range in it, we need to create a few versions of that row. 

For each range in the row, we randomly sample from each. 

** Changing the number of samples:
Change the sample_size on line 91 to however many times you want to sample each range in each row. 

** new dataset:
change line 63 "index != " the index of the last column (output)
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


def crange(arg1, arg2):
	"""character range, crange(stop) or crange(start, stop)"""
	# print('crange: ', len(arg1), len(arg2))
	# print('args: ', arg1, arg2)
	start = string.ascii_letters.index(arg1)
	stop = string.ascii_letters.index(arg2)
	# print(start, stop)

	for index in range(start, stop+1):
		yield string.ascii_letters[index]


def data_gen(data):
	''' creates a new data set of however much size you'd like. 
	Samples a value if there is a range provided in the dataset '''

	new_datalist = []

	# LOOP THROUGH EACH ROW
	for i, row in enumerate(data):
		# print(i, row)

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
			
		# print('largest: ', largest)

		# RANDOMLY SAMPLE EACH RANGE: sample_size NUMBER OF TIMES and ADD THAT NEW ROW TO A NEW LIST
		counter = 0
		sample_size = 100

		# sample_size is the number of times we want to sample the range
		# each iteration we do one sample of each range - which creates a new row
		while counter < sample_size:

			new_row = []
			# print('counter: ', counter)
			
			# for each item in the row
			for index, item in enumerate(row):
				# print(index, item)

				# Sample it if it's a range
				if '-' in item and index != 7:

					# if digits
					# print(index, item)
					dash = item.index('-')
					if item[0:dash].isdigit():
						# create a new row, sample the range
						# print('RANGE: ', int(item[0:dash]), int(item[dash+1:])+1)
						sampled_value = random.sample(range(int(item[0:dash]), int(item[dash+1:])+1), 1)
						# print('sampled: ', sampled_value, ' from ', int(item[0:dash]), ' to ', int(item[dash+1:]),)
						listToStr = ''.join(map(str, sampled_value))
						new_row.append(str(listToStr))

					# if letters
					else:
						
						item1 = item[0:dash] 
						item2 = item[dash+1:dash+2]

						chars = []
						
						for stuff in (crange(item1, item2)):
							chars += str(stuff)

						# print('chars = ', chars)
					
						sampled_char = random.sample(chars, 1)
						# print('sampled: ', sampled_char, ' from ', item[0:dash], ' to ', item[dash+1:])

						for creature in sampled_char:	
							new_row.append(str(creature))

				# if no range, or is the last item in the dataset, just append the item
				else:
					new_row.append(item)


			# print('NEW ROW: ', new_row)
			counter += 1
			# ADD IT TO OUR NEW DATASET
			new_datalist.append(new_row)

	counter = 1
	for item in new_datalist:
		# print(counter, item)
		counter += 1

	# print(new_datalist)
	return new_datalist


def write_to_csv(data):
    with open('Datasets/Generate_100.csv', 'w', newline = '') as f:
        thewriter = csv.writer(f)
 
        for row in data:
            thewriter.writerow(row)
    return


if __name__ == "__main__":
    
	file = 'Datasets/UserToPack.csv'
	as_list = csv_wrangle(file)
	data = data_gen(as_list)
	write_to_csv(data)

    # item1 = 'f'
    # item2 = 'h'
    # for item in crange(item1, item2):
    #     print(item)