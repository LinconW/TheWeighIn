from gui.app import TheWeighInGUI
from client.weighin_client import WeighInClient

BASE_URL = "http://127.0.0.1:8000"

def main():
    client = WeighInClient(BASE_URL)
    application = TheWeighInGUI(client)
    application.run()
    

if __name__ == "__main__":
    main()