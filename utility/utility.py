from datetime import datetime
from utility import constants


def get_time_diff(new_time):
    """
    Get time difference between consecutive requests
    """
    new_time_formatted = new_time.strftime("%H:%M:%S")
    last_visited_formatted = constants.LAST_VISITED.strftime("%H:%M:%S")
    return datetime.strptime(new_time_formatted, constants.FMT) - datetime.\
        strptime(last_visited_formatted, constants.FMT)


def get_movie_people_relation(title, people_dict, movie_people_dict):
    """
    Get the relation between movie title and
    the corresponding people and return as dict
    """
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
