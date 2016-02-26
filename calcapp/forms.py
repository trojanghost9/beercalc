from flask_wtf import Form
from wtforms import SubmitField, SelectField


class BeerForm(Form):
    # choice definitions
    appearance = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    aroma = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    flavor = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    mouthfeel = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    myappearance = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    myaroma = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    myflavor = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]
    replay = [(1, 'something'), (3.25, 'something'), (5.5, 'something'), (7.75, 'something'), (10, 'somethings')]

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