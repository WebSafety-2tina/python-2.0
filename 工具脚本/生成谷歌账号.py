import random
import string

# 生成多少个账号和密码
num_accounts = 43

for i in range(num_accounts):
    # 生成随机的用户名（假设使用gmail.com域）
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + "@gmail.com"

    # 生成随机的密码（包括大小写字母和符号，可以根据需求修改密码长度）
    password_length = 12  # 密码长度
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    # 打印生成的账号和密码
    print(f"Account {i + 1}:")
    print("URL: https://mail.google.com/")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print()
