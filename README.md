
# Site Pykafe

### Etapa-etapa atu run site ida ne'e mak hanesan tuir mai ne'e:

Kria projetu pykafe uza pyenv.
loke terminal no ketik etapa sira tuir mai nee:
- pyenv virtualenv 3.6.6 pykafe
- kria folder ho naran pykafe
- cd ba folder pykafe
- pyenv local pykafe

Atu setup yarn mak hanesan tuir mai ne'e:
```curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - sudo apt-get install -y nodejs curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list sudo apt-get update && sudo apt-get install yarn```

Se iha server ita presisa download GeoLite2-Country:
- cd ~/Devel/pykafe/pykafe/pykafe
- wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
- tar -xvzf GeoLite2-City*.gz
- mv GeoLite2-City GeoLite2_City

- settings/base.py
    - RECAPTCHA_PUBLIC_KEY = "public_key"
    - RECAPTCHA_PRIVATE_KEY = "private_key"
    - Atu tau `public_key` no `private_key` presisa ba registu iha link ida ne'e: https://www.google.com/recaptcha/intro/v3.html
    - Admin console

No tuir mai:
1. git clone git@github.com:pykafe/pykafe.git
2. pip install -r requirements.txt
3. yarn install
4. ./manage.py migrate
5. ./manage.py createsuperuser
6. ./manage.py runserver



