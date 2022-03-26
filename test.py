import requests

r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={'text': "green"},
    headers={'api-key': "cd7d7e11-252a-40df-a168-eab5cd6512d0"}
).json()["output"]

print(r)