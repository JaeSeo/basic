문자열은 immutable(변할 수 없는)하기 때문에 security_number를 mutable(변할 수 있는)하고 다루기 편한 리스트로 만들어 사용하겠습니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = []
    for i in range(len(security_number)):
        num_list.append(security_number[i])
사실 문자열을 한번에 리스트로 바꾸고 싶으면 곧바로 형 변환을 쓸 수도 있습니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)
이제 마지막 네 요소, 즉 인덱스 len(num_list) - 4부터 인덱스 len(num_list) - 1의 값들을 *로 바꿔주면 하면 됩니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"
마지막으로 이 리스트를 이제 다시 문자열로 만들어서 리턴시켜 주어야합니다.

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str
사실 이것도 파이썬에서는 한번에 할 수 있는 방법이 있고요...

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = "".join(num_list)

    return total_str
그리고 사실 이것보다 더 쉬운 방법은...

def mask_security_number(security_number):
    return security_number[:len(security_number) - 4] + "****"