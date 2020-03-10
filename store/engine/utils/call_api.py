import requests
import json


def call_api(url, method, data, headers={"content": "application/json"}):
    print(data)
    response = requests.post(
        url=url,
        # method=method,
        data=json.dumps(data),
        headers=headers
    )
    status_code = response.status_code
    text = json.loads(response.text)
    if status_code != 200:
        return dict(status=status_code, message=text.get("message"), error=True)
    return dict(status=status_code, data=text)