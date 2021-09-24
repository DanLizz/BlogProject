from flask import Flask, render_template
import requests

app = Flask(__name__)


# Home
@app.route('/')
def home():
    blog_url = "https://api.npoint.io/76aa84646074fa3edf51"
    response = requests.get(url=blog_url)
    blog_data = response.json()
    return render_template("index.html", posts=blog_data)


# Blog
@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/76aa84646074fa3edf51"
    response = requests.get(url=blog_url)
    blog_data = response.json()
    return render_template("post.html", blogid=int(num)-1, posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
