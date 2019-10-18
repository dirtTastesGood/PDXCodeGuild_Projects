def load_data(data):
    with open(data, 'r') as rain_data:
        data = rain_data.readlines()
        lines = []
        for line in data:
            line = line.split(" ")
            line = [x for x in line if x != ""] # keep only the elements that are not blank strings
            lines.append([line[0], line[1]])

    return lines

def create_date_dict(data):
    date_dict = {}

    for datum in data:
        date = split_date(datum[0])
        
        year = date[2]
        month = date[1]
        day = date[0]

        rainfall = datum[1]

        if year not in date_dict:
            date_dict[year] = {}
            date_dict[year][month] = {day:rainfall}
        elif year in date_dict:
            if month not in date_dict[year]:
                date_dict[year][month] = {day:rainfall} 
            elif month in date_dict[year]:
                date_dict[year][month][day] = rainfall
    
    return date_dict

def split_date(date):
    return date.split("-")
    
def get_average(data):
    nums = []
    count = 0
    for i in data:
        for j in data[i]:
            for k in data[i][j]:
                num = data[i][j][k]
                if num != "-":
                    nums.append(int(num))
                    count += 1
    
    avg = sum(nums) / count
    
    return avg

def get_variance(data, avg):
    nums = []
    count = 0
    for i in data:
        for j in data[i]:
            for k in data[i][j]:
                num = data[i][j][k]
                if num != "-":
                    num = int(num)
                    nums.append((num - avg) ** 2)
                    count += 1
    
    variance = sum(nums) / count
    
    return variance

def get_record_day(data):
    record = 0
    for i in data:
        for j in data[i]:
            for k in data[i][j]:
                num = data[i][j][k]
                if num != "-" :
                    num = int(num) 
                    if num > record:
                        record = num
                        record_day = f"{k}-{j}-{i}"
    
    return record_day

def main():
    raw_data = "rain_data.txt"
    data = load_data(raw_data)
    rain_data = create_date_dict(data)

    # year = input(f"Please enter a year {list(rain_data.keys())[-1]}-{list(rain_data.keys())[0]}: ")
    
    # months = list(rain_data[year].keys())[::-1]
    # month = input(f"Please enter a month 1-12: ")
    # month = months[int(month)-1]

    # days = list(rain_data[year][month].keys())[::-1]

    # day = input(f"Enter a day {days[0]}-{days[-1]}: ")
    # if day[0] == "0":
    #     day = day.strip("0")
    
    # day = days[int(day)-1]

    # print(f"The total rainfall for {month}-{day}-{year} was {rain_data[year][month][day]}")

    avg = get_average(rain_data)
    print(f"\nThe average total rainfall over the entire data set is: {avg}")

    print(f"\nThe variance over the entire data set is: {get_variance(rain_data, avg)}")
    
    record_day = get_record_day(rain_data)

    date = split_date(record_day)
    day = date[0]
    month = date[1]
    year = date[2]

    print(f"\nThe day in the data set that had the most rainfall was {record_day} with {rain_data[year][month][day]}")
main()