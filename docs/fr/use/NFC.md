---
source_hash: 256676a54d
source_commit: 7a18e7c
---
Ce menu n'apparaît que si une [source de données matérielle Libre](../install/datasource#libre) est sélectionnée.

Si votre téléphone possède une **puce NFC compatible ISO 15693**, vous pouvez utiliser la fonction NFC de xDrip avec les Libre 1/14 jours/Pro et 2/2+ (EU).

Pensez à activer d'abord la fonction NFC dans les paramètres Android.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_nfc_grey600_48dp.png" style="width:5%;" />&ensp;Fonctionnalités de scan NFC
:::

::: xdripitem Utiliser la fonction NFC <span class='symbol'><img src="../images/ON.png" style="zoom:75%;" /></span>
&ensp;Permettre aux capteurs d'être scannés lorsque l'application est ouverte. Les données historiques seront récupérées. Très expérimental ! Méfiez-vous cela peut casser le capteur. Tester la compatibilité du téléphone avec un capteur presque expiré tout d'abord. Vous aurez été prévenu !
:::

Vous pouvez afficher l'âge du capteur en bas du graphique principal (xDrip principal).

::: xdripitem Âge du capteur ou date d'expiration <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
Afficher l'âge du capteur sur l'écran principal
:::

Pour que xDrip s'ouvre automatiquement lorsqu'un capteur NFC est détecté, vous devez **activer** Scan en dehors de xDrip+ (recommandé). Si plusieurs applications peuvent scanner des appareils NFC, il vous sera demandé de choisir celle à utiliser à chaque scan.

::: xdripitem Scan en dehors de xDrip+ <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Le scan NFC fonctionnera également à partir de l'écran du lanceur d'applications
:::

Vous pouvez choisir comment xDrip vous signale la fin du scan. La vibration et le son sont utiles pendant les scans NFC (longs) : vous devriez **activer** les deux.

Lors du scan, n'oubliez pas que vous devez maintenir le téléphone quelques secondes au niveau de l'antenne NFC pour que le scan se fasse correctement. Consultez la documentation du fabricant de votre téléphone pour savoir où elle se trouve.

::: xdripitem Vibrer pour indiquer le statut de scan <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

::: xdripitem Bipper lors du scan au sein de l'application xDrip+ <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>

Visible uniquement lorsque l'Engineering mode (Mode développeur) est activé.
:::

Le scan plus rapide est **activé** par défaut. Si vous avez des difficultés à scanner les capteurs, essayez de le désactiver.

::: xdripitem Utiliser la méthode de lecture multibloc plus rapide <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

Si vous avez des problèmes avec le NFC de votre téléphone, essayez d'**activer** la méthode toute balise.

::: xdripitem Utiliser la méthode de lecture optimisée pour toute balise <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
:::

## Démarrage de la connexion Bluetooth avec les capteurs Libre2 {#starting-bluetooth-connection-with-libre2-sensors}

Cette fonction permet à xDrip de prendre le contrôle de la connexion Bluetooth du capteur. Sur la plupart des téléphones, elle n'est pas compatible avec l'application du fabricant (une seule application peut se connecter à un même capteur). Certains utilisateurs signalent qu'il est possible de connecter à la fois l'application du fabricant et xDrip, mais ce n'est pas garanti : désinstallez l'application du fabricant si vous voulez que xDrip soit connecté au capteur.

::: xdripitem Démarrage de la connexion Bluetooth avec les capteurs Libre2
&ensp;Se connecter à des capteurs Freestyle Libre2 après les avoir scannés. Cela empêchera le lecteur Freestyle Libre et l'application LibreLink de recevoir les alertes
:::

Ce choix ne s'affiche lorsque vous scannez un nouveau capteur Libre 2 que si vous avez sélectionné Ask me every time (me demander à chaque fois).

Sachez que Toujours se connecter aux capteurs Libre2 déconnectera très probablement toute autre application ou appareil connecté au capteur. Si xDrip réussit l'appairage, l'autre appareil ou application ne pourra plus se reconnecter.

::: xdripitem Démarrage de la connexion Bluetooth avec les capteurs Libre2
&emsp;Toujours se connecter aux capteurs Libre2<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;Ask me every time<span style="float: right;">●&emsp;</span>  
&emsp;Ne jamais se connecter aux capteurs Libre2<span style="float: right;">○&emsp;</span>  
:::

## Lisser les données Libre 3 en utilisant la méthode xxx {#smooth-libre-3-data-when-using-xxx-method}

::: info Remarque
Le lissage s'applique à toute application de source de données externe utilisant la source de données `Libre2 (patched app)`.
:::

L'implémentation d'origine comprenait un algorithme de lissage sur 25 minutes pour supprimer le bruit et rendre plus sûre la boucle fermée DIY avec les capteurs Libre. Vous pouvez régler la période de lissage sur 10, 15 ou 25 minutes.

::: xdripitem Lisser les données Libre 3 en utilisant la méthode xxx
&ensp;Nombre de minutes à prendre en compte lors de l'utilisation des données de LibreX
:::

Le lissage ajoute un retard à la glycémie de xDrip par rapport aux données brutes. Ce retard est d'environ la moitié de la période de lissage. Réglez-le en fonction du comportement du capteur, pour votre sécurité. Si vous n'utilisez pas de système de boucle fermée DIY alimenté en glycémies par xDrip, réglez-le sur 10 minutes.

::: xdripitem Lisser les données Libre 3 en utilisant la méthode xxx
&emsp;10 minutes<span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&emsp;15 minutes<span style="float: right;">○&emsp;</span>  
&emsp;25 minutes ><span style="float: right;">●&emsp;</span>  
:::

<br>

[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
