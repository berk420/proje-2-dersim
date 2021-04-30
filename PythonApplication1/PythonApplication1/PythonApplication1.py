import re

from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
# keyword_processor.add_keyword(<unclean name>, <standardised name>)
"""
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keyword ="I love Big Apple and Bay Area."
keywords_found = keyword_processor.extract_keywords(keyword)
keywords_found
print(keyword)"""


# BU ÖNEMLİ KALSIN
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
new_sentence
# 'I love New York and NCR region.'


kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
kp.add_keyword('Delhi', ('Location', 'Delhi'))
kp.extract_keywords('Taj Mahal is in Delhi.')
# [('Monument', 'Taj Mahal'), ('Location', 'Delhi')]
# NOTE: replace_keywords feature won't work with this.



keyword_dict = {
    "java": ["java_2e", "java programing"],
    "product management": ["PM", "product manager"]
}
# {'clean_name': ['list of unclean names']}
keyword_processor.add_keywords_from_dict(keyword_dict)

text = "The film Titanic was released in 1998"
result = re.match(r".*", text)
type(result)