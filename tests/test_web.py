import requests

resp = requests.post('https://mgr-osu.herokuapp.com/predict',
                     files={'file': open('blues.00000.wav', 'rb')})

print(resp.text)
