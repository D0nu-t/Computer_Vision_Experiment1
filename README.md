# placeholder2t
 Measures distance between the eyes
___
# Requirements-:

opencv2

numpy

imutils
___
Program detects the users eye and locates the center of the eye by drawing a rectangle around it

A line is drawn between each eye and the average length of the line is logged

The eyes are located by using classifiers from cv2 and the distance is written to a csv file
___
Accuracy of the measurements could be improved by using a multi-camera setup

The distance from the camera affects the measurements taken, normalizing this would further increase the accuracy of measurements taken
___
Program has potential applications in biometric security, although the reliability is not yet at a stage where that would be reccomendable
