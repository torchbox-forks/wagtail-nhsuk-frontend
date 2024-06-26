# Generated by Django 2.1.8 on 2019-05-02 14:18

from django.db import migrations, models
import django.db.models.deletion

import wagtail.blocks as wagtail_blocks
import wagtail.fields as wagtail_fields

import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0007_panel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail_fields.StreamField([('promo', wagtail_blocks.StructBlock([('url', wagtail_blocks.URLBlock(label='URL', required=True)), ('heading', wagtail_blocks.CharBlock(required=True)), ('description', wagtail_blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail_blocks.CharBlock(required=False)), ('size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2))])), ('promo_group', wagtail_blocks.StructBlock([('column', wagtail_blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('promos', wagtail_blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
