# Generated by Django 5.2 on 2025-04-13 11:20

import project_excel_comparison.models
import project_excel_comparison.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_excel_comparison', '0005_remove_comparisonsummary_comparison_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(storage=project_excel_comparison.storage.PreserveFilenameStorage(), upload_to=project_excel_comparison.models.user_directory_path),
        ),
    ]
