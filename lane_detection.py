import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_lines(img, threshold1 = 50, threshold2 = 150, aperatureSize = 3, minLineLength = 100, maxLineGap = 10):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2, aperatureSize) # detect edges
    lines = cv2.HoughLinesP(
                    edges,
                    1,
                    np.pi/180,
                    100,
                    minLineLength,
                    maxLineGap,
            ) # detect lines
    
    return lines

def draw_lines(img,lines, color = (0,255,0)):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    plt.imshow(img)

def get_slopes_intercepts(lines):
    slopes = []
    intercepts = []
    for line in lines:
        x1,y1,x2,y2 = line[0]
        slope = (y2-y1)/(x2-x1)
        inverse_slope = (x2-x1)/(y2-y1)
        intercept = x1 - y1*inverse_slope
        slopes.append(slope)
        intercepts.append(intercept)
    return slopes, intercepts

def detect_lanes(lines):
    pass

def draw_lanes(img, lanes):
    pass

img = cv2.imread("image.jpg")
lines = detect_lines(img)
draw_lines(img,lines)