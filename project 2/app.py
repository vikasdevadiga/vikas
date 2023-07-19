from flask import Flask,render_template
app = Flask(__name__)
if __name__ =="__main__":
    app.run()\
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chandan')
def chandan():
    return render_template('chandan.html')

@app.route('/raneeth')
def raneeth():
    return render_template('raneeth.html')