from django.db import models

from users.models import User


class Drug(models.Model):

    name = models.TextField(
        verbose_name='Название',
        max_length=50, unique=True
    )

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return f'{self.name}'


class Box(models.Model):

    name = models.TextField(
        verbose_name='Название',
        max_length=50
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='author_box'
    )
    drugs = models.ManyToManyField(
        Drug, verbose_name='Препарат',
        related_name='box',
        through='DrugBox', blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'name'],
                name='unique_author_box'
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.author}'


class DrugBox(models.Model):

    PIECES = 'шт.'
    MILLILITER = 'мл.'
    AMPOULE = 'ампулы'
    PILLS = 'таблетки'
    UNITS = (
        ('pieces', PIECES),
        ('milliliter', MILLILITER),
        ('ampoule', AMPOULE),
        ('pills', PILLS)
    )

    box = models.ForeignKey(
        Box, on_delete=models.CASCADE,
        related_name='drugs_in_box',
        verbose_name='Бокс'
    )
    drug = models.ForeignKey(
        Drug, on_delete=models.CASCADE,
        related_name='drugs_in_box',
        verbose_name='Препарат'
    )
    expiration_date = models.DateField(verbose_name='Срок годности')
    amount = models.PositiveIntegerField(verbose_name='Количество')
    unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=max([len(unit[0]) for unit in UNITS]),
        choices=UNITS,
    )

    class Meta:
        ordering = ('box',)
        verbose_name = 'Лекарство в боксе'
        verbose_name_plural = 'Лекарства в боксе'
        constraints = [
            models.UniqueConstraint(
                fields=['box', 'drug', 'unit'],
                name='unique_drug_in_box'
            )
        ]

    def __str__(self):
        return f'{self.box.name}, {self.drug}'
