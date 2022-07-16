import datetime


class Date:
    @staticmethod
    def get_current_date() -> str:
        current = datetime.datetime.now()
        year: str = str(current.year)
        month: str = str(current.month) if len(str(current.month)) == 2 else "0" + str(current.month)
        day: str = str(current.day) if len(str(current.day)) == 2 else "0" + str(current.day)
        response: str = year + month + day
        return response

    @staticmethod
    def compare_date(day1: str, day2: str) -> int:
        day1_year = int(day1[0:4])
        day1_month = int(day1[3:6])
        day1_day = int(day1[5:8])
        day2_year = int(day2[0:4])
        day2_month = int(day2[3:6])
        day2_day = int(day2[5:8])

        if day1_year > day2_year:
            return 1
        if day2_year > day1_year:
            return -1

        if day1_month > day2_month:
            return 1
        if day2_month > day1_month:
            return -1

        if day1_day > day2_day:
            return 1
        if day2_day > day1_day:
            return -1

        return 0