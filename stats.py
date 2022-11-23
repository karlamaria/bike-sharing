#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:52:03 2022

@author: kgarcia03

Student ID: A00304376

Calculates all metrics
"""

import math

def calc_sum(input_list): 
    """
    Calculate the sum of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The sum of all the elements in the list.
    """
    return(sum(input_list))

def calc_mean(input_list): 
    """
    Calculate the mean of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The mean of all the elements in the list.
    """
    mean = sum(input_list) / len(input_list)
    return(round(mean,2))

def calc_median(input_list): 
    """
    Calculate the median of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The median of list.
    """
    sorted_list = sorted(input_list)
    mid_index = int(len(sorted_list)/2)

    #Checks if list size is even or odd
    if (len(sorted_list) % 2 == 1):
        median = sorted_list[mid_index]
    else:
        median = (sorted_list[mid_index-1] + sorted_list[mid_index]) / 2
        
    return median

def calc_mode(input_list):
    """
    Calculate the mode of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The mode of list.
    """
    frequencies = {}
    for number in input_list:
        #Increments the frequency if key already exist or add it
        frequencies[number] = frequencies.get(number, 0) + 1
    
    mode = max(frequencies, key=frequencies.get)
    
    return mode

def calc_max_value(input_list):
    """
    Calculate the max value in the list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The max value in the list.
    """
    return max(input_list)

def calc_min_value(input_list):
    """
    Calculate the min value in the list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The min value in the list.
    """
    return min(input_list)

def calc_range(input_list):
    """
    Calculate the range of the list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The range of the list.
    """
    return calc_max_value(input_list) - calc_min_value(input_list)

def calc_inter_quartile(input_list):
    """
    Calculate the Inter Quartile of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The Inter quartile of list.
    """
    sorted_list = sorted(input_list)
    mid_index = int(len(sorted_list) / 2)

    #Checks if list size is even or odd
    if(len(input_list) % 2 == 1):
        q1 = calc_median(sorted_list[:mid_index])
        q3 = calc_median(sorted_list[mid_index+1:])
    else:
        q1 = calc_median(sorted_list[:mid_index])
        q3 = calc_median(sorted_list[mid_index:])
    
    return q3 - q1

def calc_std_deviation(input_list):
    """
    Calculate the Standard Deviation of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The Standard Deviation of list.
    """
    mean = calc_mean(input_list)
    n = len(input_list)
    
    squared_deviations = [(x - mean) ** 2 for x in input_list]
    sum_dev = sum(squared_deviations)
    
    variance = sum_dev / (n - 1)
    
    return round(math.sqrt(variance),2)

def calc_mode_skewness(input_list):
    """
    Calculate the mode skewness of list
    
    Parameters
    ----------
    input_list: list
        List of numbers.
    
    Returns
    -------
    float
        The mode skewness of list.
    """
    mean = calc_mean(input_list)
    mode = calc_mode(input_list)
    deviation = calc_std_deviation(input_list)
    
    return round(((mean - mode) / deviation), 2)

def calc_correlation(x_values, y_values):
    """
    Calculate the correlation between two lists
    
    Parameters
    ----------
    x_values: list
        x list of numbers.
    y_values: list
        y list of numbers.
    
    Returns
    -------
    float
        The correlation between the two input lists.
    """
    x_mean = calc_mean(x_values)
    y_mean = calc_mean(y_values)
    
    x_deviations = [x - x_mean for x in x_values]
    y_deviations = [y - y_mean for y in y_values]

    #For each tuple, multiply the items of the two lists
    xy_deviations = [ x*y for (x,y) in zip(x_deviations,y_deviations)]
    
    x_squared_deviations = [x ** 2 for x in x_deviations]
    y_squared_deviations = [y ** 2 for y in y_deviations]
    
    correlation = sum(xy_deviations) / (math.sqrt(sum(x_squared_deviations)) * math.sqrt(sum(y_squared_deviations)))
    
    return round(correlation,2)

def get_max_total(input_dict):
    """
    Returns item with max total value
    
    Parameters
    ----------
    input_dict: dict
        dictionary category > total
    
    Returns
    -------
    String
        Category with max value.
    String
        Max value.
    """
    # Find key with max value
    max_category = max(input_dict, key=input_dict.get)
    return str(max_category), str(input_dict[max_category])
    
def get_min_total(input_dict):
    """
    Returns item with min total value
    
    Parameters
    ----------
    input_dict: dict
        dictionary category > total
    
    Returns
    -------
    String
        Category with min value.
    String
        Min value.
    """
    # Find key with min value
    min_category = min(input_dict, key=input_dict.get)
    return str(min_category), str(input_dict[min_category])

def get_max_item(categories, values):
    """
    Returns item with max value
    
    Parameters
    ----------
    categories: list
        list of categories
    values: list
        list of values
    
    Returns
    -------
    String
        Category with max value
    String
        Min Value.
    """
    # Find the max value of the list
    max_value = max(values)
    # Get its index
    max_value_index = values.index(max_value)
    return str(categories[max_value_index]), str(max_value) 

def get_min_item(categories, values):
    """
    Returns item with min value
    
    Parameters
    ----------
    categories: list
        list of categories
    values: list
        list of values
    
    Returns
    -------
    String
        Category with min value
    String
        Min Value.
    """
    # Find the min value of the list
    min_value = min(values)
    # Get its index
    min_value_index = values.index(min_value)
    return str(categories[min_value_index]), str(min_value) 