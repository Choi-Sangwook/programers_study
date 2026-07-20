def solution(today, terms, privacies):
    answer = []

    # 약관 종류별 유효기간 저장
    term_dict = {}

    for term in terms:
        term_type, month = term.split()
        term_dict[term_type] = int(month)

    # 오늘 날짜를 총 일수로 변환
    today_days = convert_to_days(today)

    for index, privacy in enumerate(privacies, start=1):
        collected_date, term_type = privacy.split()

        # 개인정보 수집 날짜를 총 일수로 변환
        collected_days = convert_to_days(collected_date)

        # 파기 시작 날짜
        expiration_date = collected_days + term_dict[term_type] * 28

        # 오늘이 파기 시작 날짜 이상이라면 파기
        if today_days >= expiration_date:
            answer.append(index)

    return answer


def convert_to_days(date):
    year, month, day = map(int, date.split("."))

    return year * 12 * 28 + month * 28 + day