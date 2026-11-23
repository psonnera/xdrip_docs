---
source_hash: 12ee29c8aa
source_commit: 7a18e7c
---
NightLite est un service d'abonné léger, compatible Nightscout. C'est une alternative plus simple à votre propre site Nightscout lorsque vous avez seulement besoin de partager votre glycémie avec des abonnés.

xDrip est le **principal** (il envoie vos données). L'[application iOS NightLite](https://apps.apple.com/us/app/nightlite/id6759909591) (un fork de Nightguard, par Richard Lander) est l'**abonné** et affiche vos données sur iPhone, iPad, Apple Watch ou Mac.

::: info Le saviez-vous ?
xDrip n'envoie que les 12 dernières heures de glycémies (avec tendance et delta) et de traitements, actualisées à chaque nouvelle valeur (environ toutes les 5 minutes).
:::

### Prérequis {#prerequisites}

- xDrip en version [nightly](../install/download#pre-release) récente (au minimum celle du [1er mars 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.03.01)).
- Une URL NightLite pour votre compte. Elle contient votre clé de sécurité et c'est la seule chose à saisir : xDrip génère à partir d'elle le QR code destiné à l'abonné.
- Pour l'abonné : un iPhone ou iPad (iOS 15+), une Apple Watch (watchOS 9.1+) ou un Mac (macOS 12 avec M1 ou plus récent) avec l'[application NightLite](https://apps.apple.com/us/app/nightlite/id6759909591).

::: warning Attention
NightLite ne peut pas être utilisé lorsque xDrip fonctionne en tant qu'[abonné Nightscout](../install/nightscoutfollower). Il ne fonctionne que si xDrip est votre source de données principale.
:::

### Configurer le principal (xDrip) {#setup-the-master-xdrip}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_cloud_upload_grey600_48dp.png" style="width:5%;" />&ensp;Chargement vers Cloud  
&ensp;&emsp;NightLite
:::

Saisissez votre URL NightLite :

::: xdripitem NightLite URL
&ensp;Typically entered by scanning QR code from dashboard (généralement saisie en scannant le QR code du tableau de bord)  
&ensp;This contains your security key - do not disclose it (contient votre clé de sécurité, ne la divulguez pas)
:::

Activez ensuite l'envoi :

::: xdripitem Upload to NightLite<span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Whether to upload to the remote service (envoyer ou non au service distant)
:::

::: warning Attention
L'URL NightLite contient votre clé de sécurité. Toute personne qui la possède peut accéder à vos données : ne la partagez pas.
:::

### Connecter un abonné {#connect-a-follower}

Une fois l'envoi activé, xDrip peut afficher un QR code qui contient toute votre configuration. C'est ce code que votre abonné scanne ; il n'y a rien à saisir sur l'appareil de l'abonné.

::: xdripitem Afficher le code QR
&ensp;Code-barres à scanner pour les abonnés afin de les configurer automatiquement
:::

1. Installez l'[application NightLite](https://apps.apple.com/us/app/nightlite/id6759909591) sur l'appareil de l'abonné.
2. Sur le téléphone principal, appuyez sur **Afficher le code QR**. xDrip affiche le QR code `NightLite configuration`.
3. Dans les préférences de l'application NightLite, appuyez sur l'icône de scan à côté du champ Nightscout URL et scannez le QR code sur l'écran du téléphone principal.

<img src="./images/M-S-NL4.png" style="zoom:33%;" />

::: info Remarque
Le service NightLite peut renvoyer des notifications à xDrip et peut arrêter l'envoi à distance si nécessaire.
:::

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
