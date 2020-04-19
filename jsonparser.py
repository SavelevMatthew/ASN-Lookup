import json


def parse_whois_response(response_json):
    result = []
    data = response_json['data']
    records = data['irr_records']
    for record in records:
        for note in record:
            if note['key'] == 'origin':
                result.append(note['value'])
    answer = set(result)
    if (len(answer) == 0):
        return "None"
    else:
        return "; ".join(answer)
