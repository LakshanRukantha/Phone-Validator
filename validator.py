from ast import If
import requests
import time

mnumber = input("Enter your mobile number with country code : ")

url = "https://veriphone.p.rapidapi.com/verify"

querystring = {"phone":mnumber}

headers = {
	"X-RapidAPI-Host": "veriphone.p.rapidapi.com",
	"X-RapidAPI-Key": "{ENTER YOUR API KEY}"
}

response = requests.request("GET", url, headers=headers, params=querystring)

status = response.json()["status"]
country = response.json()["country"]
country_code = response.json()["country_code"]
phone_region = response.json()["phone_region"]
country_prefix = response.json()["country_prefix"]
phone = response.json()["phone"]
phone_valid = response.json()["phone_valid"]
phone_type = response.json()["phone_type"]
carrier = response.json()["carrier"]
international_number = response.json()["international_number"]
local_number = response.json()["local_number"]

if status != "success":
    print("Network Error! Please Try Again Later.")
    exit()
if phone_valid == True:
    phone_valid = "Valid Number"
if phone_valid == False:
    phone_valid = "Invalid Number"
    phone_region = "unknown"
    carrier = "unknown"

print("Country : " + country),time.sleep(0.4),
print("Country Code : " + country_code),time.sleep(0.4),
print("Phone Region : " + phone_region),time.sleep(0.4),
print("Country Prefix : " + country_prefix),time.sleep(0.4),
print("Phone Number : " + phone),time.sleep(0.4),
print("Status : " + phone_valid),time.sleep(0.4),
print("Phone Type : " + phone_type),time.sleep(0.4),
print("Carrier : " + carrier),time.sleep(0.4),
print("International Number : " + international_number),time.sleep(0.4),
print("Local Number : " + local_number)
