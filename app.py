from js import img
from flask import Flask,render_template ,request
import pandas as pd
import difflib



movie =pd.read_pickle('movie_dataset/movies.pkl')
similar1 = pd.read_pickle('movie_dataset/simi.pkl')


def movie2(name):
    movies_name = movie['title'].tolist()
    matc = difflib.get_close_matches(name, movies_name)

    if not matc:
        return []  # Return empty if no match found

    match = matc[0]
    index = movie[movie['title'] == match].index.values[0]
#    print(index)

    similarity_score2 = similar1[index]
#    sorted_data = sorted(similarity_score2, key=lambda x: x[1], reverse=True)
#    print(similarity_score2)
    data = []
    for i, m in enumerate(similarity_score2[:10]):
        idx = m[0]
        title = movie.iloc[idx]['title']
        score = movie.iloc[idx]['vote_average']
        cast = movie.iloc[idx]['cast']
        id = movie.iloc[idx]['id']
        release_date = movie.iloc[idx]['release_date']
        genres=movie[movie['index']==idx].genres.values
        img_url = img(title, release_date)

        if img_url == 'Movie not found!':
            continue

        data.append({
            'title': title,
            'cast': cast,
            'rating': float(score),
            'genres': genres,
            'name': name,
            'id': id,
            'imgurl': img_url,
        })

    return data  # Ensure this is at the correct indentation level

#def printd(data):
#    for i in data:
#        print(i)

name='avenger'
dat=movie2(name)




app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/movies",methods=['GET','POST'])
def movies():
    if(request.method=='POST'):
        name=request.form.get('movie')
        print('---DATA______--',name,'----------------')
        l=movie2(name)
        return render_template('movies.html',form=l)
    print('---------no DATA')
    return render_template('movies.html')


#@app.route("/home")
#def home():
#    return render_template('index.html')
