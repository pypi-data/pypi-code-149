import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

workDir = os.path.dirname(os.path.abspath(__file__))

class createGraph:
	def __init__(self, data):
		self.data = data
		self.columns = self.data.columns
	
	def graph(self):
		for idx, el in enumerate(self.data.columns):
			print(idx, el)
		xAxis = int(input("Enter the column number for x-axis: "))
		yAxis = int(input("Enter the column number for y-axis: "))
		title = input("Title of the graph: ")
		xValues = self.data.iloc[:,xAxis]
		yValues = self.data.iloc[:,yAxis]
		
		plt.plot(xValues, yValues)
		plt.xlabel(self.columns[xAxis], fontsize=22)
		plt.ylabel(self.columns[yAxis], fontsize=22)
		plt.title(title, weight='bold', fontsize=24)
		plt.show()
		
def main():
	if len(sys.argv) > 1:
		fileName = pd.read_csv(os.path.join(workDir,sys.argv[1]))
	else:
		fileName = pd.read_csv(os.path.join(dataPath,'fgvt-steering-data.csv'))
	graphObject = createGraph(fileName)
	graphObject.graph()

if __name__ == '__main__':
	main()
