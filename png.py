import cv2

#number show.
def show(number):

    im = cv2.imread("picture/%d.jpg"%number,0)
    cv2.imshow("%d"%number,im)
    cv2.waitKey(1)
    cv2.moveWindow("%d"%number, 4340, 1000)
    #print(im)

def show_str(str):
    if str == "start":
        im = cv2.imread("picture/start.jpg")

    if str == "end":
        im = cv2.imread("picture/end.jpg")

    if str == "answer":
        im = cv2.imread("picture/answer.jpg")

    if str == "break":
        im = cv2.imread("picture/break.jpg")

    if str == "speech":
        im = cv2.imread("picture/speech.jpg")

    if str == "nospeech":
        im = cv2.imread("picture/nospeech.jpg")

    if str == "freedom":
        im = cv2.imread("picture/freedom.jpg")

    cv2.imshow(str,im)
    cv2.waitKey(1)
    cv2.moveWindow(str, 4340, 1000)
