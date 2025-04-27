import cv2

# Initialize background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

def detect_changes(frame):
    fgmask = fgbg.apply(frame)

    # Find contours (moving objects)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter small noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return frame
