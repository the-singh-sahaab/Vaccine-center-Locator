# project using APIs and request 
#using cowwin api to demonstrate the avaialibity of vaccince


import requests
PINCODE = int(input("enter your city's pincode=>"))
REQ_DATE = input("enter the date [ make sure it's in form :(dd-mm-yyyy)]=>")
request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
responce = requests.get(request_link, headers = header)
raw_JSON = responce.json()

Total_centers = len(raw_JSON['centers'])
print ()
print ("                        *>>>>>>    RESULTS   <<<<<<<*                                ")
print ("-------------------------------------------------------------------------------------")
print (f"Date: {REQ_DATE} | Pincode: {PINCODE} ")

# print(raw_JSON)
if Total_centers != 0:
    print (f"Total centers in your area is: {Total_centers}" )
else:
    print (f"Unfortunately !! Seems like no center in this area / Kindly re-check the Pincode" )

print ("------------------------------------------------------------------------------------")
print ()

for cent in range(Total_centers):
    print ()
    print (f"[{cent+1}] Center Name:", raw_JSON['centers'][cent]['name'])
    print ("------------------------------------------------------------")
    print ("   Date      Vaccine Type    Minimum Age    Available ")
    print ("  ------     -------------   ------------   ----------")
    this_session = raw_JSON['centers'][cent]['sessions']
    
    for _sess in range(len(this_session)):
        print ( "{0:^12} {1:^12} {2:^14} {3:^16} ".format(this_session[_sess]['date'], this_session[_sess]['vaccine'], this_session[_sess]['min_age_limit'], this_session[_sess]['available_capacity']))