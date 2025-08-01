import cv2

def check_liveness():
    cap = cv2.VideoCapture(0)
    print("Look into the camera and blink...")

    blink_count = 0
    for _ in range(100):
        ret, frame = cap.read()
        cv2.imshow("Liveness Check", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Add real liveness detection logic with ML model here
        blink_count += 1  # mock for testing

    cap.release()
    cv2.destroyAllWindows()
    return blink_count > 5
