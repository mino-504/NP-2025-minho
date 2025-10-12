# 🧠 NP-2025 | 202011578 최민호

> 2025년 네트워크 프로그래밍 학습/실습 저장소입니다.  
> 각 장(Chapter)별 Jupyter Notebook과 노트를 정리합니다.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white">
  <img alt="Repo Status" src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

---

## 📁 폴더 구조

| 폴더 | 내용 |
|:--|:--|
| [chap01](./chap01) | 네트워크/소켓 기초 |
| [chap02](./chap02) | TCP/UDP 기본 실습 |
| [chap03](./chap03) | 멀티스레드/동시성 |
| [chap04](./chap04) | 파일 전송·에코 서버 |
| [chap05](./chap05) | 종합 과제/정리 |

> 현재 레포 주요 폴더는 `chap01`~`chap05`로 구성되어 있습니다. 언어 분류는 Jupyter Notebook 위주입니다. :contentReference[oaicite:1]{index=1}

---

## ⚙️ 실행 환경

- **Python** 3.x  
- **Jupyter Notebook** (또는 VS Code + Jupyter 확장)
- **OS**: Windows 10/11

### 설치 & 실행
```bash
# 1) 클론
git clone https://github.com/mino-504/NP-2025-minho.git
cd NP-2025-minho

# 2) (선택) 가상환경
python -m venv .venv
# Windows
.venv\Scripts\activate

# 3) 필요 패키지 (있다면 requirements.txt 사용)
pip install -r requirements.txt  # 파일이 없으면 생략 가능

# 4) 노트북 실행
jupyter notebook
```
