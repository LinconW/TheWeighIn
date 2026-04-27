# from DataController import DataController
# from WeightPlot import WeightPlot
# from datetime import datetime as dt # changing dates and times to actual computable strings
# import csv
# import sys
# import os

# FILE_PATH = "weights.csv"
# FIELDS = ["date", "weight", "calories"]

# def check_csv():
#     if not os.path.isfile(FILE_PATH):
#         with open(FILE_PATH, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=FIELDS)
#         writer.writeheader()

# def menu():
#     print("******** TheWeighIn ********")
#     print("1.Load Weight Data")
#     print("2.View Weight Trends")
#     print("3.Enter Weight Data")
#     print("9.Quit")

# # ======================================
# # *************** MAIN *****************
# # ======================================
# def main():

#     user_x = "No Data Loaded"
#     user_y = "No Data Loaded"
#     x_axis = []
#     y_axis = []

#     check_csv()
#     weight_data = DataController(FILE_PATH)

#     #Prints menu only once
#     menu()
#     while True:
#         user_input = input("Enter a Number: ")

#         # Loads specific axis to graph on a plot
#         if user_input == "1":
#             user_x = input("X axis: ")
#             user_y = input("Y axis: ")
#             if not weight_data.has_column(user_y) or not weight_data.has_column(user_x):
#                 print("Invalid Data Columns...")
#                 continue

#             x_axis = weight_data.read_column(user_x)
#             y_axis = weight_data.read_column(user_y)

#             print(list(zip(x_axis, y_axis)))
#             print(x_axis)
#             print(y_axis)

#         # Creates the plot. If no axis was chosen, it should default to weight vs date
#         elif user_input == "2":
#             if not x_axis or not y_axis:
#                 user_x = "date"
#                 user_y = "weight"
#                 x_axis = weight_data.read_column(user_x)
#                 y_axis = weight_data.read_column(user_y)

#             weight_plot = WeightPlot(user_x, user_y, x_axis, y_axis)
#             weight_plot.show_plot()

#         # Writes to csv file with today's date, users weight, and users calories for the day.
#         elif user_input == "3":
#             user_weight = input("Weight(lbs): ")
#             user_calories = input("Calories(kcal): ")
#             user_date = dt.now().strftime("%Y-%m-%d")

#             weight_dict = {
#                 "date": user_date,
#                 "weight": float(user_weight),
#                 "calories": float(user_calories)
#             }

#             weight_data.add_row(weight_dict)
#         elif user_input == "9":
#             sys.exit()

# if __name__ == "__main__":
#     main()