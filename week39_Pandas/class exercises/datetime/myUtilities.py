from datetime import datetime, date, time, timedelta


def get_meeting_dates(period_as_timedelta, time_of_day, number_of_meetings, start_date=date.today()):
    meeting_span = period_as_timedelta / number_of_meetings
    meeting_list = []
    counter = 1
    while counter <= number_of_meetings:
        counter += 1
        days_to_jump = meeting_span * counter
        combine_date_time = datetime.combine(
            (start_date + days_to_jump), time_of_day)
        meeting_list.append(combine_date_time)
    return meeting_list


if __name__ == "__main__":
    print(get_meeting_dates(timedelta(days=20), time(12, 30), 10))
