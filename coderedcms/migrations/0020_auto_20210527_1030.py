# Generated by Django 3.1.7 on 2021-05-27 14:30

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcrx', '0019_spelling_corrections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderedpage',
            name='struct_org_hours',
            field=wagtail.fields.StreamField([('hours', wagtail.blocks.StructBlock([('days', wagtail.blocks.MultipleChoiceBlock(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], help_text='For late night hours past 23:59, define each day in a separate block.', verbose_name='Days')), ('start_time', wagtail.blocks.TimeBlock(verbose_name='Opening time')), ('end_time', wagtail.blocks.TimeBlock(verbose_name='Closing time'))]))], blank=True, verbose_name='Hours of operation'),
        ),
    ]
