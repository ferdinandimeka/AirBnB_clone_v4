#!/usr/bin/python3
""" Flask App that integrates with AirBnB static HTML Template """
from flask import Flask, render_template
from models import storage
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    # after each request, this method calls close() like remove() on the current SQLAlchemy session
    storage.close()

@app.route('/1-hbnb')
def hbnb_filters(the_id=None):
    # handles the request to custom templates with states, cities & amenities
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Places').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)] for user in storage.all('User').values())
    return render_template('1-hbnb.html', 
                            cache_id=uuid.uuid4(),
                            states=states, amens=amens, places=places, users=users)

if __name__ == "__main__":
    """ Main Function """
    app.run(host=host, port=port)
