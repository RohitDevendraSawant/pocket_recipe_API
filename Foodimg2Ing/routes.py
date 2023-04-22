from flask import render_template ,url_for,flash,redirect,request, jsonify
from Foodimg2Ing import app
from Foodimg2Ing.output import output
import os


@app.route('/',methods=['GET'])
def home():
    # return render_template('index.html')
    return jsonify({'message':"Welcome to pocket recipe API"})

@app.route('upload/',methods=['POST','GET'])
def predict():
    imagefile=request.files['image']
    image_path=os.path.join(app.root_path,'static\\images',imagefile.filename)
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title,ingredients,recipe = output(image_path)
    return jsonify({'title' : title, 'ingrdients' : ingredients, 'recipe' : recipe, 'img' : img})

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile=os.path.join(app.root_path,'static\\images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title,ingredients,recipe = output(imagefile)
    return jsonify({'title' : title, 'ingrdients' : ingredients, 'recipe' : recipe, 'img' : img})
