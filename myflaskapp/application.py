from flask import Flask
application = Flask(__name__)
application.debug = True
@application.route('/', methods=['GET'])
def hello():
 	return '<p>Hello world</p>'

@application.route('/blog/<int:postID>')
def show_blog(postID):
 	return 'Blog Number %d' % postID
if __name__ == "__main__":
 application.run()