from django.db import migrations


def copy_data_to_lettings(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Créer une correspondance entre les anciens et les nouveaux adresses
    address_mapping = {}
    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        address_mapping[old_address.id] = new_address

    # Créer les nouvelles instances de Letting avec les nouvelles adresses
    for letting in Letting.objects.all():
        NewLetting.objects.create(
            title=letting.title,
            address=address_mapping[letting.address_id]
        )


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_to_lettings),
    ]
