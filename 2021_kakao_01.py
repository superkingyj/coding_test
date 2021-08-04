import re
def solution(new_id: str):
    # 1단계
    new_id = new_id.lower()
    print("1단계 : "+new_id)
    # 2단계
    new_id = re.sub("[^a-z0-9-_\.]", "", new_id)
    print("2단계 : "+new_id)
    # 3단계
    new_id = re.sub("\.+", ".", new_id)
    print("3단계 : "+new_id)
    # 4단계
    new_id = re.sub("^\.|\.$", "", new_id)
    print("4단계 : "+new_id)
    # 5단계
    if not new_id: new_id = "a"
    print("5단계 : "+new_id)
    # 6단계
    new_id = new_id[:15]
    new_id = re.sub("\.$", "", new_id)
    print("6단계 : "+new_id)
    # 7단계
    while len(new_id) <= 2 :
        new_id = new_id+new_id[-1]
    print("7단계 : "+new_id)
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))