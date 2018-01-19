from django.db import models


# class Tag(models.Model):
#     tag = models.CharField(max_length=200, blank=False, unique=True)
#
#     def __str__(self):
#         return self.tag


# class Source(models.Model):
#     authors = models.CharField(verbose_name="Авторы", max_length=1000, blank=True)
#     caption = models.CharField(verbose_name="Название",max_length=2000, blank=False)
#     journal = models.CharField(verbose_name="Журнал",max_length=2000, blank=True)
#     volume = models.CharField(verbose_name="Номер",max_length=20, blank=True)
#     year = models.IntegerField(verbose_name="Год", null=True, blank=True)
#     file = models.FileField(verbose_name="Имя файла", blank=True, upload_to='')
#
#     def __str__(self):
#         S = '"%s"' % self.caption
#         if self.authors != "":
#             S = self.authors + " " + S
#         return S


class Pair(models.Model):
    english_phrase = models.CharField(max_length=2000, blank=False)
    russian_phrase = models.CharField(max_length=2000, blank=False)
    context = models.TextField(blank=True)
    coef = -1
    #source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    #tags = models.ManyToManyField(Tag, null=True, blank=True)
    #comments = models.TextField(blank=True)

    def __str__(self):
        return self.english_phrase + " <=> " + self.russian_phrase

    def russianToWords(self):
        from glossary.words import prepareWords
        return prepareWords(self.russian_phrase)

    def findCorrelationCoef(self, request_words):
        base_words = self.russianToWords()
        S = 0
        for request_word in request_words:
            if request_word in base_words:
                S += 1
        self.coef = S/len(request_words)
        #return coef