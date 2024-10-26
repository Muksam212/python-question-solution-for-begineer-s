ex_dict = {"Mark":"1234", "Henry":"Password123"}


def check_password(ex_dict, check):
    for name, password in ex_dict.items():
        if name == check[0] and password == check[1]:
            return True

check = ("Mark", "1234")    
print(check_password(ex_dict, check))