# PlantDiseaseDetection

# Problem Statement:

The proposed research work is carried on potato crop. In a survey, 61.33% of farmers cultivating potatoes reported bright as one of the major reasons for their crop failure. India is the 2nd largest producer of potatoes followed by China which is the largest producer of these crop. Improving fertilization and automating the system for disease detection can improve the crop production of our country.

# Dataset used for the project


# Objectives

 - To develop a prototype for a plant detection system.
 - To apply image processing techniques to identify the disease pattern.
 - Use deep learning algorithms to predict disease.
 - Use transfer learning algorithms to predict disease.

# Modules used for the project:
 1. Keras
 2. Tensorflow
 3. OpenCv
 4. Matplotlib
 5. Image library (PIL)
 6. Tkinter
 
# Our work:

 - We carried out the work in four different cases(i.e., building four different models and picking the efficient model for predicting)
 
  1. In the first case we build a custom model using CNN. Accuracy we got for the model is **83.59%**.
  2. In the second case we used our pre-trained ResNet-50 v2 model. Accuracy we got for the model is **98.24**.
  3. In the third case we have trained our ResNet-50 v2 model. Accuracy we got for the model is **99.64%**. This one is the **efficient** model.
  4. In the fourth case we use the ResNet-50 v2 architecture but train the whole model from scratch. Accuracy we got for the model is **95.93%**.
 - We built all the above described models in **Google Colab** and saved those models.
 - We made use of the saved models for building a front end for the application using tkinter.
 - Front end takes input as image from the user and predicts the disease for the particular image.
 
 Python command to run the front end: **python FrontEnd.py**
 ![Alt text](/Users/arunamballa/Downloads/db_project_frontEnd2 "Plant Disease Detection")



 
