#신규 아이디 생성 마지막 글자는 0부터 9까지의 숫자임을 만족하면 True, 아니면 False
def is_id_valid(user_data):
    for i in range(10):    
        if user_data['id'][-1] == str(i):
            return True
    
    else:
        return False #반복이 시작되는 위치로 보내야 리스트의 끝까지 반복함
    #    else:   
    #         return False 
    #바로 밑에 두면 처음에 레인지돌 때 0에서 i값과 같지 않으면 바로 
    #return으로 보내고 Fales 나옴.

# 아래의 코드는 수정하지 않습니다.
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