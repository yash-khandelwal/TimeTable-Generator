# Generated by Django 2.2.7 on 2019-11-16 17:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource_data', '0002_auto_20191116_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200)),
                ('sem', models.IntegerField()),
                ('credits', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('lecture', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('tutorial', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('practical', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('course_intro', models.IntegerField(validators=[django.core.validators.MinValueValidator(2010), django.core.validators.MaxValueValidator(9999)])),
                ('branch_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource_data.Branch')),
            ],
        ),
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
