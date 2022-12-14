# Generated by Django 4.1.3 on 2022-11-30 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perevalapp', '0004_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='media/', verbose_name='Image')),
            ],
        ),
        migrations.AlterField(
            model_name='pereval',
            name='image',
            field=models.ManyToManyField(through='perevalapp.PerevalImages', to='perevalapp.image'),
        ),
        migrations.AlterField(
            model_name='perevalimages',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.image'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
