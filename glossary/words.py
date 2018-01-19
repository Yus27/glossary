import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def toNormalForm(token):
    p = morph.parse(token)[0]
    return p.normal_form


def prepareWords(source):
    import re
    tokens = re.split("\W+", source)
    words = [toNormalForm(token) for token in tokens]
    return words