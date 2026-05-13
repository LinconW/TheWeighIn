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

        dates = [dt.strptime(date, "%Y-%m-%d") for date in self.x_ax]
        x_numeric = mdates.date2num(dates)
        slope, intercept = np.polyfit(x_numeric, self.y_ax, 1)
        trend_line = slope * x_numeric + intercept

        plt.figure()
        plt.title(f"{self.x_title} vs {self.y_title}")
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        plt.plot(dates, self.y_ax, marker="o", label="Actual Weight")
        plt.plot(dates, trend_line, label="Trend Line")
        plt.xticks(dates)
        plt.gca().xaxis.set_major_formatter(
            mdates.DateFormatter('%Y-%m-%d')
        )

        plt.gcf().autofmt_xdate()

        plt.legend()

    def show_plot(self):
         plt.show()

