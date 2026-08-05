def solution(diffs, times, limit):
    def can_solve(level):
        total_time = 0
        time_prev = 0

        for diff, time_cur in zip(diffs, times):
            wrong = max(0, diff - level)

            total_time += time_cur + wrong * (time_cur + time_prev)

            # 이미 제한 시간을 넘었다면 더 계산할 필요가 없음
            if total_time > limit:
                return False

            time_prev = time_cur

        return True

    left = 1
    right = max(diffs)

    while left < right:
        mid = (left + right) // 2

        if can_solve(mid):
            # mid로 가능하므로 더 낮은 숙련도 탐색
            right = mid
        else:
            # mid로 불가능하므로 더 높은 숙련도 탐색
            left = mid + 1

    return left