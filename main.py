import requests
from pyzbar import pyzbar
import cv2

# If you are on macos, here's the fix for errror ImportError('Unable to find zbar shared library')
# https://github.com/npinchot/zbar/issues/3#issuecomment-1038005495
# class barcode():
#     def __init__(self, image):
#         self.image = image

#     def decode(self, image):
#         """Decode the barcode from the image using pyzbar"""
#         barcodes = pyzbar.decode(image)
#         for barcode in barcodes:
#             (x, y, w, h) = barcode.rect
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#             barcodeData = barcode.data.decode("utf-8")
#             barcodeType = barcode.type
#             text = "{} ({})".format(barcodeData, barcodeType)
#             cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.5, (0, 0, 255), 2)
#             print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
#         return image, barcodeData

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
    return frame, barcode_info

def request_barcode_info(barcode: str):

    url = "https://barcode.monster/api/" + barcode

    response = requests.request("GET", url)

    print(response.text)

# vid = cv2.VideoCapture(0)
  
# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
  
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
      
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
  
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

frame, barcode = read_barcodes(cv2.imread('IMG_7051.jpeg'))
print(barcode)

print(request_barcode_info(barcode))

# cv2.imsave('output.jpeg', frame)