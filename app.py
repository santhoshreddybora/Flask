from flask import Flask,render_template,request,jsonify


app = Flask(__name__)



@app.route("/")
def welcome():
    return "Welcome to my Flask App!"


@app.route("/index")
def secondpage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

"""
GET/POST/PUT/DELETE

"""

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Welcome to my page my name is {name} and this is flask basic and it is form route '
    else:
        return render_template('form.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'Welcome to my page my name is {name} this is submit route'
    else:
        return render_template('form.html')

# assigning a var and giving some type for getting only expected values
@app.route('/results/<int:score>')
def results(score):
    return f'Your score is {score}. Congratulations!'

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    return render_template('score.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    
    exp={'score':score,'result':res}
    return render_template('score1.html',results=exp)


@app.route('/successif/<int:score>')
def successif(score):
    return render_template('score2.html',results=score)



"""
PUT and DELETE requests
"""
items=[{"id":1,"name:'item1',""description": 'this is item 1'},
       {"id":2,"name:'item2',""description": 'this is item2'}]


@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    return jsonify(item)


@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'Missing name'})
    item={
        'id': items[-1]['id']+1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(item)
    return jsonify(item)


"Use postman api to get ouput fo below route "
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

"Use postman api to get ouput fo below route "
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    items.remove(item)
    return jsonify({'result':'Item deleted'})




if __name__ == '__main__':
    app.run(debug=True)

