import datetime

def load_file(data):
    with open(data, 'r') as rain_data:
        return rain_data.read()

def create_date_dict(data):
    date_dict = {}

    for datum in data:
        if len(datum) > 3:
            year = datum[-4::]
            month = datum[-8:-5]
            day = datum[0:2]

    print(data)

def main():
    data = "rain_data.txt"
    rain_data = load_file(data)

    user_date = "08-OCT-2019"

    date = datetime.datetime.strptime(user_date, '%d-%b-%Y')

    rain_data = ' '.join(rain_data.split())
    rain_data = rain_data.split(" ")

    create_date_dict(rain_data)
    
main()

