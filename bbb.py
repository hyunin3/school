# #신규 아이디 생성 마지막 글자는 0부터 9까지의 숫자임을 만족하면 True, 아니면 False
def is_id_valid(user_data):
    #print(user_data)
    #print((user_data)['id'][-1])
    if user_data['id'][-1] == '1':
        return True
    elif user_data['id'][-1] == '2':
        return True
    elif user_data['id'][-1] == '3':
        return True 
    elif user_data['id'][-1] == '4':
        return True
    elif user_data['id'][-1] == '5':
        return True
    elif user_data['id'][-1] == '6':
        return True
    elif user_data['id'][-1] == '7':
        return True
    elif user_data['id'][-1] == '8':
        return True
    elif user_data['id'][-1] == '9':
        return True
    elif user_data['id'][-1] == '0':
        return True
    
    else:
        return False

# # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
