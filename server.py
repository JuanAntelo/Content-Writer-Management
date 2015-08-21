import os
from flask import Flask, Response
from flask_restful import Resource, Api, marshal, fields

app = Flask(__name__, static_url_path='')
api = Api(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

writerTotalViewList = [
    {'id': 1, 'name': 'Steve J', 'viewCount' : 49},
    {'id': 2, 'name': 'Bill A', 'viewCount' : 71},
    {'id': 3, 'name': 'Joe K', 'viewCount' : 106},
    {'id': 4, 'name': 'Alex M', 'viewCount' : 129},
    {'id': 5, 'name': 'Jade S', 'viewCount' : 144},
    {'id': 6, 'name': 'Carlos A', 'viewCount' : 176}
];
viewListFields = { 'id': fields.Raw,  'name': fields.Raw, 'viewCount' : fields.Raw }

writerMetaData = {'writers': [{
			'name': 'Steve J',
			'imgPath': 'lib/images/7.jpg',
			'socialMediaPostCount' : 3,
			'blogPostCount' : 2,
			'otherPostCount' : 1,
			'employeeType' : "Fulltime",
			'totalViews' : 49
	           		},
	           		{
			'name': 'Bill A',
			'imgPath': 'lib/images/2.jpg',
			'socialMediaPostCount' : 5,
			'blogPostCount' : 1,
			'otherPostCount' : 1,
			'employeeType' : "Fulltime",
			'totalViews' : 71
	           	 	},
		            {
			'name': 'Joe K',
			'imgPath': 'lib/images/5.jpg',
			'socialMediaPostCount' : 4,
			'blogPostCount' : 1,
			'otherPostCount' : 1,
			'employeeType' : "Fulltime",
			'totalViews' : 106
	           		},
	           		{
			'name': 'Alex M',
			'imgPath': 'lib/images/3.jpg',
			'socialMediaPostCount' : 2,
			'blogPostCount' : 3,
			'otherPostCount' : 1,
			'employeeType' : "Freelance",
			'totalViews' : 129
	           		},
			{
			'name': 'Jade',
			'imgPath': 'lib/images/6.jpg',
			'socialMediaPostCount' : 5,
			'blogPostCount' : 2,
			'otherPostCount' : 1,
			'employeeType' : "Temp",
			'totalViews' : 144
	           		},
	           		{
	           	  	'name': 'Carlos A',
			'imgPath': 'lib/images/1.jpg',
			'socialMediaPostCount' : 1,
			'blogPostCount' : 1,
			'otherPostCount' : 1,
			'employeeType' : "Fulltime",
			'totalViews' : 176

	           		  }]}

metaDataFields = {'writers': fields.Raw}

class getWriterTotalViewList(Resource):
    def get(self):
        return marshal(writerTotalViewList, viewListFields)
class getWriterMetaDataList(Resource):
    def get(self):
        return marshal(writerMetaData, metaDataFields)

api.add_resource(getWriterTotalViewList, '/writerTotalViewList')
api.add_resource(getWriterMetaDataList, '/writerMetaDataList')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
