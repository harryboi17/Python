import cv2
img=cv2.imread("c:/Users/HP/Desktop/harshad.jpg",1)
#print(img) #prints a 3D vector or image coordinates 
cv2.imshow("Harshad",img)
cv2.waitKey(0)
#cv2.waitKey(5000) this statement will hold the image window for 5 seconds 
cv2.destroyAllWindows()