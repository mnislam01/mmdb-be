# Generated by Django 3.0.7 on 2020-06-12 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import movie.model_validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifer accross different system. this is guaranteed to be unique')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time the object created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time the object last updated')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifer accross different system. this is guaranteed to be unique')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time the object created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time the object last updated')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True)),
                ('rating', models.IntegerField(choices=[(0, '0 Star'), (1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=0, validators=[movie.model_validators.rating_validator])),
                ('genre', models.ManyToManyField(related_name='movies', to='movie.Genre')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifer accross different system. this is guaranteed to be unique')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time the object created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time the object last updated')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddIndex(
            model_name='watchlist',
            index=models.Index(fields=['user', 'movie'], name='movie_watch_user_id_639a88_idx'),
        ),
        migrations.AddConstraint(
            model_name='watchlist',
            constraint=models.UniqueConstraint(fields=('user', 'movie'), name='unique_movie_list'),
        ),
    ]
