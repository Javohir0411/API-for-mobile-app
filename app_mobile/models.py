from django.db import models


class WordGroup(models.Model):
    group_name = models.CharField(max_length=150)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name_plural = 'WordGroups'
        db_table = 'wordgroups'


class Homonym(models.Model):
    homonym_name = models.CharField(max_length=150)
    homonym_origin = models.CharField(max_length=100)
    homonym_word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE)
    homonym_meaning = models.TextField()
    homonym_example = models.TextField()

    def __str__(self):
        return self.homonym_name

    class Meta:
        verbose_name_plural = 'Homonyms'
        db_table = 'homonyms'
