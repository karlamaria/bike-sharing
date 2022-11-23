#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:40:44 2022

@author: kgarcia03

Test all functions that return a value
"""

import pytest
import stats

def test_calc_sum():
    input_list = [1,2,3]
    assert stats.calc_sum(input_list) == 6
    
def test_calc_mean():
    input_list = [1,2,3]
    assert stats.calc_mean(input_list) == 2
    
def test_calc_median_odd_list():
    input_list = [1,2,3]
    assert stats.calc_median(input_list) == 2
    
def test_calc_median_even_list():
    input_list = [1,2,3,4]
    assert stats.calc_median(input_list) == 2.5
    
def test_calc_mode():
    input_list = [1,2,3,4,4]
    assert stats.calc_mode(input_list) == 4
    
def test_calc_max_value():
    input_list = [1,2,3,4,4,5]
    assert stats.calc_max_value(input_list) == 5
    
def test_calc_min_value():
    input_list = [1,2,3,4,4]
    assert stats.calc_min_value(input_list) == 1
    
def test_calc_range():
    input_list = [1,2,3,4,4]
    assert stats.calc_range(input_list) == 3
    
def test_calc_inter_quartile():
    input_list = [1,2,3,4,4]
    assert stats.calc_inter_quartile(input_list) == 2.5
    
def test_calc_std_deviation():
    input_list = [1,2,3,4,4]
    assert stats.calc_std_deviation(input_list) == 1.3
    
def test_calc_mode_skewness():
    input_list = [1,2,3,4,4]
    assert stats.calc_mode_skewness(input_list) == -0.92
    
def test_calc_correlation():
    x_values = [1,2,3,4]
    y_values = [2,4,6,8]
    assert stats.calc_correlation(x_values, y_values) == 1.0
    
def test_get_max_total():
    input_list = {"a": 2, "b": 3}
    key, value = stats.get_max_total(input_list)
    assert key == "b"
    assert value == "3"
    
def test_get_max_item():
    category_list = ["a", "b"]
    value_list = [2, 3]
    category, value = stats.get_max_item(category_list, value_list)
    assert category == "b"
    assert value == "3"

def test_get_min_item():
    category_list = ["a", "b"]
    value_list = [2, 3]
    category, value = stats.get_min_item(category_list, value_list)
    assert category == "a"
    assert value == "2"
    
if __name__ == "__main__":
    pytest.main([__file__, "-v"])