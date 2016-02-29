from flask_wtf import Form
from wtforms import SubmitField, SelectField


class BeerForm(Form):
    # choice definitions
    appearance = [(1, 'Not Even Close'), (3, 'Major Faults'), (5, 'Slight Faults'), (7, 'No Faults'), (9, 'Perfect')]
    aroma = [(1, 'Not Even Close'), (3, 'Major Faults'), (5, 'Slight Faults'), (7, 'No Faults'), (9, 'Perfect')]
    flavor = [(1, 'Not Even Close'), (3, 'Major Faults'), (5, 'Slight Faults'), (7, 'No Faults'), (9, 'Perfect')]
    mouthfeel = [(1, 'Not Even Close'), (3, 'Major Faults'), (5, 'Slight Faults'), (7, 'No Faults'), (9, 'Perfect')]
    myappearance = [(1, 'Two Bagger'), (3, 'Keep Drinking'), (5, 'Plain Jane'), (7, 'Local News Anchor'), (9, 'My Wife')]
    myaroma = [(1, 'Burning Diapers'), (3, 'Stings The Nostrils'), (5, 'Smells Like Beer'), (7, 'Delightful'), (9, 'Euphoria')]
    myflavor = [(1, 'Infected'), (3, 'No Me Gusta'), (5, 'Me Gusta'), (7, 'Delicious'), (9, 'Nectar Of The Gods')]
    replay = [(1, 'Did Not Finish It'), (3, 'Once Was Enough'), (5, 'Solid Go To'), (7, 'Buy In Bulk'), (9, 'I Would Drink Only This')]

    # selection drop downs
    appearance_selector = SelectField("Appearance", choices=appearance)
    aroma_selector = SelectField("Aroma", choices=aroma)
    flavor_selector = SelectField("Flavor", choices=flavor)
    mouthfeel_selector = SelectField("Mouthfeel", choices=mouthfeel)
    myappearance_selector = SelectField("Appearance", choices=myappearance)
    myaroma_selector = SelectField("My Aroma", choices=myaroma)
    myflavor_selector = SelectField("My Flavor", choices=myflavor)
    replay_selector = SelectField("Replay", choices=replay)

    # Submit form.
    submit = SubmitField('Submit')