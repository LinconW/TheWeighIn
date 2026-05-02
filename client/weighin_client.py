import requests

class WeighInClient:
    
    def __init__(self, base_url):
        self.base_url = base_url
        
    def create_weight_entry(self, weight, calories, date=None):
        payload = {
            "weight": weight,
            "calories": calories,
        }
        
        if date:
            payload["date"] = date
                        
        response = requests.post(
            f"{self.base_url}/entries",
            json = payload
        )
        
        if response.status_code not in (200, 201):
            return {
                "error": True,
                "status_code": response.status_code,
                "detail": response.text
            }
        
        return response.json()
        
    def get_weight_entries(self):
        return requests.get(f"{self.base_url}/entries").json()
    
    def delete_weight_entry(self, entry_id):
        response = requests.delete(f"{self.base_url}/entries/{entry_id}")
        
        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "detail": response.text
            }
        return response.json()
    
    # TODO implement REST PUT/PATCH function
    def update_weight_entry(self, entry_id, weight, calories):
        payload = {}

        if weight is not None:
            payload["weight"] = weight

        if calories is not None:
            payload["calories"] = calories

        response = requests.patch(
            f"{self.base_url}/entries/{entry_id}",
            json=payload
        )

        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "detail": response.text
            }

        return response.json()