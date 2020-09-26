import json
from datetime import datetime
from utility import constants


def get_time_diff(last_visited, new_time):
    """
    Get time difference between consecutive requests
    """
    new_time_formatted = new_time.strftime("%H:%M:%S")
    last_visited_formatted = last_visited.strftime("%H:%M:%S")
    return datetime.strptime(new_time_formatted, constants.FMT) - datetime.\
        strptime(last_visited_formatted, constants.FMT)


def get_movie_people_relation(title, people_dict):
    """
    Get the relation between movie title and
    the corresponding people and return as dict
    """
    movie_people_dict = {}
    for item in title:
        for key in people_dict.keys():
            for movie_title in people_dict[key]:
                if item == movie_title:
                    if item in movie_people_dict.keys():
                        if key not in movie_people_dict[item]:
                            movie_people_dict[item] += ',' + key
                    else:
                        movie_people_dict[item] = key
                else:
                    if item not in movie_people_dict.keys():
                        movie_people_dict[item] = ''
    return movie_people_dict


def jsonize_movie_data(movie_data):
    """
    Make json from the movie data
    """
    output_json = ""
    if type(movie_data) is list:
        for movie in movie_data:
            output_json += json.dumps(
                [
                    {
                        'movie_title': movie[0],
                        'people': movie[1]
                    }
                ],
                indent=3
            )
    elif type(movie_data) is dict:
        for key_item in movie_data.keys():
            output_json += json.dumps(
                [
                    {
                        'movie_title': key_item,
                        'people': movie_data[key_item]
                    }
                ],
                indent=3
            )

    return output_json
