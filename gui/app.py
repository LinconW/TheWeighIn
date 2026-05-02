import tkinter as tk
from tkinter import font
from core.WeightPlot import WeightPlot

class TheWeighInGUI:
    
    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("TheWeighIn")
        self.root.geometry("400x300")
        self.build_ui()
    
    def run(self):
        self.root.mainloop()
        
    def build_ui(self):
        
        # date input
        tk.Label(self.root, text="Date (YYYY-MM-DD)").pack()
        self.date_entry = tk.Entry(self.root )
        self.date_entry.pack()
        tk.Label(self.root, text="leave blank for today's date", fg="grey", font=font.Font(size=8)).pack()

        
        # weight input
        tk.Label(self.root, text="Weight (lbs)").pack()
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        # calorie input
        tk.Label(self.root, text="Calories").pack()
        self.calorie_entry = tk.Entry(self.root)
        self.calorie_entry.pack()

        # Submit button
        self.add_button = tk.Button(
            self.root,
            text="Add Entry",
            command=self.submit_entry
            )
        self.add_button.pack()
        
        # Show Graph button
        self.show_graph_button = tk.Button(
            self.root,
            text = "Show Graph",
            command=self.show_graph
        )
        self.show_graph_button.pack()
        
        # Delete Entry button
        self.weight_ID_entry = tk.Entry(self.root)
        self.weight_ID_entry.pack()
        self.delete_entry_button = tk.Button(
            self.root,
            text = "Delete Entry",
            command=self.delete_entry
        )
        self.delete_entry_button.pack()

    def bind_events(self):
        pass
    
    def delete_entry(self):
        delete_id = self.weight_ID_entry.get().strip()
        self.client.delete_weight_entry(delete_id)
    
    def show_graph(self):
        weight_data = self.client.get_weight_entries()
        print(weight_data)
        weights = [entry["weight"] for entry in weight_data]
        dates = [entry["date"] for entry in weight_data]
        weight_plot = WeightPlot("Date", "Weight", dates, weights)
        weight_plot.show_plot()
        
    def submit_entry(self):
        weight_text = self.weight_entry.get().strip()
        calorie_text = self.calorie_entry.get().strip()
        date_text = self.date_entry.get().strip()

        if not weight_text or not calorie_text:
            print("Empty fields")
            return

        try:
            weight = float(weight_text)
            calories = int(calorie_text)

            self.client.create_weight_entry(weight, calories, date_text or None)

            # clear inputs AFTER successful submission
            self.weight_entry.delete(0, tk.END)
            self.calorie_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)

        except ValueError:
            print("Invalid input")