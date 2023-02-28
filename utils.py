import sqlite3


def get_data(query):

    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(query)
    executed_data = cursor.fetchall()
    connection.close()
    return executed_data


def get_picture_by_title(title):

    query = f'''
            SELECT `title`, `country`, `release_year`, `genre`, `description` 
            FROM netflix
            WHERE `title`='{title}'
            ORDER BY release_year DESC 
            LIMIT 1 
            '''

    raw_data = get_data(query)

    result = {
        "title" : raw_data[0][0],
        "country" : raw_data[0][1],
        "release_year" : raw_data[0][2],
        "genre" : raw_data[0][3],
        "description" : raw_data[0][4]
    }
    return result


def get_picture_by_years(start_year, end_year):


    query = f'''
            SELECT `title`, `release_year` 
            FROM netflix
            WHERE `release_year` BETWEEN {start_year} AND {end_year}
            LIMIT 100
            '''

    raw_data = get_data(query)
    result = []

    for picture in raw_data:
        picture_data = {"title" : picture[0],
                        "release_year" : picture[1]}
        result.append(picture_data)

    return result


def get_picture_by_rating(rating):


    if rating == 'children':
        query = f'''
        SELECT `title`, `rating`, `description` 
        FROM netflix
        WHERE `rating` = 'G'
        '''

    elif rating == 'family':
        query = f'''
        SELECT `title`, `rating`, `description` 
        FROM netflix
        WHERE `rating` IN ('G', 'PG', 'PG-13')
        '''

    elif rating == 'adult':
        query = f'''
        SELECT `title`, `rating`, `description` 
        FROM netflix
        WHERE `rating` IN ('R', 'NC-17')
        '''

    raw_data = get_data(query)
    result = []
    for picture in raw_data:
        picture_info = {"title" : picture[0],
                        "rating" : picture[1],
                        "description" : picture[2]}
        result.append(picture_info)

    return result


def get_picture_by_genre(genre):

    query = f'''
            SELECT `title`, `description`
            FROM netflix
            WHERE `listed_in` LIKE '%{genre}%'
            ORDER BY `release_year` DESC
            LIMIT 10
            '''

    raw_data = get_data(query)
    result =[]
    for picture in raw_data:
        picture_info = {"title" : picture[0],
                        "description" : picture[1]}
        result.append(picture_info)

    return result


def get_picture_by_actors(actor1, actor2):

    query = f'''
                SELECT `cast` FROM netflix
                WHERE `cast` LIKE '%{actor1}%' AND `cast` LIKE '%{actor2}%'
                '''

    raw_data = get_data(query)
    all_actors = []
    twice_match_actors = []

    for cast in raw_data:
        cast = ''.join(cast)
        cast = cast.split(', ')

        for actor in cast:
            all_actors.append(actor)

    for person in all_actors:
        if person != actor1 and person != actor2 and \
                all_actors.count(person) > 2 and \
                person not in twice_match_actors:

            twice_match_actors.append(person)

    return twice_match_actors


def get_picture_by_type_year_genre(type, year, genre):

    query = f'''
            SELECT `title`, `description`
            FROM netflix 
            WHERE `type` = '{type}' 
            AND `release_year` = '{year}' 
            AND `listed_in` LIKE '{genre}'
            '''

    raw_data = get_data(query)
    result = []

    for title in raw_data:
        picture_info = {"Title" : title[0],
                        "Description" : title[1]}
        result.append(picture_info)

    return result

