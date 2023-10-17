# Network_homwork

```
arclength = cv2.arcLength(contour, True)
epsilon = coefficient * arclength
approx = cv2.approxPolyDP(contour, epsilon, True)
```

# Calculate the error rate of x-aixs and y-aixs
```
x_error_rate = abs(x-CENTER_X) / CENTER_X * 100
y_error_rate = abs(y-CENTER_Y) / CENTER_Y * 100
```
