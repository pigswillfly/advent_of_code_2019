
import re

MIN = 172851
MAX = 675869

digits = {}
criteria_matched = 0
for i in range(MIN, MAX):
	i_str = str(i)
	matches = re.split("(\d)(\d)(\d)(\d)(\d)(\d)", i_str)
	for i in range(1, 7):
		digits[i] = int(matches[i])

	if (digits[1] != digits[2]) and (digits[2] != digits[3]) and (digits[3] != digits[4]) and (digits[4] != digits[5]) and (digits[5] != digits[6]):
		continue
	if (digits[2] < digits[1]) or (digits[3] < digits[2]) or (digits[4] < digits[3]) or (digits[5] < digits[4]) or (digits[6] < digits[5]):
		continue

	if (digits[1] == digits[2] == digits[3]):
		if (digits[4] != digits[5]) and (digits[5] != digits[6]):
			continue
		if (digits[3] == digits[4]): 
			if (digits[4] == digits[5]):
				continue
			if (digits[5] != digits[6]):
				continue
	if (digits[2] == digits[3] == digits[4]):
		if (digits[4] == digits[5]):
			continue
		if (digits[5] != digits[6]):
			continue
	if (digits[3] == digits[4] == digits[5]):
		if (digits[2] == digits[3]):
			continue
		if (digits[1] != digits[2]):
			continue
	if (digits[4] == digits[5] == digits[6]):
		if (digits[1] != digits[2]) and (digits[2] != digits[3]):
			continue	
		if (digits[3] == digits[4]):
			if (digits[2] == digits[3]):
				continue
			if (digits[1] != digits[2]):
				continue
	
	criteria_matched+=1

print(criteria_matched)
