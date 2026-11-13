def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # 50글자씩 겹치면서 이동
    return chunks


sample_doc = (
    "인공지능 솔루션 아키텍트는 고객사의 비즈니스 문제를 정의하고, "
    "클라우드 인프라와 파운데이션 모델을 최적의 비용으로 연결하는 시스템을 설계합니다. "
    "단순한 모델 파인튜닝보다 데이터 거버넌스, 지연시간 단축, 환각 방지 파이프라인이 더 중요한 역량입니다."
)

result_chunks = chunk_text(sample_doc, chunk_size=80, overlap=20)

for i, chk in enumerate(result_chunks, 1):
    print(f"[조각 {i}] (길이 {len(chk)}자): {chk}")
