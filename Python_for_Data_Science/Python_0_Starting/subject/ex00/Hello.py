ft_list		= ["Hello", "tata!"]
ft_tuple	= ("Hello", "toto!")
ft_set		= {"Hello", "tutu!"}
ft_dict		= {"Hello" : "titi"}

#리스트는 수정 가능
ft_list[1] = "World!"
#튜플은 수정 불가능 -> 리스트로 변환 후 수정
temp_list = list(ft_tuple)
temp_list[1] = "Korea!"
ft_tuple = tuple(temp_list)
#set은 수정 가능, 그러나 출력 순서가 랜덤
ft_set.remove("tutu")
ft_set.add("Seoul!")
#dict는 키-값 쌍으로 수정 가능
ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)