import requests
import os
import argparse
import re

# To take input as a command line
def parse_args():
    parser = argparse.ArgumentParser(description="output the Company Name associated with that MAC address by Querying macaddress.io")
    parser.add_argument( '-macadd', '--macaddress', type=str,
                         default='Default', help='MAC_address of Company',required = 'True')
    return parser.parse_args()


# To validate the input
def validate_macaddress(mac_address):
    if re.match( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address['macaddress'].lower() ):
         print(f"Its a valid {mac_address}")
    else:
        print(f'The Mac_Add is invalid {mac_address}')
        exit()

# To make the API- Connection
def api_output(MAC_API_KEY,mac_address):
    api_url = 'https://api.macaddress.io/v1'
    response = requests.get(url= api_url + '?output=json&search=' + mac_address['macaddress'],headers= {'X-Authentication-Token': MAC_API_KEY} )
    company_name = response.json()['vendorDetails']['companyName']
    if company_name:
        print(f'{mac_address} has this company {company_name}')
    else:
        print(f'The Company_Name does not exit for this {mac_address}')

if __name__ == "__main__":
    mac_address = vars(parse_args())
    validate_macaddress(mac_address)
    MAC_API_KEY = os.environ.get('MAC_API_KEY')
    api_output(MAC_API_KEY, mac_address)
