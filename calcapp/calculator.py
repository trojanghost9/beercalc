from flask import Flask, render_template, request
from settings import secret_key
from forms import BeerForm
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.secret_key = secret_key
CsrfProtect(app)


@app.after_request
def frame_buster(response):
    response.headers['X-Frame-Options'] = 'DENY'
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Home page of the app
    POST will check select fields and provide a rating as well as a link to send.
    GET will check for query string parameters and calculate based on the values.
    This allows us to avoid needing a data store when sharing our ratings.
    If no values are provided on a GET the default priority will be 'Not Set'
    """

    form = BeerForm()

    if request.method == 'POST':
        # do the calculations and return the information on the results page
        appearance = int(form.appearance_selector.data)
        aroma = int(form.aroma_selector.data)
        flavor = int(form.flavor_selector.data)
        mouthfeel = int(form.mouthfeel_selector.data)
        myappearance = int(form.myappearance_selector.data)
        myaroma = int(form.myaroma_selector.data)
        myflavor = int(form.myflavor_selector.data)
        replay = int(form.replay_selector.data)

        # calculate score
        style_factors = (appearance + aroma + flavor + mouthfeel) / 4.0
        my_factors = (myappearance + myaroma + myflavor + replay) / 4.0
        score = (style_factors + my_factors) / 2.0

        if score < 1.8:
            rating = "Poor it out!"
        elif score < 3.6:
            rating = "Meh"
        elif score < 5.4:
            rating = "Good"
        elif score < 7.2:
            rating = "Yum!"
        else:
            rating = "Desert island beer!!!"

        url = "http://127.0.0.1:8081/?appearance=" + str(appearance) + "&aroma=" + str(aroma) + "&flavor=" \
              + str(flavor) + "&mouthfeel=" + str(mouthfeel) + "&myappearance=" + str(myappearance) \
              + "&myaroma=" + str(myaroma) + "&myflavor=" + str(myflavor) + "&replay=" + str(replay)

        return render_template('index.html', form=form, rating=rating, url=url)
        # if GET then check if query string parameters to calculate
    else:
        try:
            appearance = int(request.args.get('appearance'))
            aroma = int(request.args.get('aroma'))
            flavor = int(request.args.get('flavor'))
            mouthfeel = int(request.args.get('mouthfeel'))
            myappearance = int(request.args.get('myappearance'))
            myaroma = int(request.args.get('myaroma'))
            myflavor = int(request.args.get('myflavor'))
            replay = int(request.args.get('replay'))

            # calculate score
            style_factors = (appearance + aroma + flavor + mouthfeel) / 4.0
            my_factors = (myappearance + myaroma + myflavor + replay) / 4.0
            score = (style_factors + my_factors) / 2.0

            if score < 1.8:
                rating = "Poor it out!"
            elif score < 3.6:
                rating = "Meh"
            elif score < 5.4:
                rating = "Good"
            elif score < 7.2:
                rating = "Yum!"
            else:
                rating = "Desert island beer!!!"

            url = "http://127.0.0.1:8081/?appearance=" + str(appearance) + "&aroma=" + str(aroma) + "&flavor=" \
                  + str(flavor) + "&mouthfeel=" + str(mouthfeel) + "&myappearance=" + str(myappearance) \
                  + "&myaroma=" + str(myaroma) + "&myflavor=" + str(myflavor) + "&replay=" + str(replay)

        except:
            rating = "Not Set"
            url = ""

        return render_template('index.html', form=form, rating=rating, url=url)


@app.route('/test')
def test():
    """
    loads test page for app
    """
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
