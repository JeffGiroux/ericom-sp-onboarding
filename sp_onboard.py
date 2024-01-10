import requests
import json
import uuid, sys, time
from urllib.parse import quote


def get_jwt(tenant, key):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    payload = json.dumps({
      "tenantID": tenant,
      "key": key
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    jwt = response.json()['JWT']
    cookie = response.cookies['route']
    return jwt, cookie

def logout(jwt):
    url = "https://ztadmin.ericomcloud.net/api/v1/auth"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}')
    }
    response = requests.request("DELETE", url, headers=headers)
    return response

def create_policy_category(category,access,jwt,cookie):
    url = "https://ztadmin.ericomcloud.net/api/v1/policies/categories"
    payload_array = [
      {"category": category, "profile": "All", "access": access}
    ]
    payload = json.dumps(payload_array)
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}'),
      'Cookie': 'route={0}'.format(str(cookie))
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def default_policy(jwt,cookie):
    url = "https://ztadmin.ericomcloud.net/api/v1/policies/default/All"
    payload = json.dumps({
      "profile": "All",
      "access": "Allow, No SSL Inspection"
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': (f'Bearer {jwt}'),
      'Cookie': 'route={0}'.format(str(cookie))
    }
    response = requests.request("PATCH", url, headers=headers, data=payload)
    return response

def usage():
    print("Usage: python3 sp_onboard.py <Tenant ID> <API Key>")


if __name__ == "__main__":
    
    try:
        auth_tenant = sys.argv[1]
    except:
        print("Tenant ID missing")
        usage()
        exit(1)
    try:
        key = sys.argv[2]
    except:
        print("API Key missing")
        usage()
        exit(1)
    
    print("Authenticating and retrieving token...")
    jwt, cookie = get_jwt(auth_tenant, key)

    inputFile = "categories.csv"

    print("Onboarding...")
    with open(inputFile, 'r') as file:
        # Skip input file header row
        header = next(file)

        for line in file:
            # Assuming each line contains values separated by a comma
            values = line.strip().split(',')
            category = values[0]
            access = values[1]
            encoded_category_name = quote(category, safe='')
            resp = delete_policy_category(encoded_category_name,jwt,cookie)
            #print(f'Deleting {resp}: {category} {resp.text}')
            resp = create_policy_category(category,access,jwt,cookie)
            print(f'{resp}: {category},{access} {resp.text}')
            #output_file.write(f'{category},{access}\n')
    
    print("Updating Default policy...")
    resp = default_policy(jwt,cookie)

    print("Done!")
    logout(jwt)

