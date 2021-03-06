# Generated by Django 2.1.1 on 2022-01-14 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20220114_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='account_balance',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='balance',
            old_name='active_deposit',
            new_name='deposit',
        ),
        migrations.RenameField(
            model_name='balance',
            old_name='bonus_balance',
            new_name='earning',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='last_deposit',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='last_withdrawal',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='pending_withdrawal',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='profit_balance',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='total_balance',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='total_deposit',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='total_withdrawal',
        ),
        migrations.AddField(
            model_name='balance',
            name='deposit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fusion',
            name='username',
            field=models.CharField(blank=True, default='username', max_length=100),
        ),
        migrations.AlterField(
            model_name='balance',
            name='username',
            field=models.CharField(blank=True, default='username', max_length=100),
        ),
    ]
