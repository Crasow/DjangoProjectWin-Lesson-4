# Generated by Django 3.2 on 2022-09-19 16:03

from django.db import migrations


def forwards_func(apps, schema_editor):
    Lesson = apps.get_model("mainapp", "Lesson")
    Course = apps.get_model("mainapp", "Courses")

    Lesson.objects.create(
        course=Course.objects.get(id=1),
        num=1,
        title='Start',
        description='Start of learning'
    )
    Lesson.objects.create(
        course=Course.objects.get(id=1),
        num=2,
        title='Second',
        description='Second part'
    )
    Lesson.objects.create(
        course=Course.objects.get(id=1),
        num=3,
        title='Third',
        description='Third part'
    )
    Lesson.objects.create(
        course=Course.objects.get(id=1),
        num=4,
        title='Fourth',
        description='Fourth part'
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    # Delete objects
    Lesson.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0003_courses_migration'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
