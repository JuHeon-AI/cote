N = int(input())

if N > 1:
    # 2부터 시작해서 N을 나누어본다.
    factor = 2
    while N > 1:
        while N % factor == 0:
            print(factor)
            N //= factor
        factor += 1
        # 제곱근 이상에서는 N 자체가 소수일 경우가 있을 수 있음
        if factor * factor > N:
            if N > 1:
                print(N)
            break
