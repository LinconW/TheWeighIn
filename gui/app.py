import tkinter as tk

class TheWeighInGUI:
    
    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("TheWeighIn")
        self.root.geometry("400x300")
        self.build_ui()
    
    def run(self):
        self.root.mainloop()
        
        
    # TODO Add labels, error messages, and disable submission on invalid input
    # TODO Add Tkinter Labels and inline validation feedback for weight/calories inputs    def build_ui(self):
    def build_ui(self):
        # Weight label + entry
        tk.Label(self.root, text="Weight (lbs)").pack()
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        # Calories label + entry
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


    def bind_events(self):
        pass
    
    def submit_entry(self):
        weight_text = self.weight_entry.get().strip()
        calorie_text = self.calorie_entry.get().strip()

        if not weight_text or not calorie_text:
            print("Empty fields")
            return

        try:
            weight = float(weight_text)
            calories = int(calorie_text)

            self.client.create_weight_entry(weight, calories)

            # clear inputs AFTER successful submission
            self.weight_entry.delete(0, tk.END)
            self.calorie_entry.delete(0, tk.END)

        except ValueError:
            print("Invalid input")