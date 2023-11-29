from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'


class PoliticalParty(models.Model):
    party_number = models.PositiveIntegerField(unique=True)
    party_name = models.CharField(max_length=50)
    president = models.CharField(max_length=100)
    photo_link = models.CharField(max_length=256)
    vice_president = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.party_number} - {self.party_name}'

    class Meta:
        verbose_name = 'Political Party'
        verbose_name_plural = 'Political Parties'


class Voter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    birth_date = models.DateField()
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Voter'
        verbose_name_plural = 'Voters'
