from twitter import *
import config
from flask import Flask,render_template
app = Flask(__name__)
import os
import yweather




@app.route('/')
def hello():
    twitter = Twitter(auth = OAuth(os.environ.get('access_key'),
                  os.environ.get('access_secret'),
                  os.environ.get('consumer_key'),
                  os.environ.get('consumer_secret')))
    client = yweather.Client()
    id_location=client.fetch_woeid('India')
    print("id is ",id_location)



    results = twitter.trends.place(_id = id_location)

    print("India Trends")
    list_of_trends=[]

    for location in results:
        for trend in location["trends"]:
            print(" - %s" % trend["name"])
            list_of_trends.append(trend["name"])    
    return render_template('index.html', trends=list_of_trends)

if __name__ == '__main__':
    app.run(debug=True)