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

<br />**REQUEST to add a new client**
<br /> 
- the microservice will be requesting users to enter a name, email, and phone number, which be written into users2.json
- This will handle the first endpoint, POST /clients
```ruby
//name: createClient
//desc: receive data on clients to store in .json
void createClient(const string& name, const string& eMail, const string& phoneNum) {
  json clientInfo;
  clientInfo["name"] = name;
  clientInfo["email"] = eMail;
  clientInfo["phoneNum"] = phoneNum;

  ofstream file("fileNameHere.json);
  file.close();
  cout << "Client added";
}
```
- when the microservice reads user input, it will process the input and add everything to fileNameHere.json
- As a programmer, you will edit the code to allow users to manually input it themselves
- if it was successfully made, then the program will display
```
int main() {
  createClient("Kaye DelaChica," "delachic@osu.edu", "503-111-1111");
  return 0;
}
```

<br />**REQUEST new Photoshoot**
<br /> 
- This works similar to createClient. the microservice will be requesting users to enter a name, email, and phone number, which be written into fileNameHere.json.
- this will return a confirmation.
- Create a function prorotype to create a new client
- the function should create a .json request file
```
//name: createPS
//desc: creates photo shoot by collecting information
void createClient(const string& clientName, const string& date, const string& time, const string& locatatoin) {
  json psInfo;
  psInfo["clientName"] = clientName;
  psInfo["date"] = date;
  psInfo["time"] = time;
  psInfo["location"] = location;

  ofstream file("fileNameHere.json);
  file.close();
  cout << "Photoshoot added.\n";
}
```
- when the microservice reads user input, it will process the input and add everything to fileNameHere.json
- As a programmer, you will edit the code to allow users to manually input it themselves
```
int main() {
  psInfo("Kaye DelaChica," "2025-02-23", "09:00", "Downtown Portland");
  return 0;
}
```
<br />**RETRIEVE appointments**
<br />
- for this microservice, when the stored data will be coming from the .json file. In this case, we will be retrieving from fileNameHere.json
- you can program the file and have i read/parse from the file to extract the files.
```
void viewAppt() {
  ifstream file("fileNameHere.json")
  json info;

  if(!file.is_open()) {
    cout << "Error opening .json";
    return;
  }
  file >> data;
  file.close();

  //open file. If iti contains photoshoots, that means its not empty
  if (data.contains("photoshoots") && !data[photoshoots"].empty()) {
    cout << "Current appointments:\n";
    for (const auto& appt : data["photoshoots"]) {
      cout << "- " << appt["date"] << " at " << appt["time"] << " with " << appt["client"] << " at " << appt["location"] << endl;
      }
  } else {
    cout << "No upcoming appointments found.\n";
  }
}
```
- The program will read the fileNameHere.json file and will collect the data.
- this can be applied to clients as well.
- In the .json file, it will store data accordingly (as seen from the raw data file from my code)
```
{
    "clients": [
        {
            "email": "delachic@oregonstate.edu",
            "name": "Kaye Delachica",
            "phone": "503-999-9999"
    ],
    "photoshoots": [
        {
            "client": "Kaye Dela Chica",
            "date": "2025-04-15",
            "location": "Sunset Blvd",
            "time": "09:00"
        }
    ]
}
```
# UML
![Image](https://github.com/user-attachments/assets/c1f5bf72-ca80-4c24-bae8-117777c521c0)
