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

    today = datetime.datetime.today()
    info_dict = {'cur_name_of_month' :calendar.month_name[month],
    'cur_num_days': range(calendar.monthrange(year,month)[1]),
    'cur_year':year,
    'cur_month':month,
    'cur_day' : day,
    'today_day' : today.day,
    'today_month': today.month,
    'today_year': today.year,
    'cur_name_of_day' : datetime.datetime.now().strftime("%A"),
    'first_day':range(first_day-1),
    'num_day': first_day - 1,
    'remainder': (8-first_day),
    'row_six': (calendar.monthrange(year,month)[1] + first_day - 1) <= 35,
    }
    
    return info_dict

def handle_year_info(year):
    return_dict = {}
    for i in range(12):
        info = get_calendar_variables(c_year = year, c_month = i+1)

        return_dict[info['cur_name_of_month']] = info


    return return_dict