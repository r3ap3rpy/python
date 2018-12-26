from collections import Counter
import flashtext


with open('rnj.txt', 'r') as play:
	content = play.read()

processor = flashtext.KeywordProcessor()
processor.add_keyword('proud')
processor.add_keyword('Shakespeare')
processor.add_keyword('hours')
processor.add_keyword('frown')


print(processor.extract_keywords(content))
print(Counter(processor.extract_keywords(content)))