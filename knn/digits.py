import pytesseract
import cv2

def classify(frame):
    
    # load the example image and convert it to grayscale
    image = cv2.imread('circle2.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
    # pre-process image
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
     
    # read text
    text = pytesseract.image_to_string(gray)
    cv2.destroyAllWindows()
    if (text): print(text)

    cv2.imshow('frame', gray)

def main():
    classify('blah')

##main() 
cap = cv2.VideoCapture(0) # use default camera

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()

