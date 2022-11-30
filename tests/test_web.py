import requests

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('classical.00002.wav', 'rb')})
print("Classical Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('blues.00000.wav', 'rb')})

print("Blues Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('country.00009.wav', 'rb')})
print("Country Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('disco.syn.mp3', 'rb')})

print("Disco Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('hiphop.00017.wav', 'rb')})
print("Hip Hop Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('jazz.00010.wav', 'rb')})

print("Jazz Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('metal.00019.wav', 'rb')})
print("Metal Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('pop.00008.wav', 'rb')})

print("Pop Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('reggae.00008.wav', 'rb')})
print("Reggae Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('rock.muse.mp3', 'rb')})

print("Rock Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('music_of_the_night_opera.mp3', 'rb')})
print("Opera Example")
print(resp.text)

resp = requests.post('http://localhost:5000/predict',
                     files={'file': open('think_of_me_opera.mp3', 'rb')})

print("Opera Example")
print(resp.text)