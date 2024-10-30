
print("loading nltk")
import nltk
import re
from nltk.corpus import EuroparlCorpusReader
from nltk.text import Text

print("downloading nltk libraries")
nltk.download('punkt_tab')

print("loading europarl corpus")
europarl_read = EuroparlCorpusReader('./europarl/en', '.*')
europarl = Text(europarl_read.words())

print("concordance for 'great'")
europarl.concordance('great')
