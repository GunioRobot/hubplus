# patches for copies of live server

python manage.py execfile scripts/patch_permissions.py
# patch the all_members group to have "display_name" from theme settings
python manage.py execfile scripts/patch_all_members.py 