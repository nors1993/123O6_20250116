sms_code = None

def check_sms_code(content):
    global sms_code
    print(content)
    sms_code = content
    if (content.isdigit() and len(content) <= 6) or len(content) == 0:
        return True
    return False


def get_sms_code():
    return sms_code


def destroy():
    pass


def input_sms_code(submit_callback):
    user_input = input("请输入短信验证码, 按回车键提交：")
    check_sms_code(user_input.strip())
    submit_callback()
