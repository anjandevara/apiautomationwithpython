from utils.payloads import *

baseUrl = ""

endpoints = {
    "sourcelatestdata": "/sourcelatestdata?sourceType=Container",
    "unifiedmodel": "/UnifiedModel?type=Properties"
}

url = f"{baseUrl}{endpoints['sourcelatestdata']}"

payload = {

}
headers = {
    'x-lynx-api-key': '',
    # 'Authorization': ''

}
