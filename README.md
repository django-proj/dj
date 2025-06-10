# FastAPI Ledger System

## 소개
가계부 기능을 제공하는 FastAPI 기반 백엔드 프로젝트입니다.

## 폴더 구조
```
router/
    main.py           # FastAPI 앱 초기화 및 라우터 등록
    ledger_router.py  # 가계부 관련 라우터
```

## 실행 방법
1. 가상환경 활성화
2. 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```
3. 서버 실행
   ```bash
   uvicorn router.main:app --reload
   ```

## 주요 엔드포인트
- `/` : 헬스체크
- `/ledger` : 가계부 라우터 