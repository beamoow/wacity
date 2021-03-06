# Generated by Django 3.2.3 on 2022-04-21 09:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Gentleman', 'Gentleman'), ('Ladies', 'Ladies'), ('Children', 'Children'), ('Necklace', 'Necklace'), ('Bracelets', 'Bracelets'), ('Ring', 'Ring'), ('Earrings', 'Earrings'), ('Bags', 'Bags'), ('Glasses', 'Glasses'), ('Shoes', 'Shoes'), ('Hats', 'Hats')], max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Detail Description'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category'),
        ),
    ]
