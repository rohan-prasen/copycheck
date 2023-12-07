from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check_copy', methods=['POST'])
def check_copy_route():
    # Your copy-checking logic here
    pass

if __name__ == '__main__':
    app.run(debug=True)
