from datetime import date  #changing dates and times to actual computable strings
import requests

class WeighInClient:
    
    def __init__(self, base_url):
        self.base_url = base_url
        
        
    # TODO Check Response Status for all REST implementations
    def create_weight_entry(self, weight, calories):
        return requests.post(
            f"{self.base_url}/entries",
            json={
                "weight": weight,
                "calories": calories,
                "date": str(date.today())
            }
        ).json()
        
    def get_weight_entries(self):
        return requests.get(f"{self.base_url}/entries").json()
    
    
    # TODO implement REST DELETE function
    def delete_weight_entry(self, entry_id):
        return
    
    # TODO implement REST PUT/PATCH function
    def update_weight_entry(self, entry_id, weight, calories):
        return
        