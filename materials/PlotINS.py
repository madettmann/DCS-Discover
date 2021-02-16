#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:18:32 2020

@author: moule
"""
import matplotlib.pyplot as plt
import os

def GetXY(filename, type='fdsm'):
	x = []
	y = []
	largest = 0
	if type == 'fdsm':
		dftFile = open(filename)
		i = 0
		for line in dftFile:
			if line[1] != '#':
				newData = line.split(',')
				newData = [float(val) for val in newData]
				x.append(newData[0])
				y.append(newData[1])
				if x[-1] > 20 and y[-1] > largest:
					largest = y[-1]
			i = i + 1
		dftFile.close()
		return x, y, largest
	elif type == 'md':
		mdFile = open(filename)
		for line in mdFile:
			newData = line.split()
			newData = [float(val) for val in newData]
			x.append(newData[0])
			y.append(sum(newData[1:]))
			if x[-1] > 20 and y[-1] > largest:
					largest = y[-1]
		mdFile.close()
		return x, y
	elif type == 'exp':
		expFile = open(filename)
		i = 0
		flag = 0
		for line in expFile:
			if i > 0 and line != '\n':
				data = line.split(',')
				if len(data) > 2 and flag == 2:
					x.append(float(data[0]))
					y.append(float(data[1]))	
					if x[-1] > 20 and y[-1] > largest:
						largest = y[-1]
				elif len(data) == 1:
					flag = flag + 1
			i = i + 1
		expFile.close()
		if x[0] > -16.0:
			x = [val * 8.06554 for val in x]
		return x, y, largest

