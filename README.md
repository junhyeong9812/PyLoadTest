# PyLoadTest

개인용 HTTP 부하 테스트 웹 도구
멀티스레드를 활용해 대량 요청을 보내고, 결과를 시각적으로 확인할 수 있도록 지원합니다.
Postman이나 일반적인 REST 클라이언트로는 테스트하기 어려운 대량 트래픽 환경에서 활용할 수 있습니다.

---

## 🚀 주요 기능

- FastAPI 기반의 웹 서버 + HTML/JS 프러티언드
- 웹 UI를 통해 다음 정보 입력 후 부회 테스트 수행:

  - 요청 URL
  - HTTP 메서드 (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
  - 헤더 / 파라미터 / 쿠키 / 바디 입력
  - 요청 횟수 및 동시 실행 스레드 수 설정

- 결과 통계 출력 (성공 / 실패 / 전체 요청 수)

---

## 📂 프로젝트 구조

```
PyLoadTest/
├── app/
│   ├── main.py               # FastAPI 앱 진입점
│   ├── templates/
│   │   └── index.html        # HTML 테스트 페이지
│   ├── static/
│   │   └── script.js         # JS 로직 (요청 전송 및 결과 표시)
│   ├── utils/
│   │   └── load_runner.py    # 머티스레드 요청 실행 로직
│   └── schemas.py            # 요청 스키마 정의
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ 설치 및 실행 방법

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 의언성 설치

```bash
pip install -r requirements.txt
```

### 3. 서버 실행

```bash
uvicorn app.main:app --reload
```

→ 브라우저에서 `http://localhost:8000` 접속

---

## 📈 테스트 방법

1. 웹페이지에서 테스트할 URL과 요청 방식 선택
2. 필요 시 헤더 / 파라미터 / 바디 / 쿠키 입력
3. 요청 횟수, 스레드 수 지정
4. Start Test 버튼 클릭
5. 결과는 하단에 JSON 형식으로 표시됨

---

## 💡 협조 계획

- 응답 시간 평균 / 최소 / 최대값 표시
- 요청 로그 CSV 다운로드
- Chart.js를 활용한 결과 시각화
- WebSocket 기반 실시간 진행률 표시

---

## 💪 기술 스택

- Python 3.10+
- FastAPI
- Uvicorn
- Jinja2 (ud14c마트 렌더링)
- HTML + JavaScript (Vanilla JS)
- ThreadPoolExecutor (머티스레드 요청)

---
