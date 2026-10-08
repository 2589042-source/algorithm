# 파이썬 3.10 경량화 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 환경변수 설정 (파이썬 출력 버퍼링 방지)
ENV PYTHONUNBUFFERED=1

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . .

# Gunicorn을 사용하여 Flask 앱 실행 (Cloud Run 기본 포트 8080)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
