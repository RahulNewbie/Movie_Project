import json
import requests
import logging

from utility import constants


def get_movie_list(title):
    """
    Get movie list from the website
    """
    try:
        response_movie = requests.get(
            constants.WEB_URL + 'films',
            headers=constants.HEADERS
        )
        # Convert it to json
        movie_list_json = json.loads(response_movie.text)
        for item in movie_list_json:
            title.append(item['title'])
    except (Exception, RuntimeError):
        logging.error(
            'Error occurred while getting movie list from web site'
        )
    return title


def get_movie_name_from_dict(url_list):
    """
    Get movie name from the movie url
    """
    movie_list = []
    try:
        for url in url_list:
            response_movie_name = requests.get(url, headers=constants.HEADERS)
            response_movie_name_json = json.loads(response_movie_name.text)
            movie_list.append(response_movie_name_json['title'])
    except (Exception, RuntimeError):
        logging.error(
            'Error occurred while getting movie list from the movie id'
        )
    return movie_list


def get_people_list(people_dict):
    """
    Get people list from the website and retrieve
    corresponding movie url
    """
    try:
        response_people = requests.get(constants.WEB_URL + 'people',
                                       headers=constants.HEADERS)
        people_list_json = json.loads(response_people.text)
        for item in people_list_json:
            people_dict[item['name']] = get_movie_name_from_dict(item['films'])
        return people_dict
    except (RuntimeError, Exception):
        logging.error(
            'Error occurred while getting people list from the web site'
        )
