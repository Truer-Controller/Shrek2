import shrek2

while True:
	text = input('Shrek2 > ')
	if text.strip() == "": continue
	result, error = shrek2.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
