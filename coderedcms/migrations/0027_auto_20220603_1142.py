# Generated by Django 3.2.13 on 2022-06-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcrx', '0026_auto_20220513_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carouselslide',
            options={'ordering': ['sort_order'], 'verbose_name': 'Carousel Slide'},
        ),
        migrations.AlterModelOptions(
            name='classifierterm',
            options={'ordering': ['sort_order'], 'verbose_name': 'Classifier Term', 'verbose_name_plural': 'Classifier Terms'},
        ),
    ]
