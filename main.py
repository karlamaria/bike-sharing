#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:50:17 2022

@author: kgarcia03

Student ID: A00304376

Starts the user menu
"""

import stats
import visualization
import sys


temperatures = []
windspeeds = []
total_rentals = []
weathersits = []
weathersit_dict = {}
season_dict = {}

"""
Calculate the sum of list

Parameters
----------
input_list: String
    filename that contains bike sharing data.

Returns
-------
None
"""
def load_bike_rentals(filename):
    
    try:
        with open(filename) as data_file:
            # read in the column headers and ignore  
            headers = data_file.readline()
            # for each subsequent line
            for line in data_file:
                # split into components        
                date_string, season, weekday, weathersit, temp, windspeed, total_rental, casual, registered, month, holiday = line.split(",")
        
                temperatures.append(round(float(temp),2))
                windspeeds.append(round(float(windspeed),2))
                total_rentals.append(int(total_rental))
                weathersits.append(weathersit)
                
                weathersit_dict[weathersit] = weathersit_dict.get(weathersit,0) + int(total_rental)

                if season not in season_dict:
                    season_dict[season] = [int(total_rental)]
                else:
                    season_dict[season].append(int(total_rental))
                
                
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IsADirectoryError as dir_error:
        print(dir_error)
    except PermissionError as permission_error:
        print(permission_error)
        
def show_category_menu():        
    option = '1'
    while (option != '0'):
        print("""
[1]Number of weathersit
[2]Weathersit with more rentals
[3]Weathersit with less rentals 
[4]Weathersit with highest rentals
[5]Weathersit with lowest rentals
[6]Pie chart Weathersit
[7]Bar chart renatals
[8]Box Plot Season 
[0]Return to main menu""")
        option = input("Please Select:") 
                
        if (option == '1'):   
            print("Number of weathersit:", len(weathersit_dict))
            print()
            continue   
            
        if (option == '2'):   
            most_popular_weathersit, most_popular_weathersit_value = stats.get_max_total(weathersit_dict)
            print("Weathersit with more rentals is " + most_popular_weathersit + " with " + most_popular_weathersit_value + " rentals.")
            print()
            continue   
            
        if (option == '3'):   
            less_popular_weathersit, less_popular_weathersit_value = stats.get_min_total(weathersit_dict)
            print("Weathersit with less rentals is " + less_popular_weathersit + " with " + less_popular_weathersit_value + " rentals.")
            print()
            continue   
            
        if (option == '4'):   
            max_category, max_category_value = stats.get_max_item(weathersits, total_rentals)
            print("Weathersit with highest rentals is " + max_category + " with " + max_category_value + " rentals.")
            print()
            continue   
            
        if (option == '5'):   
            min_category, min_category_value = stats.get_min_item(weathersits, total_rentals)
            print("Weathersit with lowest rentals:", min_category + " with " + min_category_value + " rentals.")
            print()
            continue   
        
        if (option == '6'):
            visualization.plot_pie_chart(weathersit_dict, "Weathersit")
            print()
            continue   
                        
        if (option == '7'):
            visualization.plot_bar_chart(weathersit_dict, "Rentals", "Weathersit")
            print()
            continue   
                        
        if (option == '8'):                
            visualization.plot_multiple_box_plot(season_dict, "Season", "Total Rental")
            print()
            continue   
        

def show_numeric_menu():
    option = '1'
    while (option != '0'):
        print("""
[1]Number inputs
[2]Total
[3]Mean
[4]Median
[5]Mode
[6]Maximum
[7]Minimum
[8]Range
[9]InterQuartile Range
[10]Standard Deviation
[11]Skewness
[12]Total Rental x Temperature Correlation
[13]Total Rental x Wind Speed Correlation
[14]Histogram Temperature
[15]Histogram Rentals
[16]Box Plot Temperature
[17]Box Plot Rentals
[18]Scatter Temperature vs Rentals
[19]Scatter Windspeed vs Rentals
[0]Return to main menu""")
        option = input("Please Select:") 
        
        if (option == '1'):
            print("Number of inputs:", len(total_rentals))
            print()
            continue
               
        if (option == '2'):
            total_rental = stats.calc_sum(total_rentals)
            print("Total " + str(total_rental))
            print()
            continue
        
        if (option == '3'):
            mean_by_day = stats.calc_mean(total_rentals)
            print("Mean "  + str(mean_by_day))
            print()
            continue
        
        if (option == '4'):
            median = stats.calc_median(total_rentals)
            print("Median " + str(median))
            print()
            continue
        
        if (option == '5'):
            mode = stats.calc_mode(total_rentals)
            print("Mode " + str(mode))
            print()
            continue
        
        if (option == '6'):
            max_value = stats.calc_max_value(total_rentals)
            print("Max " + str(max_value))
            print()
            continue
        
        if (option == '7'):
            min_value = stats.calc_min_value(total_rentals)
            print("Min " + str(min_value))
            print()
            continue
        
        if (option == '8'):     
            range_value = stats.calc_range(total_rentals)
            print("Range " + str(range_value))
            print()
            continue

        if (option == '9'):     
            inter_quartile = stats.calc_inter_quartile(total_rentals)
            print("Inter Quartile " + str(inter_quartile))
            print()
            continue

        if (option == '10'):     
            std_deviation = stats.calc_std_deviation(total_rentals)
            print("Standard Deviation", std_deviation)
            print()
            continue

        if (option == '11'):     
            mode_skewness = stats.calc_mode_skewness(total_rentals)
            print("Mode Skewness", mode_skewness)
            print()
            continue

        if (option == '12'):     
            correlation = stats.calc_correlation(total_rentals, temperatures)
            print("Total Rental x Temperature Correlation", correlation)
            print()
            continue     

        if (option == '13'):   
            correlation = stats.calc_correlation(total_rentals, windspeeds)
            print("Total Rental x Wind Speed Correlation", correlation)
            print()
            continue   
        
        if (option == '14'):   
            visualization.plot_histogram(temperatures, "Temperature")
            print()
            continue 
        
        if (option == '15'):   
            visualization.plot_histogram(total_rentals, "Total Rental", 200)
            print()
            continue 
           
        if (option == '16'):   
            visualization.plot_box_plot(temperatures, "Temperature")
            print()
            continue 
            
        if (option == '17'):   
            visualization.plot_box_plot(total_rentals, "Total Rental")
            print()
            continue 
           
        if (option == '18'):   
            visualization.plot_scatter_plot(temperatures, total_rentals, "Temperature", "Total Rental")
            print()
            continue 
        
        if (option == '19'):   
            visualization.plot_scatter_plot(windspeeds, total_rentals, "Wind Speed", "Total Rental")
            print()
            continue 
        

if __name__ == "__main__":
    load_bike_rentals("bike-sharing.csv")
   
    if (len(temperatures) > 0 and len(total_rentals) > 0):
        option = ''
        while (option != 'q'):
            print("""
[N]Analysis by numeric feature
[C]Analysis by Category feature
[Q]uit""")
            option = input("Please Select:").lower()
           
            if (option == 'n'):
                show_numeric_menu()
                continue
            if (option == 'c'):
                show_category_menu()
                continue
                