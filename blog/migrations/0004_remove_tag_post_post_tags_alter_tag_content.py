# Generated by Django 4.2.3 on 2023-07-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_rename_hashtag_tag_posttag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="post",
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(through="blog.PostTag", to="blog.tag"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="content",
            field=models.CharField(max_length=30),
        ),
    ]
