from flask import Flask, render_template, request
from settings import secret_key
from forms import FormOne

app = Flask(__name__)
app.secret_key = secret_key


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Home page of the app
    POST will check select fields and provide a rating as well as a link to send.
    GET will check for query string parameters and calculate based on the values.
    This allows us to avoid needing a data store when sharing our ratings.
    If no values are provided on a GET the default priority will be 'Not Set'
    """

    form = FormOne()

    if request.method == 'POST':
        # do the calculations and return the information on the results page
        level = int(form.level_selector.data)
        discovery = int(form.discovery_selector.data)
        ease = int(form.ease_selector.data)
        awareness = int(form.awareness_selector.data)
        info = int(form.info_selector.data)
        availability = int(form.availability_selector.data)
        brand = int(form.brand_selector.data)
        privacy = int(form.privacy_selector.data)

        some_factors = (level + discovery + ease + awareness) / 4.0
        some_impact = (info + availability) / 2.0
        other_impact = (brand + privacy) / 2.0
        score = (some_factors + some_impact + other_impact) / 3.0

        if score < 1.8:
            rating = "bad"
        elif score < 3.6:
            rating = "meh"
        elif score < 5.4:
            rating = "good"
        elif score < 7.2:
            rating = "yum"
        else:
            rating = "desert island"

        url = "http://127.0.0.1:8081/results?level=" + str(level) + "&discovery=" + str(discovery) + "&ease=" \
              + str(ease) + "&awareness=" + str(awareness) + "&info=" + str(info) \
              + "&availability=" + str(availability) + "&brand=" + str(brand) + "&privacy=" + str(privacy)

        return render_template('index.html', form=form, rating=rating, url=url)
        # if GET then check if query string parameters to calculate
    else:
        try:
            level = int(request.args.get('level'))
            discovery = int(request.args.get('discovery'))
            ease = int(request.args.get('ease'))
            awareness = int(request.args.get('awareness'))
            info = int(request.args.get('info'))
            availability = int(request.args.get('availability'))
            brand = int(request.args.get('brand'))
            privacy = int(request.args.get('privacy'))

            # calculate score
            some_factors = (level + discovery + ease + awareness) / 4.0
            some_impact = (info + availability) / 2.0
            other_impact = (brand + privacy) / 2.0
            score = (some_factors + some_impact + other_impact) / 3.0

            # set priority
            if score < 1.8:
                rating = "bad"
            elif score < 3.6:
                rating = "meh"
            elif score < 5.4:
                rating = "good"
            elif score < 7.2:
                rating = "yum"
            else:
                rating = "desert island"
        except:
            rating = "Not Set"

        return render_template('index.html', form=form, rating=rating)


@app.route('/test')
def test():
    """
    loads test page for app
    """
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
