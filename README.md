# Communication Contract (Round 2)
- **For which teammate did you implement “Microservice A”?**
<br />Stormi - Confirmation

- **What is the current status of the microservice? Hopefully, it’s done!**
<br />The microservice is finished. It just needs to be implemented into their own respectable program and edited to handle the remaining tasks

- **How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is your microservice hosted somewhere? Etc.**
<br />The link to the github is provided in S2.6 Discussion post and will be sent directly once finished. It can run locally.

- **If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?**
<br />I would ensure that all the required libraries are installed FIRST. If they do need help, I am available anytime after 5:30PM PST M-F and most of the weekend. I am pretty busy and have some family things going on at the moment, so my accessibility to my laptop may be limited, however, I am very quick to respond and I’m able to give the assistance as needed (even while at work). 

- **If your teammate cannot access/call your microservice, by when do they need to tell you?**
<br />ASAP. I want to be able to help my team as much as I can. When I joined this group, I told everyone about transparency. There are no dumb questions on the road to success! We are a team so I am here to help

- **Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?**
<br />Since the primary focus of this microservice is handling user authentication and session management I have just inserted an example call for getting tasks. I am assuming that this will be implemented by another microservice and later tied into my microservice.

# How to request/retreive data
Users will interact with the coordinating .json file. In my case, I used users2.json. In the case the .json file does not exist, the program will create the file using loadData.
```ruby
def loadData():
    if os.path.exists(dataBase):
        with open(dataBase, "r") as file:
            return json.load(file)
        
    return {"clients": [], "photoshoots": []}
```
The microservice will then write data back to the file and save for future use (saveInfo)

```ruby
def saveInfo(data):
    with open(dataBase, "w") as file:
        json.dump(data, file, indent=4)
```

The program has 3 main API endpoints: 

<br />**REQUEST to add a new client**
<br /> 
- the microservice will be requesting users to enter a name, email, and phone number, which be written into users2.json
- This will handle the first endpoint, POST /clients
- when the microservice reads user input, it will process the input and add everything to users2.json
```ruby
def tAddClient(success=True):
    clientData = {
        "name": "Kaye Dela Chica" if success else "CANCEL",
        "email": "delachic@oregonstate.edu",
        "phone": "123-456-7890"
    }

    response = requests.post(f"{listenHere}/clients", json=clientData)
    print(f"\nTesting Add Client ({'Success' if success else 'Cancel'}):", response.json())
    print(f"Status Code: {response.status_code}, Response: {response.json()}")
```
- As a programmer, you will edit the code to allow users to manually test it themselves
- If the entry is successful, the status code will respond with a 201 code, whereas an unsuccessful entry (or cancel) will output a 400 status code. 
![Image](https://github.com/user-attachments/assets/c5e85da2-0153-44ef-b919-ff80009d4b5b)

<br />**REQUEST new Photoshoot**
<br /> 
- This works similar to clients. the microservice will be requesting users to enter a name, email, and phone number, which be written into users2.json. This will handle the second endpoint POST /photoshoots.
- this will return a confirmation and cancelation message like /clients
```ruby
def tAddPS(success=True):
    psData = {
        "client": "Kaye Dela Chica" if success else "CANCEL",
        "date": "2025-03-05",
        "time": "12:00",
        "location": "Portland"
    }

    response = requests.post(f"{listenHere}/photoshoots", json=psData)

    print(f"\nTestinf Add Photoshoot ({'Success' if success else 'Cancel'}):", response.json())
    print(f"Status Code: {response.status_code}, Response: {response.json()}")
```
- similar to clients, test2.py's tAddPS sends data if true, assuming it was false, the data returns as canceled, outputting a 400 error code. 
![Image](https://github.com/user-attachments/assets/66bc100f-c3a1-4d27-9f33-7dc0754af3e5)

<br />**RETRIEVE appointments**
<br />
- the microservice will retrieve the data from users2.json. tViewAppt() will send a GET request and will retrieve all the scheduled appts from users2.json.
```ruby
stormiServ.py
@app.route("/appts", methods=["GET"])
def viewAppt():
    data = loadData()
    numAppt = len(data["photoshoots"])
    return jsonify({
        "total appts": numAppt,
        "appointments": data["photoshoots"]
    })
```
We can use a CURL request to output to send a request to test. Successful, the code displays a 200 status code!  
```ruby
curl.exe -X GET http://127.0.0.1:5000/appts
```
![Image](https://github.com/user-attachments/assets/84768ec3-44f9-4c01-9beb-bdea52b1bd75)

# UML
![Image](https://github.com/user-attachments/assets/c1f5bf72-ca80-4c24-bae8-117777c521c0)
