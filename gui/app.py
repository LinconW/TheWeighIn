import tkinter as tk
from tkinter import font
from core.WeightPlot import WeightPlot

HEIGHT = 300
WIDTH = 600

class TheWeighInGUI:
    
    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("TheWeighIn")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.build_ui()
    
    def run(self):
        self.root.mainloop()
        
    def build_ui(self):
        
        self.title_txt = tk.Label(self.root, text="The Weigh In", font=font.Font(size=24))
        self.title_txt.pack()
       
        # Frames
        self.menu_frame = tk.Frame(self.root)
        self.entry_frame = tk.Frame(self.root)
        self.averages_frame = tk.Frame(self.root)
        self.delete_entry_frame = tk.Frame(self.root)
        
        # ------------ Menu Widgets ------------
        self.enter_entry_button = tk.Button(self.menu_frame, text="Enter Entry", command=self.enter_entry_forum)
        self.enter_entry_button.pack()
        
        self.show_averages_button = tk.Button(self.menu_frame, text="Calculate Averages", command=self.averages_forum) # averages will eventually have user inputted range. (1 week average, all time avg)
        self.show_averages_button.pack()
        
        self.show_graph_button = tk.Button(self.menu_frame, text = "Show Graph", command=self.show_graph)
        self.show_graph_button.pack()
        
        self.delete_entry_button = tk.Button(self.menu_frame, text="Delete Entry", command=self.delete_entry_forum)
        self.delete_entry_button.pack()
        
        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.root.destroy)
        self.quit_button.pack()
        
        #  ------------ Entry Forum Widgets ------------
        tk.Label(self.entry_frame, text="Date (YYYY-MM-DD)").pack()
        self.date_entry = tk.Entry(self.entry_frame)
        self.date_entry.pack()
        tk.Label(self.entry_frame, text="leave blank for today's date", fg="grey", font=font.Font(size=8)).pack()

        # weight input
        tk.Label(self.entry_frame, text="Weight (lbs)").pack()
        self.weight_entry = tk.Entry(self.entry_frame)
        self.weight_entry.pack()

        # calorie input
        tk.Label(self.entry_frame, text="Calories").pack()
        self.calorie_entry = tk.Entry(self.entry_frame)
        self.calorie_entry.pack()

        # Submit button
        self.add_button = tk.Button(self.entry_frame, text="Add Entry", command=self.submit_entry)
        self.add_button.pack()
        
        # Status Label
        self.status_label = tk.Label(self.entry_frame, text="", fg="grey")
        self.status_label.pack()
        
        # Exit button is universal
        self.exit_button = tk.Button(self.root, text="Exit", command=self.show_menu)
        
        # ------------ Averages Widgets ------------
        
        # TODO create averages API endpoint that accepts a date range
        # TODO add UI controls for preset ranges: 1 week, 1 month, all time
        # TODO call averages endpoint and display returned average weight/calories
        
        self.averages_label = tk.Label(self.averages_frame, text=" ")
        
        # ------------ Delete Entry Widgets ------------
        self.weight_ID_entry = tk.Entry(self.delete_entry_frame)
        self.weight_ID_entry.pack()
        self.delete_button = tk.Button(self.delete_entry_frame, text = "Delete Entry", command=self.delete_entry)
        self.delete_button.pack()
    
        # ------------ Initial Menu Call ------------
        self.show_menu()
    
    def submit_entry(self):
        weight_text = self.weight_entry.get().strip()
        calorie_text = self.calorie_entry.get().strip()
        date_text = self.date_entry.get().strip()

        if not weight_text or not calorie_text:
            self.status_label.config(text="Weight and calories are required.", fg="red")
            return

        try:
            weight = float(weight_text)
            calories = int(calorie_text)
            response = self.client.create_weight_entry(weight, calories, date_text or None)

            if isinstance(response, dict) and response.get("error"):
                self.status_label.config(text=f"Add failed: {response['detail']}", fg="red")
                return
            
            # clear inputs AFTER successful submission
            self.weight_entry.delete(0, tk.END)
            self.calorie_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
        
            self.status_label.config(text="Entry added successfully.", fg="green")

        except ValueError:
            self.status_label.config(text="Invalid input. Weight must be a number and calories must be an integer.", fg="red")
    
    
    # TODO implement line of best fit to show weight trends. 
    # Reduces noise due to weight fluctuations throughout the week.
    def show_graph(self):
        weight_data = self.client.get_weight_entries()

        if isinstance(weight_data, dict) and weight_data.get("error"):
            self.status_label.config(text=f"Graph failed: {weight_data['detail']}", fg="red")
            return

        if not weight_data:
            self.status_label.config(text="No entries to graph.", fg="red")
            return

        weights = [entry["weight"] for entry in weight_data]
        dates = [entry["date"] for entry in weight_data]

        weight_plot = WeightPlot("Date", "Weight", dates, weights)
        weight_plot.show_plot()
        self.status_label.config(text="Graph loaded successfully.", fg="green")
    
    def delete_entry(self):
        delete_id = self.weight_ID_entry.get().strip()

        if not delete_id:
            self.status_label.config(text="Enter an entry ID to delete.", fg="red")
            return

        response = self.client.delete_weight_entry(delete_id)

        if isinstance(response, dict) and response.get("error"):
            self.status_label.config(text=f"Delete failed: {response['detail']}", fg="red")
            return

        self.status_label.config(text="Entry deleted successfully.", fg="green")
        self.weight_ID_entry.delete(0, tk.END)
    
    def calculate_averages(self):
        return
    
    def hide_all_frames(self):
        self.menu_frame.pack_forget()
        self.entry_frame.pack_forget()
        self.averages_frame.pack_forget()
        self.delete_entry_frame.pack_forget()
        self.exit_button.pack_forget()
        
    def show_menu(self):
        self.hide_all_frames()
        self.menu_frame.pack()
        
    def enter_entry_forum(self):
        self.hide_all_frames()
        self.entry_frame.pack()
        self.exit_button.pack()
        
    def averages_forum(self):
        self.hide_all_frames()
        self.averages_frame.pack()
        self.exit_button.pack()
        
    def delete_entry_forum(self):
        self.hide_all_frames()
        self.delete_entry_frame.pack()
        self.exit_button.pack()