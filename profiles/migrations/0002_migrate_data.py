from django.db import migrations


def copy_data_to_profiles(apps, schema_editor):
    # Get the old and new Profile models
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    # Copy each old profile to the new profiles app
    for old_profile in OldProfile.objects.all():
        # Create new Profile entries based on the old ones
        NewProfile.objects.create(
            user=User.objects.get(id=old_profile.user_id),
            favorite_city=old_profile.favorite_city
        )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_to_profiles),
    ]
