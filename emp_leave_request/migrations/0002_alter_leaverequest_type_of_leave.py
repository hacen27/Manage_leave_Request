# Generated by Django 3.2.15 on 2023-01-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_leave_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='type_of_leave',
            field=models.CharField(choices=[('Conge Malade', 'Conge Malade'), ('Conge Pro', 'Conge Pro'), ('Urgence Conge', 'Urgence Conge'), ('Conge Impaye', 'Conge Impaye ')], max_length=50),
        ),
    ]
