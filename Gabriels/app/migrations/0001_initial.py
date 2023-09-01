# Generated by Django 4.2.2 on 2023-08-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Det',
            fields=[
                ('userid', models.AutoField(db_column='UserId', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=20, null=True)),
                ('useraddress', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='UserAddress', max_length=30, null=True)),
                ('userphone', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='UserPhone', max_length=25, null=True, unique=True)),
                ('usermail', models.CharField(blank=True, db_column='UserMail', max_length=20, null=True, unique=True)),
                ('userprofileimg', models.ImageField(blank=True, db_column='UserProfileImg', max_length=3000, null=True, upload_to='C:/Users/Best/Documents/Gabriels/static/image/')),
                ('dateupdated', models.DateTimeField(blank=True, db_column='DateUpdated', null=True)),
            ],
            options={
                'db_table': 'det',
                'managed': False,
            },
        ),
    ]
