import requests
import time

for _ in range(15): # loop de iterações = 15
    response = requests.get("http://www.cloudflare.com/rate-limit-test/")
    print(response.status_code) 
    time.sleep(5) # tempo de 5 segundos para cada requisição