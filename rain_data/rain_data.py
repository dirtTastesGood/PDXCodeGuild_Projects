def load_data(data):
    with open(data, 'r') as rain_data:
        data = rain_data.readlines()
        data_tups = []
        for line in data:
            line = line.split(" ")
            line = [x for x in line if x != ""] # eliminate blank strings in line
            data_tups.append((line[0], line[1]))

    return data_tups

def create_date_dict(data):
    date_dict = {}

    for datum in data:
        split_date = datum[0].split("-")
        
        year = split_date[2]
        month = split_date[1]
        day = split_date[0]

        rainfall = datum[1]

        if year not in date_dict:
            date_dict[year] = {}
        elif year in date_dict:
            if month not in date_dict[year]:
                date_dict[year][month] = {} 
            elif month in date_dict[year]:
                if day not in date_dict[year][month]:
                    date_dict[year][month][day] = rainfall
            
    

    return date_dict

def main():
    raw_data = "rain_data.txt"
    data = load_data(raw_data)
    rain_data = create_date_dict(data)

    #print(rain_data)
    #print(rain_data['2011']['AUG']['30'])

    # year = input(f"Please enter a year {list(rain_data.keys())[-1]}-{list(rain_data.keys())[0]}: ")
    
    # months = list(rain_data[year].keys())[::-1]
    # month = input(f"Please enter a month 1-12: ")
    # month = months[int(month)-1]

    # print(month)

    # days = list(rain_data[year][month].keys())[::-1]

    # print(days)

    # day = input(f"Enter a day {days[0]}-{days[-1]}: ")
    # day = days[int(day.strip("0"))]

    # print(day)
    # print(f"The total rainfall for {month}-{year} was {rain_data[year][month]}")
main()

