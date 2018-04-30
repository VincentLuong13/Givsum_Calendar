import datetime
import calendar

def get_calendar_variables(c_year = 0, c_month = 0, c_week = 0):
    today_date = datetime.datetime.today()
    if c_year != 0:
        today_date = today_date.replace(year = c_year, day = 1)
    if c_month !=0:
        today_date = today_date.replace(month = c_month,day = 1)
    if c_week !=0:
        today_date = today_date.replace(c_week = c_week,day = 1)

    first_day = {'Sunday': 1,'Monday': 2,'Tuesday': 3,'Wednesday': 4,'Thursday': 5,'Friday': 6,'Saturday': 7}[today_date.replace(day=1).strftime("%A")]
    year = today_date.year
    month = today_date.month
    day = today_date.day

    info_dict = {'cur_name_of_month' :calendar.month_name[month],
    'cur_num_days': range(calendar.monthrange(year,month)[1]),
    'cur_year':year,
    'cur_month':month,
    'cur_day' : day,
    'cur_name_of_day' : datetime.datetime.now().strftime("%A"),
    'first_day':range(first_day-1)}
    
    return info_dict