import requests
import json
import jsonparser

whoisUrl = 'https://stat.ripe.net/data/whois/data.json'


def get_ASN(ip_address):
    return try_get_ASN(ip_address, 3)


def try_get_ASN(ip_address, attemps_left):
    params = {'resource': ip_address}
    try:
        response = requests.get(whoisUrl, params=params)
    except:
        if attemps_left > 0:
            return try_get_ASN(ip_address, attemps_left - 1)
        else:
            return 'Can\'t connect to server'
    if response.status_code == 200:
        response_json = response.json()
        return jsonparser.parse_whois_response(response_json)

        return 'sss'
    elif attemps_left > 0:
        return try_get_ASN(ip_address, attemps_left - 1)
    else:
        return 'Error! Response code: ' + response.status_code
