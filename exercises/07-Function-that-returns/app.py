def dollar_to_euro(dollar_value):
	return dollar_value * 0.91

def euro_to_yen(euro_value):
	return euro_value * 161.70

####### ↓ YOUR CODE BELOW ↓ #######
# def dollar_to_yen(dollar):
# 	euro = dollar_to_euro(dollar)
# 	yen = euro_to_yen(euro)
# 	return yen

# print(dollar_to_yen(137))

euro = dollar_to_euro(137)
yen = euro_to_yen(euro)
print(yen)