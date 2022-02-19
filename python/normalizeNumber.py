string = input()
engInt = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
perInt = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
perInt2 = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]

for i in range(10):
    string = string.replace(perInt[i], engInt[i])
    string = string.replace(perInt2[i], engInt[i])

print(string)
