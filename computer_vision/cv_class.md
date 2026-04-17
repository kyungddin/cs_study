# 영상처리 수업 이론

## 휴먼 팩터
- 인간의 Needs를 고려한 설계 및 방법론?


## DCT (Discrete Cosine Transform)
- 고/저주파를 분리한다
    - JPG 압축에 쓰인다


## 이진화 Threshold 값을 상수로 Fix 하지 말 것


# 영상처리 수업 실습


## MFC + OpenCV
- DLL 지연으로 메모리 누수가 발생할 수 있으니 
```
지연 로드된 DLL 항목에 OpenCV DLL 파일 이름 추가
```


## OpenCV의 메모리 할당
- 일반적으로 OpenCV의 Mat Type은 자동으로 메모리 할당을 하는 것을 지원하지만
    - 특정 함수의 경우 메모리 할당을 신경 써줘야 하는데
    - 이는 공식 Reference에서 함수 설명을 통해 참고 가능



## cv::Exception
- 일반적인 catch와 마찬가지로 인자로 포인터를 못 받음
- 따라서 call by reference로 ㄱㄱ


## cv::Mat
- 버퍼 느낌의 변수로 생각하기
- 이미지 생성 시에 설정하는 타입으로 대체적으로 CV_8UC3을 사용한다


## Mat 행렬 접근
- STL 사용 등의 방법을 통해 접근을 할 수 있으나 속도가 느리거나 등의 이유로 안 좋음
- 가장 좋은 법은 uchar* 포인터를 활용해 접근하는 것 (직관적이고 속도가 빠르다)
