from flask import Flask, render_template, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-trends")
def get_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    
    regions = {
        'USA': 'united_states',
        'Wielka Brytania': 'united_kingdom',
        'Australia': 'australia',
        'Indie': 'india',
        'Kanada': 'canada',
        'Francja': 'france',
        'Niemcy': 'germany',
        'Włochy': 'italy',
        'Brazylia': 'brazil',
        'Rosja': 'russia',
        'Meksyk': 'mexico',
        'Japonia': 'japan',
        'Hiszpania': 'spain',
        'Argentyna': 'argentina',
        'Chiny': 'china',
        'RPA': 'south_africa',
        'Indonezja': 'indonesia',
        'Szwecja': 'sweden',
        'Niderlandy': 'netherlands',
        'Nowa Zelandia': 'new_zealand',
        'Singapur': 'singapore'
    }

    trends_data = {}
    for region_name, region_code in regions.items():
        try:
            trending_searches_df = pytrends.trending_searches(pn=region_code)
            trends_data[region_name] = trending_searches_df[0].tolist()
        except:
            trends_data[region_name] = ['Brak danych dla tego regionu.']

    return jsonify(trends_data)

if __name__ == "__main__":
    app.run(debug=True)
