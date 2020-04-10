# MAC address lookup API

The python script query https://macaddress.io/ to get output the Company Name associated with that MAC address.

## Prerequisites:

The API key as an environment variable `MAC_API_KEY` before running the script

Example:
    1. From Terminal:
    command : python MAC_Add.py --macaddress E8:40:40:79:C8:60
    output  : Its a valid {'macaddress': 'E8:40:40:79:C8:60'}
              {'macaddress': 'E8:40:40:79:C8:60'} has this company Cisco Systems, Inc      
    2. From Docker:
    docker run --env MAC_API_KEY=at_vNq5rSCF7AihbZqpXPf6OY8P3wvB3 1202680/macaddress:latest MAC_Add.py -macadd 44:38:39:ff:ef:57
    output = Its a valid {'macaddress': '44:38:39:ff:ef:57'}
             {'macaddress': '44:38:39:ff:ef:57'} has this company Cumulus Networks, Inc

## Process to get API KEY:
    Generate the API_Key FROM https://macaddress.io/api/documentation/making-requests
    

## Docker-image:
    The Link is "docker pull 1202680/macaddress:latest"       
    "# MAC_Add" 
