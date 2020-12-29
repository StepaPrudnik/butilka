data_base = {
    "Stepa": "1234567890",
    "Anatoliy": "0987654321"
}


def check_password(login, password):
    if login in data_base:
        if data_base[login] == password:
            return True
        return False


user_login = "Anatoliy"
count = 0
passwords = ["1", "2", 'dfs', 'ggg']

with open("pop-passwords.txt") as passwords_file:
    for line in passwords_file:
        user_password = line.strip()
        if check_password(user_login, user_password) == True:
            print(f"попытка №{count} пароль подошёл")
            break
        else:
            count+=1