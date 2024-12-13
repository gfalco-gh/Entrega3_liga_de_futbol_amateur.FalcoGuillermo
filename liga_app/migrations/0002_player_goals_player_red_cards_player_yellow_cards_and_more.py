# Generated by Django 5.1.3 on 2024-12-11 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='red_cards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='yellow_cards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_conceded',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_scored',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('home_score', models.PositiveIntegerField(default=0)),
                ('away_score', models.PositiveIntegerField(default=0)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='liga_app.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='liga_app.team')),
            ],
        ),
    ]
