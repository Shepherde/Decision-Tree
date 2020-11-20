''' CLIMATE HELPER FUNCTIONS '''

from calendar import monthrange

def get_months(num):
    ''' gets next three months as a list of numbers '''

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

    # print(months)
    return months

def get_days(year, month_list):
    ''' returns the number of days in each of the months as well as the days from that year when the month actually began '''
    days_dict = {}

    total_days = 0
    counter = 1
    
    for month in range(1, 13):

        wkday_days = monthrange(year, month)
        days = wkday_days[1]
        # print(counter, days)

        # it's okay that we get the month from the same year even if it loops around to the next year
        # because it's an average of all the years, so it gets calculated anyways. 
        for item in month_list:
            if item == counter:
                days_dict[item] = [total_days , days]

        total_days += days
        counter += 1

    # dict(month:[start:total])
    # print('Days: ', days_dict)
    return days_dict

    

if __name__ == "__main__":
    m_list = get_months(10)
    days_month = get_days(2005, m_list)
        