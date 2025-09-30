🧪 다양한 print() 사용법 예제
# 1. 기본 출력
print("Hello, World!")  # 문자열 출력

# 2. 변수 출력
name = "Alice"
age = 25
print(name, age)  # 변수 출력: 기본 구분자(공백)로 구분됨

# 3. f-string 포매팅 (Python 3.6 이상)
print(f"My name is {name} and I am {age} years old.")  # f-string을 사용한 문자열 포매팅

# 4. format() 메서드 포매팅
print("My name is {} and I am {} years old.".format(name, age))  # format() 메서드를 사용한 문자열 포매팅

# 5. % 포매팅
print("My name is %s and I am %d years old." % (name, age))  # % 포매팅을 사용한 문자열 포매팅

# 6. 구분자(sep)와 끝 문자(end) 설정
print("2025", "09", "23", sep="-", end="\n")  # 구분자를 "-"로 설정하고 끝 문자를 줄바꿈으로 설정

# 7. 여러 줄 출력
print("""
Hello,
This is a multi-line
string.
""")  # 여러 줄 문자열 출력

# 8. print() 없이 줄바꿈 없이 출력
print("Hello", end=" ")
print("World!")  # end=" "로 설정하여 줄바꿈 없이 출력

# 9. print() 없이 줄바꿈 없이 출력 (빈 print() 사용)
print("Hello", end="")
print("World!")  # end=""로 설정하여 줄바꿈 없이 출력

🛠️ 실행 환경별 실행 방법
1. VS Code에서 실행

파일 확장자: .py

실행 방법:

터미널에서 python 파일명.py 명령어 입력

또는 VS Code의 상단 메뉴에서 ▶️(실행) 버튼 클릭

2. 터미널에서 실행

파일 확장자: .py

실행 방법:

터미널에서 python 파일명.py 명령어 입력

3. Jupyter Notebook에서 실행

파일 확장자: .ipynb

실행 방법:

터미널에서 jupyter notebook 명령어 입력하여 Jupyter Notebook 실행

웹 브라우저에서 열리는 Jupyter Notebook 인터페이스에서 새로운 노트북을 생성하고 코드 셀에 입력하여 실행

📌 참고 사항

VS Code에서 Jupyter Notebook 사용:

VS Code에서 Jupyter Notebook을 사용하려면 Python 확장과 Jupyter 확장이 설치되어 있어야 합니다.

.ipynb 파일을 열면 셀 단위로 코드를 실행할 수 있습니다.

데이터프레임 출력 시 print() 대신 display()를 사용하면 더 깔끔하게 출력됩니다.

출력 포맷팅 팁:

f-string은 가독성이 높고 성능이 우수하여 Python 3.6 이상에서 권장됩니다.

format() 메서드와 % 포매팅은 이전 버전의 Python에서도 사용 가능합니다.