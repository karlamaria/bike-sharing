#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:50:17 2022
@author: kgarcia03
Student ID: A00304376
Load dataset and Starts the user menu
"""

import stats
import visualization
import sys


temperatures = []
windspeeds = []
total_rentals = []
weathersits = []
weathersit_dict = {}
season_rentals_dict = {}
season_temp_dict = {}
weekday_dict = {}

def load_bike_rentals(filename):
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
    try:
        with open(filename) as data_file:
            # read in the column headers and ignore  
            headers = data_file.readline()
            # reads file by line
            for line in data_file:
                # split into components        
                date_string, season, weekday, weathersit, temp, windspeed, total_rental, casual, registered, month, holiday = line.split(",")

                # Populates lists and dictionaries
                temperatures.append(float(temp))
                windspeeds.append(float(windspeed))
                total_rentals.append(int(total_rental))
                weathersits.append(weathersit)
                
                weathersit_dict[weathersit] = weathersit_dict.get(weathersit,0) + int(total_rental)
                weekday_dict[weekday] = weekday_dict.get(weekday,0) + int(total_rental)

                if season not in season_rentals_dict:
                    season_rentals_dict[season] = [int(total_rental)]
                    season_temp_dict[season] = [float(temp)]
                else:
                    season_rentals_dict[season].append(int(total_rental))
                    season_temp_dict[season].append(float(temp))
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IsADirectoryError as dir_error:
        print(dir_error)
    except PermissionError as permission_error:
        print(permission_error)
        
def show_category_menu():
    """
    Analyse by Category Menu
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    option = ''
    while (option != '0'):
        print("""
[1]Weathersit Metrics
[2]Weathersit sub category Metrics
[3]Weathersit Visualisation
[4]Season Visualisation
[5]Weekday Visualisation
[0]Return to main menu""")
        option = input("Please Select:")
            
        if (option == '1'):
            most_freq_category, most_freq_category_value = stats.get_most_frequent(weathersits)
            less_freq_category, less_freq_category_value = stats.get_less_frequent(weathersits)

            print("Weathersit                                     Name of categorical Variable")
            print(f"Number of Subcategories                 {len(weathersit_dict):>20}")
            print(f"Subcategory with highest frequency      {most_freq_category:>20} ({most_freq_category_value:.2f})")
            print(f"Subcategory with lowest frequency       {less_freq_category:>20} ({less_freq_category_value:.2f})")
            print()
            continue

        if (option == '2'):
            highest_total, highest_total_value = stats.get_max_total(weathersit_dict)
            lowest_total, lowest_total_value = stats.get_min_total(weathersit_dict)

            print("Analysis by Category                                  Weathersit")
            print(f"Subcategory with highest total      {highest_total:>20} ({highest_total_value:.2f})")
            print(f"Subcategory with lowest total       {lowest_total:>20} ({lowest_total_value:.2f})")
            print()
            continue

        if (option == '3'):
            visualization.plot_pie_chart(weathersit_dict, "Weathersit")
            visualization.plot_bar_chart(weathersit_dict, "Rentals", "Weathersit")
            print("Charts saved")
            print()
            continue
                        
        if (option == '4'):
            visualization.plot_multiple_box_plot(season_rentals_dict, "Season", "Total Rental")
            visualization.plot_histogram(season_temp_dict["summer"], "Summer")
            visualization.plot_histogram(season_temp_dict["springer"], "Springer")
            visualization.plot_histogram(season_temp_dict["fall"], "Fall")
            visualization.plot_histogram(season_temp_dict["winter"], "Winter")
            print("Charts saved")
            print()
            continue

        if (option == '5'):
            visualization.plot_pie_chart(weekday_dict, "Weekday")
            print("Chart saved")
            print()
            continue

def show_numeric_menu():
    """
    Numeric Columns Menu
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    option = ''
    while (option != '0'):
        print("""
[1]Total Rentals and Temperature Metrics
[2]Total Rentals Visualisation
[3]Temperature Visualisation
[4]Total Rentals and Temperature Visualisation
[5]Total Rentals and Windspeed Visualisation
[0]Return to main menu""")
        option = input("Please Select:") 
        
        if (option == '1'):
            correlation = stats.calc_correlation(total_rentals, temperatures)

            total_rentals_len = len(total_rentals)
            total_rental_sum = stats.calc_sum(total_rentals)
            total_rentals_mean_by_day = stats.calc_mean(total_rentals)
            total_rentals_median = stats.calc_median(total_rentals)
            total_rentals_mode = stats.calc_mode(total_rentals)
            total_rentals_max_value = stats.calc_max_value(total_rentals)
            total_rentals_min_value = stats.calc_min_value(total_rentals)
            total_rentals_range_value = stats.calc_range(total_rentals)
            total_rentals_inter_quartile = stats.calc_inter_quartile(total_rentals)
            total_rentals_std_deviation = stats.calc_std_deviation(total_rentals)
            total_rentals_mode_skewness = stats.calc_mode_skewness(total_rentals)
            total_rentals_median_skewness = stats.calc_median_skewness(total_rentals)

            temperatures_len = len(temperatures)
            temperatures_sum = stats.calc_sum(temperatures)
            temperatures_mean_by_day = stats.calc_mean(temperatures)
            temperatures_median = stats.calc_median(temperatures)
            temperatures_mode = stats.calc_mode(temperatures)
            temperatures_max_value = stats.calc_max_value(temperatures)
            temperatures_min_value = stats.calc_min_value(temperatures)
            temperatures_range_value = stats.calc_range(temperatures)
            temperatures_inter_quartile = stats.calc_inter_quartile(temperatures)
            temperatures_std_deviation = stats.calc_std_deviation(temperatures)
            temperatures_mode_skewness = stats.calc_mode_skewness(temperatures)
            temperatures_median_skewness = stats.calc_median_skewness(temperatures)

            print("                              Total Rentals           Temperature")
            print(f"Number of values        {total_rentals_len:>20}{temperatures_len:>20}")
            print(f"Total                   {total_rental_sum:>20}{temperatures_sum:>20,.2f}")
            print(f"Mean                    {total_rentals_mean_by_day:>20,.2f}{temperatures_mean_by_day:>20,.2f}")
            print(f"Median                  {total_rentals_median:>20,.2f}{temperatures_median:>20,.2f}")
            print(f"Mode                    {total_rentals_mode:>20,.2f}{temperatures_mode:>20,.2f}")
            print(f"Maximum                 {total_rentals_max_value:>20,.2f}{temperatures_max_value:>20,.2f}")
            print(f"Minimum                 {total_rentals_min_value:>20,.2f}{temperatures_min_value:>20,.2f}")
            print(f"Range                   {total_rentals_range_value:>20,.2f}{temperatures_range_value:>20,.2f}")
            print(f"Inter-Quartile Range    {total_rentals_inter_quartile:>20,.2f}{temperatures_inter_quartile:>20,.2f}")
            print(f"Standard Deviation      {total_rentals_std_deviation:>20,.2f}{temperatures_std_deviation:>20,.2f}")
            print(f"Media Skewness          {total_rentals_median_skewness:>20,.2f}{temperatures_median_skewness:>20,.2f}")
            print(f"Mode Skewness           {total_rentals_mode_skewness:>20,.2f}{temperatures_mode_skewness:>20,.2f}")
            print(f"Correlation                        {correlation:>20,.2f}")
            print()
            continue

        if (option == '2'):
            visualization.plot_histogram(total_rentals, "Total Rentals", 200)
            visualization.plot_box_plot(total_rentals, "Total Rentals")
            print("Charts saved")
            print()
            continue

        if (option == '3'):
            visualization.plot_histogram(temperatures, "Temperature")
            visualization.plot_box_plot(temperatures, "Temperature")
            print("Charts saved")
            print()
            continue

        if (option == '4'):
            visualization.plot_scatter_plot(temperatures, total_rentals, "Temperature", "Total Rental")
            print("Chart saved")
            print()
            continue

        if (option == '5'):
            visualization.plot_scatter_plot(windspeeds, total_rentals, "Windspeed", "Total Rental")
            print("Chart saved")
            print()
            continue

def show_main_menu():
    """
    Shows main menu
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    #Do nothing if there are no rentals
    if (len(total_rentals) > 0):
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

if __name__ == "__main__":
    load_bike_rentals("bike-sharing.csv")
    show_main_menu()
                