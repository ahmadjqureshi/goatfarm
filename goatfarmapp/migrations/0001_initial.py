# Generated by Django 3.1 on 2020-09-05 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnimalID', models.PositiveIntegerField()),
                ('Heading', models.CharField(max_length=256)),
                ('Description', models.CharField(max_length=1024)),
                ('Price', models.FloatField()),
                ('Height', models.FloatField()),
                ('Length', models.FloatField()),
                ('neckCircumference', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeID', models.PositiveIntegerField()),
                ('TypeName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityID', models.PositiveIntegerField()),
                ('CityName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BreedID', models.PositiveIntegerField()),
                ('BreedName', models.CharField(max_length=64)),
                ('BreedDescription', models.CharField(max_length=1024)),
                ('AnimalTypeFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goatfarmapp.animaltype')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PicID', models.PositiveIntegerField()),
                ('PicFileName', models.CharField(max_length=1024)),
                ('AnimalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goatfarmapp.animaldata')),
            ],
        ),
        migrations.AddField(
            model_name='animaldata',
            name='AnimalTypeFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goatfarmapp.animaltype'),
        ),
        migrations.AddField(
            model_name='animaldata',
            name='BreedFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goatfarmapp.breed'),
        ),
        migrations.AddField(
            model_name='animaldata',
            name='CityFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goatfarmapp.city'),
        ),
    ]