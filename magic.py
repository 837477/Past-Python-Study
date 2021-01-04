class MyInt(int):
    # __add__ 변경
    def __add__(self, other):
        return '{} 더하기 {} 는 {} 입니다'.format(self.real, other.real, self.real + other.real)

# 인스턴스 생성
my_num = MyInt(5)

print(my_num + 5)  # => 5 더하기 5 는 10 입니다
