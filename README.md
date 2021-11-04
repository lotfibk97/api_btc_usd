# api_btc_usd

This is an api that gives the btc usd rate.



## Getting Started

	git clone https://github.com/lotfibk97/api_btc_usd
  
  Go to api_btc_usd:
  
  ```cd api_btc_usd```
  
  Launch the containers:
  
  ```docker-compose buid``` 
  
  Then:
  
  ```docker-compose up``` 

Ps: You need to set up a secret key in settings.py and you need to replace API_KEY by the api key you generated from the alphavantage API

## Usage

  Go to your django url: (0.0.0.0:8000)
  
  First you have to generate a key: 0.0.0.0:8000/generate_key
  
  Then all you have to do is request your exchange rate at 0.0.0.0:8000/api/v1/quotes/your_api_key 
  (A post request to the same url wil trigger an update of the rate)

