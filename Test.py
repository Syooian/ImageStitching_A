import cv2

def main():
    # 開啟 WebCam（預設為 0，若有多個攝影機可調整參數）

    #================================ 列出所有 WebCam 資訊
    # for index in range(0, 11):
    #     print(f"Index: {index}")

    #     try:
    #         cap = cv2.VideoCapture(index)
    #         if not cap.isOpened():
    #             break
    #         print(f"WebCam {index} 可用")
    #         # cap.release()
    #         # index += 1
    #     except Exception as e:
    #         print("錯誤 : "+e)
    #================================

    # while True:
    #     cap = cv2.VideoCapture(index)
    #     if not cap.isOpened():
    #         break
    #     print(f"WebCam {index} 可用")
    #     cap.release()
    #     index += 1

    # if index == 0:
    #     print("沒有可用的 WebCam")







    cap0 = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)

    if not cap0.isOpened():
        print("無法開啟攝影機0")
        return
    if not cap1.isOpened():
        print("無法開啟攝影機1")
        return
    
    # 初始化 OpenCV Stitcher
    Stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
    StitcherOnOff=False

    while True:
        # 讀取攝影機畫面
        ret0, frame0 = cap0.read()
        if not ret0:
            print("無法讀取畫面0")
            break
        # 顯示畫面
        cv2.imshow('WebCam0', frame0)

        ret1, frame1 = cap1.read()
        if not ret1:
            print("無法讀取畫面1")
            break
        # 顯示畫面
        cv2.imshow('WebCam1', frame1)

        # 開啟合併
        #if(cv2.waitKey(1) & 0xFF==ord('s')):
        #    StitcherOnOff =True

        #if(StitcherOnOff):
        if(cv2.waitKey(1) & 0xFF==ord('s')):
            print("Start stitching")

            F0 = frame0
            F1 = frame1

            # 將 frame0 和 frame1 轉成 JPG 並存檔
            cv2.imwrite('frame0.jpg', frame0)
            cv2.imwrite('frame1.jpg', frame1)

            result = None
            status, result = Stitcher.stitch([F0, F1])

            if status == cv2.Stitcher_OK:
                # 顯示合併後的畫面
                cv2.imshow('Stitched WebCam', result)
            else:
                print(f"合併失敗，狀態碼: {status}")


        # 按下 'q' 鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    cap0.release()
    cap1.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()