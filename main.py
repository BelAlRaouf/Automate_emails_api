import requests


api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey" \
      "=890603a55bfa47048e4490069ebee18c"

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print("****", article["title"], "****")
    print(article["description"])
