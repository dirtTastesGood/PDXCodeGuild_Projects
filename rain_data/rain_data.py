import datetime

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
        if len(datum) > 3:
            year = datum[-4::]
            month = datum[-8:-5]
            day = datum[0:2]

    print(data)

def main():
    raw_data = "rain_data.txt"
    data = load_data(raw_data)

    user_date = "08-OCT-2019"

    date = datetime.datetime.strptime(user_date, '%d-%b-%Y')

    #create_date_dict(rain_data)
    
main()

