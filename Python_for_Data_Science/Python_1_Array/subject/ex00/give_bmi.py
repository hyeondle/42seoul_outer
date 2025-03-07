import sys
# 에러 핸들링 추가

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	result = []
	for i in range(len(height)):
		result.append(weight[i] / height[i] ** 2)
	return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	result = []
	for i in range(len(bmi)):
		if bmi[i] > limit:
			result.append(True)
		else:
			result.append(False)
	return result


def main():
	return


if __name__ == '__main__':
	main()
