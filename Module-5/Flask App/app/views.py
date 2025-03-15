from flask import render_template, request
import os
import cv2
from app.face_recognition import faceRecognitionPipeline
import matplotlib.image as matimg

UPLOAD_FOLDER='static/upload'
def index():
    return render_template('index.html')


def app():
    return render_template('app.html')

def genderapp():
    if request.method=='POST':
        f=request.files['image_name']
        filename=f.filename 
        path=os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        pred_image, predictions = faceRecognitionPipeline(path)
        pred_filename = 'prediction_image.jpg'
        cv2.imwrite(f"./static/predict/{pred_filename}", pred_image)
        print(predictions)
        
        report = []
        
        for i, obj in enumerate(predictions):
            gray_img = obj['roi']
            eign_img = obj['eig_img'].reshape(100,100)
            gender_name = obj['prediction_name']
            score = round(obj['score']*100,2)
            
            gray_img_name = f'roi_{i}.jpg'
            eig_img_name = f'eigen_{i}.jpg'
            
            matimg.imsave(f'./static/predict/{gray_img_name}', gray_img, cmap='gray')
            matimg.imsave(f'./static/predict/{eig_img_name}', eign_img, cmap='gray')
            
            report.append([gray_img_name, eig_img_name, gender_name, score])
        return render_template('gender.html', fileupload=True, report=report)
    print("Machine Learning Model executed successfully")
            
        
        
    
    
    return render_template('gender.html')