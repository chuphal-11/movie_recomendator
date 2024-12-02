from js import img
from flask import Flask,render_template ,request

from flask_wtf import FlaskForm
import pickle
import difflib




movie =pickle.load(open('movie_dataset/movies.pkl','rb'))
similar1 = pickle.load(open('movie_dataset/similarity_1.pkl','rb'))
similar2 = pickle.load(open('movie_dataset/similarity_2.pkl','rb'))
similar3 = pickle.load(open('movie_dataset/similarity_3.pkl','rb'))
similar4 = pickle.load(open('movie_dataset/similarity_4.pkl','rb'))
similar5 = pickle.load(open('movie_dataset/similarity_5.pkl','rb'))


def movie2(name):
    movies_name = movie['title'].tolist()
    matc = difflib.get_close_matches(name, movies_name)

    if not matc:
        return []  # Return empty if no match found

    match = matc[0]
    index = movie[movie['title'] == match].index.values[0]

    if index < 1000:
        similarity_score2 = list(enumerate(similar1[index]))
    elif index < 2000:
        similarity_score2 = list(enumerate(similar2[index - 1000]))
    elif index < 3000:
        similarity_score2 = list(enumerate(similar3[index - 2000]))
    elif index < 4000:
        similarity_score2 = list(enumerate(similar4[index - 3000]))
    else:
        similarity_score2 = list(enumerate(similar5[index - 4000]))

    sorted_data = sorted(similarity_score2, key=lambda x: x[1], reverse=True)

    data = []
    for i, m in enumerate(sorted_data[:10]):
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

def printd(data):
    for i in data:
        print(i)

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

if __name__=='__main__':
    app.run(debug=True)

#@app.route("/home")
#def home():
#    return render_template('index.html')