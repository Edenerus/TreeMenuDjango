#!/usr/bin/bash
python manage.py migrate --check
# shellcheck disable=SC2034
status=$?
# shellcheck disable=SC2050
if [[ status != 0 ]]; then
  python manage.py makemigrations
  python manage.py migrate
fi
python manage.py collectstatic -c --no-input
python manage.py create_superuser --username=admin \
  --email=admin@mail.ru \
  --password=admin
exec "$@"
