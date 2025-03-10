import requests

#server it is running on. 
listenHere = "http://127.0.0.1:5000"

#this will test ADDING a client/Cancel.
#true sends data to .json and false is Client canceled
def tAddClient(success=True):
    clientData = {
        "name": "Kaye Dela Chica" if success else "CANCEL",
        "email": "delachic@oregonstate.edu",
        "phone": "123-456-7890"
    }

    response = requests.post(f"{listenHere}/clients", json=clientData)

    print(f"\nTesting Add Client ({'Success' if success else 'Cancel'}):", response.json())
    print(f"Status Code: {response.status_code}, Response: {response.json()}")

#this will test ADDING a photoshoot(booking)/Cancel.
#same here, true sends data to .json and false is Client canceled
def tAddPS(success=True):
    psData = {
        "client": "Kaye Dela Chica" if success else "CANCEL",
        "date": "2025-03-05",
        "time": "12:00",
        "location": "Porland"
    }

    response = requests.post(f"{listenHere}/photoshoots", json=psData)

    print(f"\nTestinf Add Photoshoot ({'Success' if success else 'Cancel'}):", response.json())
    print(f"Status Code: {response.status_code}, Response: {response.json()}")

def tViewAppt():
    response = requests.get(f"{listenHere}/appts")
    data = response.json()

    print(f"\nTest View appts (Status Code {response.status_code}):", data)


# Run all tests
if __name__ == "__main__":
    print("\n~~~~~~ TEST RUN HERE ~~~~~~\n")
    

    tAddClient(success=True)
    tAddClient(success=False)

    tAddPS(success=True)
    tAddPS(success=False)

    tViewAppt()
