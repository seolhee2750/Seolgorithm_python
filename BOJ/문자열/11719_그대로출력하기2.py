while True:
    try:
        print(input())
    except EOFError:
        break

"""
import sys
print(sys.stdin.read())

readline말고 read 사용하면 EOF 발생 전까지 계속 입력 받기 가능
"""