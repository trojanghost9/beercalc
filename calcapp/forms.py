from flask_wtf import Form
from wtforms import SubmitField, SelectField


class FormOne(Form):
    # choice definitions
    level = [(1, 'something'), (3, 'something'), (5, 'something'), (6, 'something'), (9, 'somethings')]

    discovery = [(1, 'something'), (3, 'something'), (7, 'something'), (9, 'Asomething')]

    ease = [(1, 'something'), (3, 'something'), (5, 'something'), (9, 'something')]

    awareness = [(1, 'something'), (4, 'something'), (6, 'something'), (9, 'something')]

    info = [(2, 'something'), (5, 'something'), (6, 'something'), (7, 'something'), (9, 'something')]

    availability = [(1, 'something'), (5, 'something'), (5, 'something'), (7, 'something'), (9, 'something')]

    brand = [(1, 'Minimal Damage'), (4, 'Loss of Major Accounts'), (5, 'Loss of Goodwill'), (9, 'Brand Damage')]

    privacy = [(3, 'One Individual'), (5, 'Hundreds of People'), (7, 'Thousands of People'), (9, 'Millions of People')]

    # selection drop downs
    level_selector = SelectField("Level", choices=level)

    discovery_selector = SelectField("Discovery", choices=discovery)

    ease_selector = SelectField("Ease", choices=ease)

    awareness_selector = SelectField("Awareness", choices=awareness)

    info_selector = SelectField("Info", choices=info)

    availability_selector = SelectField("Availability", choices=availability)

    brand_selector = SelectField("Brand", choices=brand)

    privacy_selector = SelectField("Privacy", choices=privacy)

    # Submit form.
    submit = SubmitField('Submit')