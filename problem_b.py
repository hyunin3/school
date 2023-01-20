import json
from pprint import pprint


def movie_info(movie, genres):
    #print(movie)
    #print(genres) #우리는 바깥에 있는 장르파일을 모르고 movie랑 genres만 알고있음
    movie['genre_ids'] #=[18,80]
    genre_list = []
    for ids in movie:
        int(ids['genre_ids']) 
        # for id in [80, 18]:
    for id in movie['genre_ids']:
        
        if genres['id'] == id:
            genre_list.append(genres['name'])
                
            # for genre in genres:
            #     if genre['id'] == number:
            #         genre_list.append(genre['name'])
            #     elif genre['id'] == number: 
            #         genre_list.append(genre['name'])
            
    # print(genre_list)
    
    new_data = {
        # 'genre_names': genres.get('name', 'name'),#리스트 안에 딕셔너리가 여러개 들어있음.
        'genre_names': genre_list,
        'id': movie.get('id'),                    
        'overview': movie.get('overview'),        
        'poster_path': movie.get('poster_path'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }
    return new_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
