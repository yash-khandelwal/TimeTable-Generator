# Generated by Django 2.2.7 on 2019-11-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse1', models.CharField(blank=True, max_length=10, null=True)),
                ('cse2', models.CharField(blank=True, max_length=10, null=True)),
                ('cse3', models.CharField(blank=True, max_length=10, null=True)),
                ('cse4', models.CharField(blank=True, max_length=10, null=True)),
                ('cse5', models.CharField(blank=True, max_length=10, null=True)),
                ('cse6', models.CharField(blank=True, max_length=10, null=True)),
                ('cse7', models.CharField(blank=True, max_length=10, null=True)),
                ('cse8', models.CharField(blank=True, max_length=10, null=True)),
                ('ece1', models.CharField(blank=True, max_length=10, null=True)),
                ('ece2', models.CharField(blank=True, max_length=10, null=True)),
                ('ece3', models.CharField(blank=True, max_length=10, null=True)),
                ('ece4', models.CharField(blank=True, max_length=10, null=True)),
                ('ece5', models.CharField(blank=True, max_length=10, null=True)),
                ('ece6', models.CharField(blank=True, max_length=10, null=True)),
                ('ece7', models.CharField(blank=True, max_length=10, null=True)),
                ('ece8', models.CharField(blank=True, max_length=10, null=True)),
                ('it1', models.CharField(blank=True, max_length=10, null=True)),
                ('it2', models.CharField(blank=True, max_length=10, null=True)),
                ('it3', models.CharField(blank=True, max_length=10, null=True)),
                ('it4', models.CharField(blank=True, max_length=10, null=True)),
                ('it5', models.CharField(blank=True, max_length=10, null=True)),
                ('it6', models.CharField(blank=True, max_length=10, null=True)),
                ('it7', models.CharField(blank=True, max_length=10, null=True)),
                ('it8', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
