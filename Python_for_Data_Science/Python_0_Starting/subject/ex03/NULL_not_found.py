def NULL_not_found(object: any) -> int:
	if object is None :
		print(f"Nothing: {object} {type(object)}")
		return 0
	# NaN은 항상 자기 자신과 같지 않다고 한다. 따라서 float인지 확인하고 NaN인지 확인.
	elif isinstance(object, float) and object != object :
		print(f"Cheese: {object} {type(object)}")
		return 0
	elif object == 0 :
		print(f"Zero: {object} {type(object)}")
		return 0
	elif object == '':
		print(f"Empty: {object} {type(object)}")
		return 0
	elif object is False :
		print(f"Fake: {object} {type(object)}")
		return 0
	else:
		print("Type not found")
	return 1

# is와 ==의 차이점은 is는 객체의 주소값을 비교하고 ==는 객체의 값 자체를 비교한다.
# is는 객체의 식별자(id)를 비교하므로, 두 객체가 같은 메모리 주소를 가지는지 확인. 값이 같아도 객체가 다르면 is 비교는 실패해야 함
# object로 들어온 값이 0일지라도 비교 대상 0은 다른 메모리 주소를 가지고 있으므로 is 비교는 실패해야 함
# 하지만 인터프리터 내부적으로 0, 1, None, True, False는 캐싱되어 있어서 같은 메모리 주소를 가지고 있음
# 특정 상황에서 Python이 최적화를 통해 리터럴 값(0, '')을 동일한 객체로 재사용하기 때문에 is 비교가 성공할 수 있음
# 따라서 일반적으로는 ==를 사용하는 것이 안전하다.
# 싱글턴 객체의 경우에 is를 사용하는 것이 맞다.