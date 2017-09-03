# FaceIdentification_Generic_Approach_For_Authentication

Step 1 : Register your Face : 

  A. Take a video of few seconds of your face.
  
  B. Create samples of images from Video to train Convolutional Neural Network.
  
  C. Train the model with those images (class = 'YES') and some images that is not your face (class = 'NO')
  
  D. Convert the model output (.h5) into .mlmodel 
  
  E. import it into your Xcode for Production.
 
  
Step 2 : Next Time while log in

  A. Take image from Camera
  
  B. Give the image to CNN for calssification.
  
  C. If it's you then "Successful Log in"
  
  D. Other-wise show some pop-up like "It's not you"
  
Focus :

-- On Accuracy 

-- Feature selections : 

      like Face Landmarks, 
      Face landmarks positions, 
      color information, 
      Shape of Face Landmarks,
 
-- update model after certain period of time (say 6 months) for better accuracy:
Human beings face changes dynamically over ages and times. 
