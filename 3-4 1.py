# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# font_list=fm.findSystemFonts()
# path=font_list[font_list.index('C:\\WINDOWS\\Fonts\\malgun.ttf')]
# font_name = fm.FontProperties(fname=path, size=18).get_name()
# plt.rc('font', family=font_name)
#
# countries = ['미국', '우크라이나', '캐나다', '러시아', '독일']
# gold = [34,53,24,54,24]
# silver = [23,41,32,14,34]
# bronze = [23,52,34,95,13]
#
# bottom_silver = [a+3 for a in gold]
# bottom_bronze = [a + b+6 for a, b in zip(gold, silver)]
#
# fig, ax = plt.subplots()
# p1 = ax.bar(countries, gold, color='gold', label='Gold')
# p2 = ax.bar(countries, silver, bottom=bottom_silver, label='Silver', color='blue')
# p3 = ax.bar(countries, bronze, bottom=bottom_bronze, label='bronze', color='lightcoral')
#
# plt.xlabel('나라')
# plt.ylabel('메달수')
# plt.title('2015년 리오 올림픽')
# plt.legend()
#
# ax.bar_label(p1, label_type='center')
# ax.bar_label(p2, label_type='center')
# ax.bar_label(p3, label_type='center')
# plt.show()


# import matplotlib.pyplot as plt
#
#
# countries = ['USA', 'KOREA', 'CHINA', 'RUSSIA', 'GERMANY']
# gold = [0.1, 99, 0.1, 0.1, 0.1]
# colors= ['red', 'GREEN', 'blue', 'yellow', 'cyan']
# explode=[35, 26, 13, 36, 1]
#
# plt.pie(gold, explode=explode, labels=countries, colors=colors, autopct='%.1f%%')
# plt.title('medal')
# plt.show()