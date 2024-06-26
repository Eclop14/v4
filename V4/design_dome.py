
# 전역 변수 선언
material = ''
diameter = 0
thickness = 0
area = 0
weight = 0

# 화성의 중력 (지구 중력의 약 38%)
MARS_GRAVITY = 0.38

# pi 값 정의
PI = 3.141592653589793

def sphere_area(diameter, material='유리', thickness=1):
    global area, weight

    # 면적 계산 (4πr^2)
    radius = diameter / 2
    area = 4 * PI * radius ** 2

    # 부피 계산 (면적 * 두께)
    volume = area * (thickness / 100)  # 두께를 m 단위로 변환

    # 재질에 따른 밀도 설정 (kg/m^3)
    densities = {
        '유리': 2400,
        '알루미늄': 2700,
        '탄소강': 7850
    }

    # 질량 계산 (부피 * 밀도)
    mass = volume * densities.get(material, 2400)

    # 화성에서의 무게 계산 (질량 * 화성 중력)
    weight = mass * MARS_GRAVITY

    return area, weight

def get_input(prompt, type_func):
    while True:
        try:
            value = type_func(input(prompt))
            if isinstance(value, (int, float)) and value <= 0:
                print('0보다 큰 값을 입력해주세요.')
                continue
            return value
        except ValueError:
            print('올바른 값을 입력해주세요.')

def get_continue_input():
    while True:
        response = input('계속하시겠습니까? (y/n): ').lower()
        if response in ['y', 'n']:
            return response == 'y'
        print('y 또는 n을 입력해주세요.')

def main():
    global material, diameter, thickness

    while True:
        material = get_input('재질을 입력하세요 (유리/알루미늄/탄소강): ', str)
        if material not in ['유리', '알루미늄', '탄소강']:
            print('유효한 재질을 입력해주세요.')
            continue

        diameter = get_input('지름을 입력하세요 (m): ', float)
        thickness = get_input('두께를 입력하세요 (cm): ', float)

        area, weight = sphere_area(diameter, material, thickness)

        print(f'재질 => {{material}}, 지름 => {{diameter:.3f}}, 두께 => {{thickness:.3f}}, '
              f'면적 => {{area:.3f}}, 무게 => {{weight:.3f}} kg')

        if not get_continue_input():
            break

if __name__ == '__main__':
    main()
