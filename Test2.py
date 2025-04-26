import cv2

def main():
    # 開啟兩個 WebCam
    cap1 = cv2.VideoCapture(0)  # 第一個攝影機
    cap2 = cv2.VideoCapture(1)  # 第二個攝影機

    if not cap1.isOpened() or not cap2.isOpened():
        print("無法開啟其中一個攝影機")
        return

    # 初始化 OpenCV Stitcher
    stitcher = cv2.Stitcher_create()

    while True:
        # 從兩個攝影機讀取畫面
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("無法讀取畫面")
            break

        # 將兩個畫面合併
        result = None
        status, result = stitcher.stitch([frame1, frame2])

        if status == cv2.Stitcher_OK:
            # 顯示合併後的畫面
            cv2.imshow('Stitched WebCam', result)
        else:
            print(f"合併失敗，狀態碼: {status}")

        # 按下 'q' 鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()