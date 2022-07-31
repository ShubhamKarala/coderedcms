# Generated by Django 3.2.7 on 2021-09-08 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcrx', '0023_auto_20210908_1702'),
        ('testapp', '0005_auto_20210908_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexTestPage',
            fields=[
                ('coderedpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcrx.coderedpage')),
            ],
            options={
                'verbose_name': 'Index Test Page',
            },
            bases=('wagtailcrx.coderedpage',),
        ),
    ]
