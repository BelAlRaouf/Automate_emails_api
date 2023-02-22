import requests
from send_email import send_email


api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey" \
      "=890603a55bfa47048e4490069ebee18c"

request = requests.get(url)

content = request.json()

email_contents = ""
for article in content["articles"]:
    if article['title'] is not None:
        email_contents = "Subject: Today's News" + "\n"\
                         + email_contents \
                         + article["title"] + "\n" \
                         + article["description"] + "\n"\
                         + article["url"] + 2*"\n"

email_contents = email_contents.encode("utf-8")
send_email(message=email_contents)
