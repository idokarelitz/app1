from flask import Flask, render_template, flash, request, redirect, url_for



# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def main():
    return render_template("main.html")

# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

#start app
if __name__=='__main__':
    app.run(debug=True,port=9000)