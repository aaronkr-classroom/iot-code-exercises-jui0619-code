# 3_str.py
#문자열 묶는 방법
f="hong" #큰따옴표
n='길동' #작은따옴표

#문자열 연결하기
fn=f + n

#글자수 확인
ln=len(fn) #6

#작은 따옴표와 큰 따옴표 출력하기
qt1="It's a beautiful day"
qt2='he said, "Hello World!"'
qt3="She said, \"No, it's not!\""
qt4='I\'m hungry.'
qt5='C:\\Windows\\Users\\Desktop\\'

print(1,fn)
print("2 {ln}")
print(3,qt1)
print(f"4: {qt2}")
print(f"5: {qt3}\n\t6: {qt4}\t7: {qt5}")