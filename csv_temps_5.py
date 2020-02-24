import matplotlib.pyplot as plt
import csv
from datetime import datetime

def get_weather_data(filename, highs, lows, dates):
    open_file = open(filename, "r")
    csv_file = csv.reader(open_file, delimiter = ",")
    header_row = next(csv_file)    

    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    date_index = header_row.index('DATE')
    name_index = header_row.index('NAME')

    # Get high and low temperatures and dates from this file
    for row in csv_file:        
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    
# Get weather data for Sitka
open_file1 = "sitka_weather_2018_simple.csv"
highs, lows, dates = [], [], []

get_weather_data(open_file1, highs, lows, dates)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig,ax = plt.subplots(2,1)
ax[0].set_title("SITKA AIRPORT, AK US", fontsize = 12)
ax[0].plot(dates, highs, color = 'red', alpha = 0.5)
ax[0].plot(dates, lows, color = 'blue', alpha = 0.5)
ax[0].fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Get weather data for Death Valley
open_file2 = "death_valley_2018_simple.csv"
highs, lows, dates = [], [], []

get_weather_data(open_file2, highs, lows, dates)

# Add Death Valley data to other plot
ax[1].set_title("DEATH VALLEY, CA US", fontsize = 12)
ax[1].plot(dates, highs, color = 'red', alpha = 0.5)
ax[1].plot(dates, lows, color = 'blue', alpha = 0.5)
ax[1].fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format plot
plt.suptitle("Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US",fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis = 'both', which = "major", labelsize = 12)


fig.autofmt_xdate()


plt.show()