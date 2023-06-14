from flask import Flask, render_template  # added render_template!

app = Flask(__name__)                     
    
@app.route('/lists')                           
def render_lists():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    user_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


    return render_template('index.html', users=user_info)  
    
if __name__=="__main__":
    app.run(debug=True,port=5001)                   

