from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20170503_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.FileField(upload_to='music'),
        ),
    ]
