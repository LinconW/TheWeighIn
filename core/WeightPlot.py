import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime as dt # changing dates and times to actual computable strings

class WeightPlot():

    def __init__(self, x_title, y_title, x_ax, y_ax):
        self.x_title = x_title
        self.y_title = y_title
        self.x_ax = x_ax
        self.y_ax = y_ax
        self.create_figure()
       
    def create_figure(self):
        plt.figure()
        plt.title(f"{self.x_title} vs {self.y_title}")
        plt.xlabel(f"{self.x_title}")
        plt.ylabel(f"{self.y_title}")
        plt.plot(self.x_ax, self.y_ax)

    def show_plot(self):
         plt.show()

