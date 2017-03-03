from datetime import datetime
from csv import reader 

def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile = 'temperature_log'
outfile = 'sensor_data.nc'


times = []
temps = []

with open(infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter = '\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))


