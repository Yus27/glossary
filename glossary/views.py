from django.shortcuts import render
from glossary.models import Pair


def index(request):
    return render(request, 'glossary/index.html', {'results': []})


def result(request):
    source = request.POST['qr'].strip()
    from glossary.words import prepareWords
    words_source = prepareWords(source)
    words_source.sort()

    results = Pair.objects.all()
    for result in results:
        result.findCorrelationCoef(words_source)
    results = [res for res in results if res.coef > 0]
    results = sorted(results, key=lambda p: p.coef, reverse=True)

    return render(request, 'glossary/index.html', {'results': results})


