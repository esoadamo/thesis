\[\[thesis\]\]

# Identity Managment for families

- \[\[Microsoft\]\]
- \[\[Google\]\]
- \[\[Synnology\]\]
- \[\[Cloudflare\]\]

## Other services

### Authelia

- https://www.authelia.com/
- open-source IdP
- alternative: https://www.keycloak.org/ 
  - has support for Kerberos, but overall difficult to configure

### Seznam

- ![](assets/2023-10-04-11-06-48-image.png)
- může ověřit účet pomocí bankovní identity
- používá vlastní 2FA aplikace, fallback na SMS
- [OpenID zrušeno 2015](https://www.cnews.cz/clanky/seznam-rusi-openid-lide-se-uz-naucili-pouzivat-jine-zpusoby-prihlasovani/)
- [Podporuje OAuth](https://vyvojari.seznam.cz/oauth)

### MojeID

- [hodně podporovaných služeb](https://www.mojeid.cz/cs/kde-pouzit/katalog-sluzeb/) - datová schránka, portál občana, Alza, knihovny, .... 
  - dovoluje nastavit jako [zdroj OIDC](https://www.mojeid.cz/dokumentace/html/ImplementacePodporyMojeid/OpenidConnect/index.html)
- může mít úroveň záruky "vysoká", "značná" atp.

### Nextcloud

- [Box - Nextcloud](https://nextcloud.com/box/)
- může být [OIDC provider](https://apps.nextcloud.com/apps/oidc)

### KeyCloak

- [website](https://www.keycloak.org/)

## Notes

- zmínit hardwarovou bezpečnost - řeší ji někdo? Používají šifrování? USB s PIN?
- krabicové offices - často už nemají updates -> nebezpečné
- [Study Reveals Average Person Has 100 Passwords | Tech.co](https://tech.co/password-managers/how-many-passwords-average-person)

### TODO

- synchronizace všeho po ukradení notebooku? 
  - prý umí Synnology
- tisky? WiFi?