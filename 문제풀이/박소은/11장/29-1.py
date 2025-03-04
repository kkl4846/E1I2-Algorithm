# 29. 보석과 돌

def numJewelsInStones(self, J: str, S: str) -> int:
    freqs = {}  # 해시테이블 선언
    count = 0

    # 돌(S)의 빈도 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    # 보석(J)의 빈도 수 합산
    for char in J:
        if char in freqs:
            count += freqs[char]
    
    return count