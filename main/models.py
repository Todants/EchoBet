from django.db import models


class Accounts(models.Model):

    id_Accounts = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)


class APIKeys(models.Model):

    id_APIKeys = models.AutoField(primary_key=True)
    id_Accounts = models.ForeignKey(Accounts, on_delete=models.CASCADE, to_field='id_Accounts')
    key = models.CharField(max_length=500, blank=False, null=False)
    secret_key = models.CharField(max_length=500, blank=False, null=False)


class Listeners(models.Model):

    id_Listeners = models.AutoField(primary_key=True)
    id_APIKeys = models.ForeignKey(APIKeys, on_delete=models.CASCADE, to_field='id_APIKeys')
    size = models.BigIntegerField(null=False, default=0)
    side = models.CharField(max_length=50, blank=False, null=False)
