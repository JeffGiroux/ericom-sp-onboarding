import requests
import json
import uuid, sys, time


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

def usage():
    print("Usage: python3 sp_decommission.py <Tenant ID> <API Key>")


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

    print("Decommissioning...")
    #TBD enter code here for decomm

    print("Done!")
    logout(jwt)

