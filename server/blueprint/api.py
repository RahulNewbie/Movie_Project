
from flask import Blueprint, current_app
from datetime import datetime
import logging

from utility.utility import get_time_diff
from utility import constants
from request.request import get_movie_list, get_people_list
from utility.utility import get_movie_people_relation, jsonize_movie_data

api = Blueprint('api', __name__)

# Global variable to check last visited time stamp
last_visited = datetime.strptime('00:00:00', constants.FMT)


@api.route('/movies/')
def show_list_of_movies():
    """
    API endpoint to get list of movies
    This operation is done in three steps
    a) First get the list of movies
    b) Get the list of people and their corresponding movies
    c) Get the relationship between Movies and the corresponding people
    d) Show the result in the Rest API
    """
    global last_visited
    title = []
    people_dict = {}
    movie_people_dict = {}
    new_time = datetime.now()
    time_diff = get_time_diff(last_visited, new_time)
    # If the time difference between consecutive request
    # is more than a minute, then application will fetch
    # Data from the website
    # Else, it will show the already stored data
    if time_diff.seconds > constants.SINGLE_MINUTE_IN_SECONDS:
        try:
            # Get movie list from the web API
            get_movie_list(title)
            # Get People list from the API
            get_people_list(people_dict)
            # Enquire in people_dict for the
            get_movie_people_relation(title, people_dict, movie_people_dict)
            # Assign the latest request time to the variable
            last_visited = new_time
        except (RuntimeError, Exception):
            logging.error(
                'Error occurred while generating relationship between Movie title and people'
            )
        # Call the database api to remove the old data
        # and store the new movie data into database
        try:
            current_app.config['DB'].delete_data()
            current_app.config['DB'].insert_movie_data(movie_people_dict)
        except OSError:
            logging.error('Error occurred while storing the data into database')
        # Creating output for the user
        output_json = jsonize_movie_data(movie_people_dict)
    else:
        # Call the database api to get the last fetched data
        output_json = jsonize_movie_data(
            current_app.config['DB'].get_movie_data()
        )
    return output_json
