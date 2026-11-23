---
source_hash: f83c7ecdbb
source_commit: 7a18e7c
---
<img src="../images/3dots_menu.png" style="zoom:75%;" />

### Rappels {#reminders}

Ce menu vous permet de configurer divers rappels : appuyez simplement sur le bouton + en bas à droite.

<img src="./images/3DM-Rem.png" style="zoom:75%;" />

Donnez-lui le nom de votre choix

<img src="./images/3DM-RemA.png" style="zoom:75%;" />

L'icône de note de musique `1` vous permet de choisir le son qui retentira lorsque le rappel se déclenchera.  
Vous pouvez programmer le rappel pour qu'il se déclenche après un délai défini à partir de maintenant, en choisissant `2` heures, jours ou semaines et la valeur numérique. Si vous cochez Répéter, il se répétera avec le même délai : par exemple, vous pouvez le régler pour qu'il sonne toutes les 2 semaines.  
Vous pouvez le régler pour qu'il ne se déclenche qu'en semaine, que le week-end, ou les deux `3`.  
Si vous sélectionnez En alternance, il affichera des messages différents `4` que vous pouvez intervertir avec l'icône à double flèche.  
Le rappel peut être annoncé à voix haute lorsqu'il se déclenche.  
Si vous sélectionnez Carillon seulement, le rappel n'aura pas besoin d'être confirmé : il ne sonnera qu'une fois. Sans cette option, il sonnera de façon répétée jusqu'à ce qu'il soit ignoré.  
À la maison seulement fait que le rappel ne se déclenche que lorsque le téléphone est connecté au Wi-Fi de votre domicile ; voir plus bas comment le configurer.

Cocher ou décocher les cases affiche des indications sur leur fonction réelle.

Une fois le rappel configuré, vous pouvez modifier son titre en appuyant dessus.

Vous pouvez le modifier par un appui long.

Balayer un rappel vers la gauche le met en veille pour 30 minutes (par défaut) ; vous pouvez changer ce délai avec le bouton en dessous.

<img src="./images/3DM-RemS.png" style="zoom:75%;" />

Balayer un rappel vers la droite vous permet soit `1` de le mettre en veille pour la durée sélectionnée en dessous (de 15 minutes à 1 semaine), soit `3` de le supprimer. Si vous changez d'avis, vous pouvez annuler les modifications `2`.

<img src="./images/3DM-RemA1.png" style="zoom:75%;" />

Un autre menu à 3 points est disponible en haut à droite.

<img src="./images/3DM-RemM.png" style="zoom:75%;" />

Vous pouvez définir votre réseau domestique avec Définir le réseau domestique ; il est utilisé lorsque le rappel est réglé sur À la maison seulement.  
Vous pouvez désactiver les rappels pendant la nuit ; vous pouvez aussi désactiver toutes les alertes, auquel cas la case suivante vous permet de les réactiver (réactiver tous les rappels) le lendemain matin.

### Messages d'urgence {#emergency-messages}

xDrip peut envoyer automatiquement des SMS dans certaines situations pour alerter d'autres personnes. Cela nécessite évidemment une couverture réseau et une carte SIM active. La localisation du téléphone doit être autorisée pour que xDrip puisse utiliser cette fonction.

<img src="./images/3DM-EM.png" style="zoom:75%;" />

Pour la configurer, vous devez d'abord ajouter un contact, éventuellement lui donner un nom, et enfin choisir quelles situations d'urgence déclencheront l'envoi du SMS.

<img src="./images/3DM-EM1.png" style="zoom:75%;" />

Vous pouvez ensuite envoyer un message de test pour vérifier le bon fonctionnement du système d'urgence.

<img src="./images/3DM-EM2.png" style="zoom:75%;" />

### Fonctions d'import/export {#import-export-features}

Ce menu propose diverses options pour importer (uniquement la base de données xDrip complète) ou exporter des données.

<img src="../images/3DM-IE.png" style="zoom:75%;" />

Voir [ici](../troubleshoot/reinstall#backup) pour l'import/export de la base de données et des paramètres.

Vous pouvez exporter les données depuis une date donnée jusqu'à maintenant, au format SiDiary. Le fichier est enregistré dans `/storage/emulated/0/xDrip` sous forme de fichier zip contenant la liste des données au format CSV (valeurs séparées par des virgules).

<img src="./images/3DM-IE-SiDiary.png" style="zoom:75%;" />

### Traduction crowdsourcing {#crowd-sources-translation}

La traduction de xDrip repose sur des bénévoles, via [Crowdin](https://crowdin.com/project/xdrip).  
Vous êtes les bienvenus pour y contribuer : contactez les responsables en bas de la page.

<img src="./images/3DM-CIT.png" style="zoom:75%;" />

### Journal d'événements {#events-log}

Le journal d'événements donne de nombreuses indications sur ce que fait xDrip ; vous pouvez ajouter des traces supplémentaires en ajoutant des [tags](./lesscommon#extra-logging-settings).

<img src="./images/3DM-EL.png" style="zoom:75%;" />

Vous pouvez aussi filtrer les éléments affichés en sélectionnant le journal ou les événements souhaités avec les cases à cocher au-dessus de la liste.  
Lorsque vous partagez des captures d'écran du journal d'erreurs, veillez à tout activer et à masquer manuellement les informations personnelles (identifiants, numéros de série, ...)

`High` affiche les erreurs

<img src="./images/3DM-EL1.png" style="zoom:75%;" />

`Mid` affiche les traces

<img src="./images/3DM-EL2.png" style="zoom:75%;" /> 

`Low` affiche tout le reste (importance moindre)

`EH` affiche les événements de plus grande importance

<img src="./images/3DM-EL3.png" style="zoom:75%;" /> 

`EL` affiche les événements de moindre importance.

<img src="./images/3DM-EL4.png" style="zoom:75%;" /> 

### Tendance Libre {#libre-trend}

Si vous utilisez un capteur Libre, Afficher la tendance du Freestyle Libre affiche les 45 dernières minutes d'informations du capteur, minute par minute.

<img src="./images/3DM-LT.png" style="zoom:75%;" /> 

### Partager les paramètres via le code QR {#share-settings-via-qr-code}

C'est un raccourci vers Menu / Paramètres / [Affichage QR codes](./copysettings) 

### Vérifier les mises à jour {#check-for-updated-version}

Cette entrée lance une vérification de version selon les réglages de Menu / Paramètres / [xDrip+ Mises à jour](./update)  
Si une nouvelle version est disponible, l'écran de téléchargement s'ouvre.

<img src="./images/3DM-CU.png" style="zoom:75%;" /> 

### Envoyer des messages au développeur {#send-feedback-to-developers}

N'utilisez cette fonction que pour envoyer des compliments.

Pour toute autre demande, préférez les [discussions GitHub de xDrip](https://github.com/NightscoutFoundation/xDrip/discussions) ou [Facebook](https://www.facebook.com/groups/xDripG5).

<br>

[*Dernière modification le 15/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
