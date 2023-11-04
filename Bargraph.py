import matplotlib.pyplot as pyplot
BAR_WIDTH = 0.35

teama_results = (60, 75, 56, 62, 58)
teamb_results = (55, 68, 80, 73, 55)

index_teama = (1, 2, 3, 4, 5)
index_teamb = [i + BAR_WIDTH for i in index_teama]

ticks = [i + BAR_WIDTH / 2 for i in  index_teama]
ticks_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')


pyplot.bar(index_teama, teama_results, BAR_WIDTH, color='b',
	label='Team A')
pyplot.bar(index_teamb, teamb_results, BAR_WIDTH, color='g',
    label='Team B')



pyplot.xlabel('Labs')
pyplot.ylabel('Scores')
pyplot.title('Scores by Lab')
pyplot.xticks(ticks, ticks_labels)
pyplot.legend()


pyplot.show()

