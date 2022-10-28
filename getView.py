import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Views(Resource):
    def get(self, link):
        res = requests.get('http://www.youtube.com/watch?v='+link)
        soup = BeautifulSoup(res.text,'html.parser')
        num = 0
        list1=[]
        for metaTag in soup.find_all('meta'):
            num = num+1
            metaContent = metaTag['content']
            try:
                print(metaContent)
                list1.append(metaContent)
            except:
                pass
        views = list1[len(list1)-4]
        return {"views" : views}

api.add_resource(Views, "/<string:link>")

if __name__ == "__main__":
    app.run(debug=True)

# https://github.com/iqbalnur21/get-views-flask-api.git

# link='https://www.youtube.com/watch?v=Md5H3-QsZzA&t=10s'

# res = requests.get(link)
# soup = BeautifulSoup(res.text,'html.parser')
# num = 0
# list1=[]

# def getViews():
#     for metaTag in soup.find_all('meta'):
#         num = num+1
#         metaContent = metaTag['content']
#         try:
#             print(metaContent)
#             list1.append(metaContent)
#         except:
#             pass
#     views = list1[len(list1)-4]
#     return views