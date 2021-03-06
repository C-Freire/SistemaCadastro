# Generated by Django 4.0 on 2021-12-22 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ativo',
            options={'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='CategoriaAtivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ativo.ativo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ativo.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='ativos',
            field=models.ManyToManyField(through='Ativo.CategoriaAtivos', to='Ativo.Ativo'),
        ),
    ]
