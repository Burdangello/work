
score = input("Zadejte score studentů oddělené čárkou a mezerou\n")
score_list = score.split(",")
print(type(score_list))
score_list_number = []

for index in range (0, len(score_list)):
    score_list_number.append(int(score_list[index]))

print((score_list_number))