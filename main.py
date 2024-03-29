import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from pyscript import document
from pyscript import display

volume = document.querySelector("#volume")
sizeElement = document.querySelector("#size")
mediumTempElement = document.querySelector("#mediumTemp")
objectTempElement = document.querySelector("#objectTemp")

def getK(time1, temp1, mediumTemp, startTemp):
	if time1 == 0:
		return 0;
	return -(np.log((temp1 - mediumTemp)/(startTemp - mediumTemp))/time1)

	

def onSubmit(event):
	# TODO: check for where the graph hits around zero and then decide the range based on that.
	# TODO: Calculate the equations that relates the k values for each shape and size and then use that to calc K.
	# https://education.molssi.org/python-data-analysis/03-data-fitting/index.html
	if isinstance(float(sizeElement.value), (float, int)) == False:
		return
	
	if isinstance(float(mediumTempElement.value), (float, int)) == False:
		return

	if isinstance(float(objectTempElement.value), (float, int)) == False:
		return

	size = float(sizeElement.value)
	mediumTemp = float(mediumTempElement.value)
	startTemp = float(objectTempElement.value)
	if size <= 0 or size > 10:
		return

	K = .01;

	t = np.arange(0.0,24.0 * 60.0,1.0)
	s = mediumTemp + (startTemp - mediumTemp) * np.exp(-K*t)

	fig, ax = plt.subplots()

	ax.plot(t,s)

	ax.set(xlabel = "time (m)", ylabel = "Temperature(F)", title = volume.value)

	ax.grid

	plot = document.querySelector("#plot")
	plot.innerHTML = ""

	display(fig, target = "plot")