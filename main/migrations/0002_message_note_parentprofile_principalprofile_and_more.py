# Generated by Django 4.2.2 on 2023-06-14 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcast', models.BooleanField(default=False)),
                ('message_title', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('message', models.TextField(blank=True, default='', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_message', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrincipalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_class', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('principal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='principal_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_class', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to='main.subject')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('reason', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('month', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_salary', to='main.teacherprofile')),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='shipping_order',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='ShippingOrder',
        ),
        migrations.AddField(
            model_name='parentprofile',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_profile', to='main.studentprofile'),
        ),
        migrations.AddField(
            model_name='parentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_note', to='main.studentprofile'),
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to='main.subject'),
        ),
        migrations.AddField(
            model_name='note',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teahcer_note', to='main.teacherprofile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='main.studentprofile'),
        ),
    ]
