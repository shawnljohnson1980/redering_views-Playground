from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
 title='play'
 return render_template('index.html')  

@app.route ('/play')
def playground( ):
    
    return render_template("index.html",x=int(3)) 

@app.route('/play/<int:x>')
def mult(x):
   
    some_num={x}
    return render_template('index.html',x=int(x))

@app.route('/play/<color>')
def color(color):
    color=[
        "red","blue","green","yellow","orange","brown","black","pink","purple","cyan","magenta","teal","gray"
    ]
    return render_template('index.html', color=int(color))

@app.errorhandler(404)
def function_name(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True)               


