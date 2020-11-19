''' CLIMATE HELPER FUNCTIONS '''

def get_months(num):
    ''' gets next three months as list of numbers '''
    month_num = num
    beep = False 
    counter = 0
    months = []

    while not beep:

        for item in range(12):
            # print(item)

            if counter >= 3:
                beep = True
                break

            if item == month_num:
                counter += 1
                months.append(item+1)
                # print('counter ', counter)
            
            elif counter != 0:
                counter += 1
                months.append(item+1)
                # print('counter ', counter)

    print(months)
    return months



if __name__ == "__main__":
    get_months(3)
        