n = input()
nums = list(map(lambda x: int(x), list(input())))
print(sum(nums))

"""
두 번째 풀이

n = int(input())
nums = map(int, list(input()))
print(sum(nums))

=> 결과는 같으나, 첫 번째 풀이가 메모리, 시간 면에서 모두 우수하다.
그리고 map을 한 결과를 list로 묶어주었기에 첫 번째 풀이에서 nums를 출력하면 list의 형태로 출력되지만,
두 번째 풀이의 경우 map으로 바꿔 준 후 끝났기에, nums 출력 시 map object로 출력된다.
즉, list에 map 활용 시 list 형태 그대로를 유지하지 않는다.

또한, lambda를 활용한 경우, 그냥 map에서 int로 변환한 경우보다 시간에서 유리했다.
"""