from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# jinja filters
''' 
safe
capitalize
lower
upper
title
trim
striptags
'''

# Create a home route
@app.route('/')
@app.route('/home')
def index():
    first_name = "Aritra"
    bold = "<strong>Bold</strong>"
    company = "hdfc bank private limited"
    cust_id = "101 202 303"
    products = ['current account', 'savings account', 'loan','locker']

    return render_template("index.html", first_name=first_name,
                           bold=bold, company=company,
                           cust_id=cust_id, products=products)

# Create a user route
# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# Create custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html"), 404

# Create custom error pages
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error_404.html"), 500

if __name__ == "__main__":
    app.run(debug=True)