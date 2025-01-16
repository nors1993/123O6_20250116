import time
import datetime

from global_var import get_value


def is_candidate_config():
    candidate = False
    candidate_config = get_value('config_dict')['candidate']
    if candidate_config is not None and candidate_config == '1':
        candidate = True
    return candidate

def get_today_str():
    return datetime.date.today().strftime('%Y-%m-%d')

def is_success(response):
    if response is None:
        return False
    if not isinstance(response, dict):
        return False
    if 'result_code' in response:
        return str(response['result_code']) == '0'
    if 'status' in response:
        return response['status']
    return False

def wait_until_time():
    date = get_value('config_dict')['ticketRushTime']
    target_time = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M")

    while True:
        # 获取当前时间
        current_time = datetime.datetime.now()
        # 计算时间差
        time_diff = target_time - current_time
        # 如果时间差为负数，说明已经超过了目标时间
        if time_diff.total_seconds() <= 0:
            break
        # 否则，暂停执行一段时间（留3s以避免过早唤醒）
        time_to_sleep = time_diff.total_seconds()
        if time_to_sleep > 3:
            time_to_sleep -= 3
        time.sleep(time_to_sleep)
