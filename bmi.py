while True:
#使用者輸入資料
	try:
		height = input('請輸入身高︰ ')
		height = float(height)
		weight = input('請輸入體重︰ ')
		weight = float(weight)
	except:
		print('輸入錯誤')
	else:

#身高的單位
		if height >= 3 and height < 10:
			height = float(height * 0.3048)
		elif height >= 10:
			height = float(height / 100)

#體重的單位
		if weight >= 100:
			weight = float(weight / 2.2)

#BMI
		bmi = weight / height / height
		bmi = round(bmi, 1)

#第一句
		height = round(height, 2)
		height = str(height)
		weight = round(weight, 1)
		weight = str(weight)
		para1 = str('你的身高是 ' + height + 'm，你的體重是 ' + weight + 'kg。')
		print(para1)

#第二句
		if bmi < 18.5:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，過輕。')
		elif 18.5 <= bmi and bmi < 24:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，正常。')
		elif 24 <= bmi and bmi < 27:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，過重。')
		elif 27 <= bmi and bmi < 30:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，輕度肥胖。')
		elif 30 <= bmi and bmi < 35:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，中度肥胖。')
		elif bmi >= 35:
			para2 = str('你的 BMI 是 ' + str(bmi) + ' ，重度肥胖。')
		print(para2)

#儲存報告
		report = open("bmi.txt", "w")
		report.write(para1 + '\n' + para2)

		message = input('請按 Enter 鍵繼續......')