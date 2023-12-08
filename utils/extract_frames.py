import cv2
import os

def video_to_frames(input_video, output_root_folder):
    # 동영상 파일 열기
    cap = cv2.VideoCapture(input_video)

    # 동영상 파일이 열리는지 확인
    if not cap.isOpened():
        print("동영상 파일을 열 수 없습니다.")
        return

    # 동영상 파일명에서 확장자를 제외한 이름을 추출
    video_name = os.path.splitext(os.path.basename(input_video))[0]

    # 출력 폴더 생성 또는 기존 폴더 사용
    output_folder = os.path.join(output_root_folder, video_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 프레임 수, 초당 프레임 수, 프레임 크기 가져오기
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"프레임 수: {frame_count}, 초당 프레임 수: {fps}, 프레임 크기: {frame_width} x {frame_height}")

    # 초당 프레임 수만큼 프레임을 추출
    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 초 단위로 파일 저장
        current_second = frame_index // int(fps)
        frame_filename = f"{output_folder}/second_{current_second:04d}.jpg"
        cv2.imwrite(frame_filename, frame)

        # 진행 상황 출력
        print(f"프레임 {frame_index + 1}/{frame_count} 저장 중...")

        frame_index += 1

    # 동영상 파일 닫기
    cap.release()

    print("프레임 추출 완료")