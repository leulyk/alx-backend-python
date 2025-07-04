# Generated by Django 5.2.1 on 2025-06-01 08:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('conversation_id', models.UUIDField(default=uuid.UUID('7a9e5339-408b-4d17-898a-121856e51bad'), editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.UUIDField(default=uuid.UUID('acce3036-04c6-4625-8737-789a85738cc0'), editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='chats_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='chats_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.UUID('49bddd80-8724-4428-b2bb-0ea39ab20484'), editable=False, primary_key=True, serialize=False)),
                ('message_body', models.TextField()),
                ('sent_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.conversation')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.user')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(to='chats.user'),
        ),
    ]
