# Generated by Django 2.1.3 on 2018-11-13 13:11

import adminsortable.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securitypolicy', '0003_auto_20181112_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Section Title', max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='section',
            name='policy',
            field=adminsortable.fields.SortableForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='securitypolicy.Policy'),
        ),
    ]
