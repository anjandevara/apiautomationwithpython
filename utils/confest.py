from utils.payloads import *

baseUrl = "https://api.qa.fleet.lynx.carrier.io/coa/v1/api/core2"

endpoints = {
    "sourcelatestdata": "/sourcelatestdata?sourceType=Container",
    "unifiedmodel": "/UnifiedModel?type=Properties"
}

url = f"{baseUrl}{endpoints['sourcelatestdata']}"

payload = {

}
headers = {
    'x-lynx-api-key': 'f8lQTkrHSc9gOddAGqbk2e4Kuw448AMQfHtKI0Uzy6jja7Nq',
    # 'Authorization': 'Basic YWtpbC5qYWxpc2F0Z2lAY2Fycmllci5jb206Q2FycmllckAxMjM='

}
