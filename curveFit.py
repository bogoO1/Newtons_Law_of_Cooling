import scipy
from scipy.optimize import curve_fit
import numpy as np
import json
import matplotlib
import matplotlib.pyplot as plt
from pyscript import document
from pyscript import display
import csv

csv_reader = {}

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

line_count = 0
for row in csv_reader:
	if line_count == 0:
		print(f'Column names are {", ".join(row)}')
		line_count += 1
		continue
	print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
	line_count += 1
print(f'Processed {line_count} lines.')

# line_count = 0
# columnNames = {}
# for row in csv_reader:
# 	if line_count == 0:
# 		print(f'Column names are {", ".join(row)}')
# 		columnNames = row
# 		line_count += 1
# 		continue

	

# convert the code into k values.

# xdata = [ -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
# ydata = [1.2, 4.2, 6.7, 8.3, 10.6, 11.7, 13.5, 14.5, 15.7, 16.1, 16.6, 16.0, 15.4, 14.4, 14.2, 12.7, 10.3, 8.6, 6.1, 3.9, 2.1]

# #Recast xdata and ydata into numpy arrays so we can use their handy features
# xdata = np.asarray(xdata)
# ydata = np.asarray(ydata)

# fig, ax = plt.subplots()


# ax.plot(xdata, ydata, 'o')

# def Gauss(x, A, B):
#     y = A*np.exp(-1*B*x**2)
#     return y

# parameters, covariance = curve_fit(Gauss, xdata, ydata)
# fit_A = parameters[0]
# fit_B = parameters[1]
# print(fit_A)
# print(fit_B)

# fit_y = Gauss(xdata, fit_A, fit_B)
# ax.plot(xdata, ydata, 'o', label='data')
# ax.plot(xdata, fit_y, '-', label='fit')
# ax.legend()

# plot = document.querySelector("#curveFit")
# plot.innerHTML = ""


# display(fig, target = "curveFit")