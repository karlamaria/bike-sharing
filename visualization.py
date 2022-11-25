#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:32:01 2022

@author: kgarcia03

Student ID: A00304376

Plots all charts

"""

import matplotlib.pyplot as plt
def plot_histogram(input_list, feature, step = 1):
    """
    Plots a Histrogram for a list

    Parameters
    ----------
    input_list: list
        List of numbers.
    feature: String
        The feature name to be plotted
    step: [optional] int
        The difference between any two numbers in the sequence.

    Returns
    -------
    None:
        list is plotted in a histragram which is saved in a .png file

    """
    fig, ax = plt.subplots(figsize=(15,10))

    ax.set_title("Histogram")
    ax.set_xlabel(feature)
    ax.set_ylabel("Frequency")

    bins = range(int(min(input_list)-5), int(max(input_list)+5), step)

    ax.set_xticks(bins)
    ax.hist(input_list,bins,ec="black")
    # Change x rotation to better visualize the items
    plt.xticks(rotation=45)
    
    fig.savefig(feature.lower().replace(" ", "_") + "_histogram_visualisations.png")

def plot_box_plot(input_list, feature):
    """
    Plots a Box Plot for a list

    Parameters
    ----------
    input_list: list
        List of numbers.
    feature: String
        The feature name to be plotted

    Returns
    -------
    None:
        list is plotted in a box plot which is saved in a .png file

    """
    fig, ax = plt.subplots(figsize=(15,10))
    
    ax.set_title("Box Plot")
    ax.set_ylabel(feature)
    ax.boxplot(input_list, showmeans=True, meanline=True)
    
    fig.savefig(feature.lower().replace(" ", "_") + "_box_plot_visualisations.png")
    

def plot_scatter_plot(input_list_x, input_list_y, feature_x, feature_y):
    """
    Plots a Scatter Plot for a list

    Parameters
    ----------
    input_list_x: list
        Feature list in the axis x.
    input_list_y: list
        Feature list in the axis y.
    feature_x: String
        The feature name in the axis x
    feature_y: String
        The feature name in the axis y

    Returns
    -------
    None:
        lists are plotted in a scatter plot which is saved in a .png file
"""
    fig, ax = plt.subplots(figsize=(10,15))
    
    ax.set_title(feature_y + " vs " + feature_x)        
    ax.set_xlabel(feature_x)
    ax.set_ylabel(feature_y)
    ax.scatter(input_list_x,input_list_y,marker=".")

    fig.savefig(feature_x.lower().replace(" ", "_") + "_vs_" + feature_y.lower().replace(" ", "_")  + ".png")

def plot_pie_chart(input_dict, feature):
    """
    Plots a Pie chart

    Parameters
    ----------
    input_dict: dict
        Feature dictionary
    feature: String
        The feature name to be plotted

    Returns
    -------
    None:
        dictionary keys/values are plotted in a pie chart which is saved in a .png file

    """
    fig, ax = plt.subplots()
    
    ax.set_title(feature)
    ax.pie(input_dict.values(), labels=input_dict.keys(), autopct="%.f%%")
    ax.plot(input_dict.keys(),input_dict.values())

    fig.savefig(feature.lower().replace(" ", "_") + "_pie_chart.png")

def plot_bar_chart(input_dict, feature_x, feature_y):
    """
    Plots a Bar chart

    Parameters
    ----------
    input_dict: dict
        Feature dictionary
    feature_x: String
        The feature name in the axis x
    feature_y: String
        The feature name in the axis y

    Returns
    -------
    None:
        dictionary keys/values are plotted in a bar chart which is saved in a .png file

    """
    fig, ax = plt.subplots(figsize=(15,10))

    ax.set_title(feature_x)

    ax.set_xlabel(feature_x)
    ax.set_ylabel(feature_y)

    ax.barh(list(input_dict.keys()),input_dict.values())
    for index,value in enumerate(input_dict.values()):
        ax.text(value, index, str(value))
     
    fig.savefig(feature_y.lower().replace(" ", "_") + "_bar_chart.png")

def plot_multiple_box_plot(input_dict, feature_x, feature_y):
    """
    Plots a multiple Box Plot for a dictionary

    Parameters
    ----------
    input_dict: dict
        Dict of categories.
    feature_x: String
        The feature name in the axis x
    feature_y: String
        The feature name in the axis y

    Returns
    -------
    None:
        dictionary keys/values are plotted in a box plot which is saved in a .png file
    """
    fig, ax = plt.subplots(figsize=(15,10))
    
    ax.set_title(feature_x)
    ax.set_xlabel(feature_x)
    ax.set_ylabel(feature_y)
    ax.boxplot(input_dict.values(),labels=input_dict.keys(),
                    showmeans=True, meanline=True)
    
    fig.savefig(feature_x.lower().replace(" ", "_") + "_multiple_box_plot.png")