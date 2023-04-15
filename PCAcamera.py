import cv2
from sklearn.decomposition import PCA
import numpy as np
n_samples = 150 #explains itself
n_components1 = 120 #the number of eigvectors for the PCA
img_quality =120 #the size of each eigvector
if n_samples<n_components1 or img_quality<n_components1:
    print("you need to have more samples or more img quality...\n they have to be at least as many as the number of components ")
    exit() #should avoid bad input data, comment it to see the error if u want
out_img_quality = 500#output image

#capture the images to do PCA
capture = cv2.VideoCapture(0)
i=0
#each iteration it saves an image inside images
images = []
while i<n_samples:
    i+=1
    img = capture.read()[1]
    cv2.imshow("", img)
    cv2.waitKey(3)
    img = cv2.resize(img, [img_quality,img_quality])
    images.append(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
    
data = np.array(images)
pca = PCA(n_components=n_components1)
data = data.reshape(n_samples, -1)
pca.fit(data) #feed the PCA :(

while True:
    imgo = cv2.cvtColor(capture.read()[1], cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(imgo, [img_quality,img_quality])#make the camera image the same size of sqrt(1 eigvector)
    #we have to reshape so it's same size of 1 eigvector
    project = pca.transform(resized.reshape([1,-1]))# it's equal to do P = U.T @ resized.reshape[1,-1].T
    reproject = pca.inverse_transform(project)# it's equal to do U @ P ----> U @ (U.T @ data.T)
    img = reproject.reshape((img_quality,img_quality))#make the image squared
    img = img.astype("uint8")#convert the type from float64 so it doesn't show a white image
    errors_img = cv2.applyColorMap((img-resized)**2, cv2.COLORMAP_PLASMA)#This is to improve, 
    #i wanna see the difference between the original image and the projected one, ideal would be to apply jet cmap of matplotlib
    cv2.imshow("", imgo)#original image
    #we make the images bigger so it's beter to see
    cv2.imshow("errors", cv2.resize(errors_img,[out_img_quality,out_img_quality]))#error image
    cv2.imshow("0", cv2.resize(img, [out_img_quality,out_img_quality]))#transofrmed image
    if  cv2.waitKey(1) & 0xFF == ord('q'):
           break