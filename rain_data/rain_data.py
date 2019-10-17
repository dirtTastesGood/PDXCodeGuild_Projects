def load_data(data):
    with open(data, 'r') as rain_data:
        data = rain_data.readlines()
        lines = []
        for line in data:
            line = line.split(" ")
            line = [x for x in line if x != ""] # eliminate blank strings in line
            lines.append([line[0], line[1]])

    return lines

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
            date_dict[year][month] = {day:rainfall}
        elif year in date_dict:
            if month not in date_dict[year]:
                date_dict[year][month] = {day:rainfall} 
            elif month in date_dict[year]:
                date_dict[year][month][day] = rainfall
            
    return date_dict

def average(data):
    nums = []
    for i in data:
        if i[1] != '-':
            nums.append(int(i[1]))
    avg = sum(nums) // len(nums)

    return avg
    
def main():
    raw_data = "rain_data.txt"
    data = load_data(raw_data)
    rain_data = create_date_dict(data)

    year = input(f"Please enter a year {list(rain_data.keys())[-1]}-{list(rain_data.keys())[0]}: ")
    
    months = list(rain_data[year].keys())[::-1]
    month = input(f"Please enter a month 1-12: ")
    month = months[int(month)-1]

    days = list(rain_data[year][month].keys())[::-1]

    day = input(f"Enter a day {days[0]}-{days[-1]}: ")
    if day[0] == "0":
        day = day.strip("0")
    
    day = days[int(day)-1]

    print(day)
    print(f"The total rainfall for {month}-{day}-{year} was {rain_data[year][month][day]}")

    print(f"The average total rainfall over the entire data set is: {average(data)}")
    
main()

