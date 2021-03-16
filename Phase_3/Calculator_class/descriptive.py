#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
# class Calculator:
#     def __init__(self, data):
#         self.data = data;
#         self.length = len(data)
#         self.mean = self.__calc__mean()
#         self.median = self.__calc__median()
#         self.variance = self.__calc__variance()
#         self.stand_dev = self.__calc__std()
        
#     def __calc__mean(self):
#         mean = sum(self.data)/len(self.data)
#         return mean
    
#     def __calc__median(self):
#         nums = sorted(self.data)
#         if len(nums) % 2 != 0:
#             median = nums[len(nums)//2]
#         else:
#             n1 = nums[len(nums)//2]
#             n2 = nums[len(nums)//2-1]
#             median = (n1+n2)/2
#         return median
    
#     def __calc__variance(self):
#         self.mean
#         var = sum((x-self.mean)**2 for x in self.data) / (len(self.data)-1)
#         return var
    
#     def __calc__std(self):
#         self.mean
#         self.variance
#         std = self.variance **.5
#         return std
    
#     def add_data(self, nums):
#         self.data.extend(nums)
#         self.__init__(self.data)
#         return self
    
#     def remove_data(self, data):
#         for num in data:
#             if num in self.data:
#                 self.data.remove(num)            
#         self.__init__(self.data)
#         return self


class Calculator:
    #init gets called when instance is created
    def __init__(self, data):
        self.data = data;
        self.update_values()
        
    def update_values(self):
        #This function is also defining the attributes
        self.length = len(self.data)
        self.mean = self.__calc__mean()
        self.median = self.__calc__median()
        self.variance = self.__calc__variance()
        self.stand_dev = self.__calc__std()

        
    def __calc__mean(self):
        mean = sum(self.data)/len(self.data)
        return mean
    
    def __calc__median(self):
        nums = sorted(self.data)
        if len(nums) % 2 != 0:
            median = nums[len(nums)//2]
        else:
            n1 = nums[len(nums)//2]
            n2 = nums[len(nums)//2-1]
            median = (n1+n2)/2
        return median
    
    def __calc__variance(self):
        self.mean
        var = sum((x-self.mean)**2 for x in self.data) / (len(self.data)-1)
        return var
    
    def __calc__std(self):
        self.mean
        self.variance
        std = self.variance **.5
        return std
    
    def add_data(self, nums):
        self.data.extend(nums)
        #The update will also recall the attributes after the extend
        self.update_values()
    
    def remove_data(self, data):
        for num in data:
            if num in self.data:
                self.data.remove(num)
        #The update will also recall the attributese after the remove
        self.update_values()
     





