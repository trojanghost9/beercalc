from flask_wtf import Form
from wtforms import SubmitField, SelectField


class BeerForm(Form):
    # choice definitions
    appearance = [(1, 'Not Even Close'), (3.25, 'Major Faults'), (5.5, 'Slight Faults'), (7.75, 'No Faults'), (10, 'Perfect')]
    aroma = [(1, 'Not Even Close'), (3.25, 'Major Faults'), (5.5, 'Slight Faults'), (7.75, 'No Faults'), (10, 'Perfect')]
    flavor = [(1, 'Not Even Close'), (3.25, 'Major Faults'), (5.5, 'Slight Faults'), (7.75, 'No Faults'), (10, 'Perfect')]
    mouthfeel = [(1, 'Not Even Close'), (3.25, 'Major Faults'), (5.5, 'Slight Faults'), (7.75, 'No Faults'), (10, 'Perfect')]
    myappearance = [(1, 'Two Bagger'), (3.25, 'Keep Drinking'), (5.5, 'Plain Jane'), (7.75, 'Local News Anchor'), (10, 'My Wife')]
    myaroma = [(1, 'Burning Diapers'), (3.25, 'Stings The Nostrils'), (5.5, 'Smells Like Beer'), (7.75, 'Delightful'), (10, 'Euphoria')]
    myflavor = [(1, 'Infected'), (3.25, 'No Me Gusta'), (5.5, 'Me Gusta'), (7.75, 'Delicious'), (10, 'Nectar Of The Gods')]
    replay = [(1, 'Did Not Finish It'), (3.25, 'Once Was Enough'), (5.5, 'Solid Go To'), (7.75, 'Buy In Bulk'), (10, 'I Would Drink Only This')]

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