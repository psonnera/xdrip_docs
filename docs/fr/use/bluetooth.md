---
source_hash: c7d2a497a5
source_commit: 7a18e7c
---
La multitude de fabricants de téléphones Android et les particularités des capteurs et transmetteurs font de la fiabilité de la connexion Bluetooth une difficulté majeure pour xDrip. Ce menu contient de nombreux réglages avancés qui ne peuvent pas être standardisés pour tous les systèmes.

::: info Configurez les paramètres Bluetooth comme indiqué ci-dessous
:::

Une approche par essais successifs est recommandée, mais ne modifiez qu'un paramètre à la fois pour éviter d'ajouter de la confusion.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;Paramètres moins courants  
&ensp;&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_bluetooth_settings_grey600_48dp.png" style="width:5%;" />&ensp;Paramètres Bluetooth
:::

#### Activer le Bluetooth {#turn-bluetooth-on}

Cette option fait que xDrip essaie d'activer le Bluetooth.

Si xDrip se connecte à un appareil Bluetooth, Activer le Bluetooth est indispensable.  
xDrip peut ne pas réussir à passer outre complètement les réglages de votre téléphone : si vous désactivez le Bluetooth dans les paramètres Android ou mettez votre téléphone en mode avion, il risque de ne pas pouvoir le réactiver. Le Bluetooth doit être activé dans les paramètres Android si vous voulez que xDrip l'utilise.  

*Collecteur : gestion Bluetooth globale (transmetteur classique + OB1 Dex) — Dexcom G5/G6/G7, transmetteurs G4/Libre*

::: xdripitem Activer le Bluetooth<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Activer automatiquement bluetooth s'il est éteint lorsqu'on tente de se connecter à un périphérique bluetooth 
:::

#### Garde-fou Bluetooth {#bluetooth-watchdog}

En cas de données manquantes à cause d'une perte de connexion Bluetooth, vous pouvez faire en sorte que xDrip désactive puis réactive le Bluetooth de votre téléphone ; le délai par défaut est de 20 minutes sans données. Vous pouvez personnaliser cette valeur.

Si vous voyez le message indiquant que **xDrip a désactivé le Bluetooth**, c'est probablement parce que le garde-fou s'est déclenché et que xDrip essaie de rétablir la connexion avec le capteur.

*Collecteur : logique de récupération globale (collecteurs classiques + séquenceur) — collecteurs Dexcom et à transmetteur*

::: xdripitem Garde-fou Bluetooth<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Réinitialiser Bluetooth en le désactivant puis réactivant si nous n’obtenons rien pendant 20 minutes
:::

::: info Remarque
Attention : le déclenchement du garde-fou Bluetooth et du garde-fou Bluetooth G5 entraîne une déconnexion Bluetooth temporaire de tous les appareils connectés. Vous voudrez peut-être désactiver cette fonction si vous utilisez AAPS et que votre transmetteur ou votre pompe ne rétablit pas automatiquement la connexion Bluetooth.  
Notez que le garde-fou Bluetooth G6/G7/1/1+ n'est pas contrôlé par ce paramètre
:::

#### Chien de garde Bluetooth Dex {#dex-bluetooth-watchdog}

Pour les capteurs G5, vous pouvez faire en sorte que xDrip désactive et réactive systématiquement le Bluetooth. Laissez cette option activée si vous avez des problèmes de connexion.

*Collecteur : chemins du collecteur OB1 Dex — Dexcom G5/G6/G7*

::: xdripitem Chien de garde Bluetooth Dex<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Réinitialiser Bluetooth en le désactivant et reactivant pour continuer de faire marcher la source de données. Sans cela, le collecteur peut échouer.
:::

#### Fermer GATT sur déconnexion BLE {#close-gatt-on-ble-disconnect}

Lorsque cette option est activée, xDrip effectue une déconnexion complète puis une reconnexion de votre appareil Bluetooth (fermeture du lien, découverte et connexion) en cas de perte de connexion. Comme cela peut être inefficace, il est recommandé de la laisser **désactivée** : l'appareil reste alors en mémoire et xDrip essaie seulement de s'y reconnecter en tant qu'appareil BLE connu.

*Collecteur : collecteur de transmetteur classique (`DexCollectionService`) — transmetteurs G4/Libre, BlueReader/Atom/Tomato*

::: xdripitem Fermer GATT sur déconnexion BLE<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Si le garde-fou Bluetooth s'active souvent alors vous pouvez essayer de décocher cette option pour voir si ça aide
:::

#### Utiliser le scan {#use-scanning}

Utiliser le scan effectue l'équivalent de Scan Bluetooth du menu principal pour tenter de rétablir une connexion perdue. Ce n'est pas toujours efficace avec les téléphones récents. Laissez-la d'abord **désactivée**, sauf si elle s'avère utile.

*Collecteur : collecteur de transmetteur classique (`DexCollectionService`) — transmetteurs G4/Libre, BluKon*

::: xdripitem Utiliser le scan<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Scanner avant de se connecter sur xBridge et Bluetooth Libre
:::

#### Use BLE manager {#use-ble-manager}

Utilise un système de gestion BLE plus moderne. Laissez-la **désactivée**, sauf si vous dépannez un problème de connexion et qu'on vous a conseillé de l'essayer.

*Collecteur : collecteur de transmetteur classique (`DexCollectionService`) — appareils à transmetteur*

::: xdripitem Use BLE manager<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use a more modern BLE manager system (utiliser un système de gestion BLE plus moderne)
:::

#### Faire confiance à Auto-Connect {#trust-auto-connect}

Faire confiance à Auto-Connect dépend vraiment de votre téléphone. Cette option est **activée** par défaut. Si vous avez un Samsung, Xiaomi, OnePlus, Oppo, Huawei ou Realme, vous devriez probablement la désactiver. Si vous perdez souvent la connexion sans parvenir à la rétablir, essayez de la désactiver.

*Collecteur : collecteur de transmetteur classique + collecteur OB1 Dex — Dexcom G5/G6/G7, appareils à transmetteur*

::: xdripitem Faire confiance à Auto-Connect<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utiliser et faire confiance à la fonctionnalité de connexion auto Bluetooth d'Android
:::

#### Utiliser les scans en arrière-plan {#use-background-scan}

Utiliser les scans en arrière-plan est une fonction des versions récentes d'Android, **activée** par défaut. Si vous perdez régulièrement la connexion, essayez de la désactiver.

*Collecteur : collecteurs à séquenceur/scan en arrière-plan (Android O+) — principalement collecteurs Dexcom/BLE*

::: xdripitem Utiliser les scans en arrière-plan<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Utiliser la fonction de scan en arrière-plan d'Android 8+
:::

#### Companion Bluetooth {#companion-bluetooth}

Companion Bluetooth permet à l'application de fonctionner en même temps que l'application Dex principale connectée au capteur.

*Collecteur : écouteur compagnon BlueTails — émetteurs Dexcom en configuration compagnon/sniffer*

::: xdripitem Companion Bluetooth<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use Bluetooth with Companion app data source (utiliser le Bluetooth avec la source de données application compagnon)
:::

#### Wakelocks Bluetooth {#bluetooth-wakelocks}

Les wakelocks Bluetooth ne sont pas recommandés et doivent rester **désactivés**.

*Collecteur : collecteur classique + chemins de callback BLE — principalement collecteurs à transmetteur*

::: xdripitem Wakelocks Bluetooth<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Anciens wakelocks Bluetooth qui peuvent drainer la batterie un peu plus, mais pourraient être nécessaire pour la réception bluetooth  
:::

#### Mode de sondage xBridge+ {#xbridge-polling-mode}

Le mode de sondage xBridge+ permet à xDrip d'envoyer des requêtes au transmetteur. Même s'il n'a aucun effet avec les autres appareils Bluetooth, vous pouvez l'activer si vous perdez souvent la connexion, car il occupera de toute façon le Bluetooth de votre téléphone à essayer de se connecter.

*Collecteur : collecteur de transmetteur classique (`DexCollectionService`) — xBridge et matériels similaires*

::: xdripitem Mode de sondage xBridge+<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Support expérimental pour la fonction de sondage xBridge+
:::

#### Toujours découvrir les services {#always-discover-services}

Activé par défaut. Visible uniquement lorsque l'Engineering mode (Mode développeur) est activé.

*Collecteur : collecteur de transmetteur classique (`DexCollectionService`) — appareils BLE à transmetteur*

::: xdripitem Toujours découvrir les services<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Sonder les services Bluetooth à chaque connexion
:::

#### Use GATT refresh {#use-gatt-refresh}

Indique s'il faut utiliser le mécanisme bas niveau de rafraîchissement GATT. Activé par défaut. Visible uniquement lorsque l'Engineering mode (Mode développeur) est activé.

*Collecteur : collecteur OB1 Dex, collecteurs de type JamBase — Dexcom G5/G6/G7, Medtrum*

::: xdripitem Use GATT refresh<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Whether to use the low level gatt refresh mechanism (utiliser ou non le mécanisme bas niveau de rafraîchissement GATT)
:::

#### Permettre la dissociation du BluCon {#allow-blucon-unbonding}

Permettre la dissociation du BluCon n'est utile que si vous utilisez un transmetteur BluCon, car les autres ne s'associent pas à votre téléphone. Si ce transmetteur vous demande souvent l'association, désactivez cette option.

*Collecteur : chemin des transmetteurs BluKon/Libre — BluKon et configurations de transmetteurs Libre apparentées*

::: xdripitem Permettre la dissociation du BluCon<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Disponible uniquement pour les téléphones qui supportent l'association automatique
:::

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
