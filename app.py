from js import img
from flask import Flask,render_template ,request

from flask_wtf import FlaskForm
import pickle
import difflib




movie =pickle.load(open('movie_dataset/movies.pkl','rb'))
movie_similarity =pickle.load(open('movie_dataset/movies_similarity.pkl','rb'))


def movie2(name):
    movies_name = movie['title'].tolist()
    matc = difflib.get_close_matches(name,movies_name)
    
    match=matc[0]
    index=movie[movie['title']==match].index.values[0]

    sort = list(enumerate(movie_similarity[index]))

    sorted_data=sorted(sort,key=lambda x:x[1],reverse=True)

    i=1
    data=[]
    for m in sorted_data:
        idx=m[0]
        if i<11:
            data2={}
            title=movie[movie['index']==idx].title.values[0]
            score=movie[movie['index']==idx].vote_average.values[0]
            cast=movie[movie['index']==idx].cast.values[0]
            id=movie[movie['index']==idx].id.values[0]
            release_date=movie[movie['index']==idx].release_date.values[0]
            genres=movie[movie['index']==idx].genres.values
            k=float(score)
            data2['title']=title
            data2['cast']=cast
            data2['rating']=k
            data2['genres']=genres
            data2['name']=name  
            data2['id']=id
            
            data2['imgurl']=img(title,release_date)
            if(data2['imgurl']=='Movie not found!'):
                continue
                i=i-1
            
            data.append(data2)
            i=i+1
            
    return data
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