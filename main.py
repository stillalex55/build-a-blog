from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://buildablog:Aa02850621!@localhost:8889/buildablog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'jfhjerj3h234'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/')
def index():

    return redirect('/blog')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        new_title = request.form['title']
        new_blog = request.form['blog'] 

        if new_title == "":
            flash('Must have a title')
            return redirect("/newpost")
        if new_blog == "":
            flash('Must have a body')
            return redirect("/newpost")
        else:
            new_post = Blog(title, blog)
            db.session.add(new_post)
            db.session.commit()
            return redirect ('/blog?id={}'.format(new_post.id))
        

    return render_template('newpost.html', title="Add an Entry")

@app.route('/blog', methods=['POST', 'GET'])
def blog(): 
    blog_id = request.args.get('id')

    if blog_id == None:
        blogs = Blog.query.all()
        return render_template('blog.html', title="Build a Blog", blogs=blogs)
    else:
        posts = Blog.query.get(blog_id)
        return render_template('blogpost.html', title=posts.title, posts=posts)

if __name__ == '__main__':
    app.run()