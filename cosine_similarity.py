import math


def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_v1 = math.sqrt(sum(a * a for a in v1))
    norm_v2 = math.sqrt(sum(b * b for b in v2))
    return dot_product / (norm_v1 * norm_v2)


# 가상의 3차원 임베딩 예시
# 축 1: 경제/급여 성향, 축 2: 이동수단 성향, 축 3: 음식 성향
vector_salary = [0.95, 0.05, 0.02]  # "급여 지급 규정"
vector_paycheck = [0.92, 0.08, 0.01]  # "월급 언제 입금돼요?"
vector_airplane = [0.05, 0.98, 0.01]  # "비행기 예약 방법"

sim_1 = cosine_similarity(vector_salary, vector_paycheck)
sim_2 = cosine_similarity(vector_salary, vector_airplane)

print(f"급여 vs 월급 유사도: {sim_1:.4f} (거의 1.0에 가까움!)")
print(f"급여 vs 비행기 유사도: {sim_2:.4f} (완전히 다른 분야)")
