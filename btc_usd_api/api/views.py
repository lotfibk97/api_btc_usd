from rest_framework.views import APIView
from .serializers import RealTimeRateSerializer
from .models import RealTimeRate
from rest_framework.response import Response
import requests
from rest_framework_api_key.models import APIKey
from django.http import HttpResponse
from django.conf import settings


class GetRate(APIView):
    #serializer_class = RealTimeRateSerializer
    
    def api_key_verification(self, apikey):
        api_key = APIKey.objects.get_from_key(apikey)
        if api_key is not None:
            return True
        return False    

    def get(self, request, apikey, format=None):
        #we first check if the user has the right to perform the request
        if self.api_key_verification(apikey):
            #we return the most updated value we have
            rate = RealTimeRate.objects.latest()
            serializer = RealTimeRateSerializer(rate)
            return Response(serializer.data)
        else:
            #we ask him to generate a key
            return HttpResponse("""<p>You need an api key to perform this request.</p> 
                <p>If  you don't have one go to /generate_key to get one.</p>
                <p>Example: api/v1/quotes/your_api_key</p> """)

    def post(self, request, apikey, format=None):
        #we first check if the user has the right to perform the request
        if self.api_key_verification(apikey):
            #fetching the api
            url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=" + settings.API_KEY
            r = requests.get(url)
            #getting only the desired values
            data = r.json().get('Realtime Currency Exchange Rate')
            data_cleaned = {}
            #we need to remove the unnecessary characters and make it match the fields names
            for key in data.keys():
                k = key.split('. ')[1].replace(' ','_').lower()
                data_cleaned[k] = data[key]
            #now our serializer will handle the rest        
            serializer = RealTimeRateSerializer(data=data_cleaned)
            if serializer.is_valid(raise_exception=True):
                real_time_rate = serializer.save()
            return Response({"success": "Rate Refreshed successfully"})
        else:
            return HttpResponse("""<p>You need an api key to perform this request.</p> 
                <p>If  you don't have one go to /generate_key to get one.</p>
                <p>Example: api/v1/quotes/query?apikey=your_api_key</p> """)
    
#api key generation
def generate_api_key(request):
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    return HttpResponse('Your API key is : ' + key + ' Keep it safe.')