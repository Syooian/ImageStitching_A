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

        





    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("無法開啟攝影機")
        return

    while True:
        # 讀取攝影機畫面
        ret, frame = cap.read()
        if not ret:
            print("無法讀取畫面")
            break

        # 顯示畫面
        cv2.imshow('WebCam', frame)

        # 按下 'q' 鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()