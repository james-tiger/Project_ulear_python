# Generated by Django 4.0.6 on 2024-12-18 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profession', '0002_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryByCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='key_skills',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='posted_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title',
            field=models.CharField(blank=True, default='Default Title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='currency',
            field=models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], default='RUB', max_length=10),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(related_name='vacancies', to='profession.skill'),
        ),
    ]
