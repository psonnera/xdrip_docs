---
source_hash: 2ef67c25aa
source_commit: 8f65827
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Paramètres  
&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_add_alert_grey600_48dp.png" style="width:5%;" />&ensp;Alarmes et alertes
:::

xDrip permet de configurer de nombreuses alertes.

Si xDrip est votre seule application de suivi de la glycémie, il est recommandé d'activer au moins trois alertes :

- Alerte Basse
- Alerte Haute
- Alerte de lecture manquée

### Liste des alertes de niveau de glycémie {#glucose-level-alerts-list}

::: xdripitem Liste des alertes de niveau de glycémie
:::

Par défaut, une alerte Basse et une alerte Haute sont définies.

Les alertes Basses se déclenchent lorsque la glycémie est inférieure ou égale à la valeur de l'alerte, les alertes Hautes lorsqu'elle est supérieure ou égale.

Pour créer une nouvelle alerte, appuyez sur la barre de titre `CRÉER ALERTE BASSE` ou `CRÉER ALERTE HAUTE`.

Pour modifier une alerte existante, faites un appui long sur l'alerte

::: xdrip ☰&emsp;Liste d'alertes
<div style="background-color: gray; color: white; text-align: center;">  &emsp;CRÉER ALERTE BASSE&emsp;</div> 

 <small>&emsp;&emsp;Alerte Basse&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;70&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;toute la journée</small>  
<small>Ignorer le mode silencieux&emsp;&emsp;&emsp;Sonnerie par défaut (sonnerie inconnue)</small>  

<div style="background-color: gray; color: white; text-align: center;">  &emsp;CRÉER ALERTE HAUTE&emsp;</div>  
<small>&emsp;&emsp;Alerte Haute&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;224&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;toute la journée</small>  
<small>Ignorer le mode silencieux&emsp;&emsp;&emsp;Sonnerie par défaut (sonnerie inconnue)</small>  
:::

1. Vous pouvez donner à une alerte le nom de votre choix, tant qu'aucune autre alerte ne porte le même nom
2. Le seuil est la glycémie qui déclenche l'alarme ; une seule alarme peut utiliser cette valeur
3. La mise en veille par défaut est la durée proposée lorsque vous mettez l'alerte en veille
4. L'alarme se déclenche de nouveau toutes les x minutes si elle n'est pas confirmée

::: xdrip ☰&emsp;Modifier l'alerte
&emsp;&emsp;&emsp;Modification Alerte Basse  


&emsp;&emsp;<small>Nom de l'alerte: <u>Alerte Basse</u></small>&emsp;<span style="background-color: green; color: white; text-align: center;">1</span>  
&emsp;&emsp;<small>Seuil: <u>70</u></small>&emsp;<span style="background-color: green; color: white; text-align: center;">2</span>  
&emsp;&emsp;<small>Mise en veille par défaut: <u>35</u></small>&emsp;<span style="background-color: green; color: white; text-align: center;">3</span>  
&emsp;&emsp;<small>Rappeler toutes les x minutes: <u>1</u></small>&emsp;<span style="background-color: green; color: white; text-align: center;">4</span>  
&emsp;&emsp;<small>si non confirmé</small>  

&emsp;&emsp;<small>Son d'alerte: <u>Sonnerie par défaut (sonnerie inconnue)</u></small>&emsp;<span style="background-color: green; color: white; text-align: center;">5</span>  
:::

&emsp;5. Vous pouvez personnaliser le son de l'alerte : appuyez sur CHOISIR LE FICHIER pour sélectionner la sonnerie de cette alarme.

- Son/Alarme Système vous permet de choisir parmi les sonneries de votre téléphone.

- Son/Alarme personnalisés vous permet de choisir votre propre son ou musique.

- Son xDrip par défaut utilise le son par défaut de l'application.

::: xdripitem Quel type de son ?
&emsp;Son/Alarme Système  
&emsp;Son/Alarme personnalisés  
&emsp;Son xDrip par défaut
:::

Par défaut, l'alarme est active toute la journée.

::: xdripitem <small>Sélectionner la période de l'alerte</small>
&emsp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;✅&ensp;toute la journée
:::

Si vous décochez la case, vous pouvez définir les heures d'activité.  
Appuyez sur l'heure de début et l'heure de fin pour définir la plage horaire pendant laquelle l'alarme est active.

::: xdripitem <small>Sélectionner la période de l'alerte</small>
&emsp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;☐&ensp;toute la journée  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;0:00&emsp;-&emsp;0:00  
:::
Vous pouvez désactiver l'alarme (décocher) lorsque le téléphone est en mode silencieux (désactivation déconseillée)

::: xdripitem <small>Remplacer le mode silencieux du téléphone</small><span class='symbol'><small>✅</small></span>
:::

Forcer par haut-parleur fait sonner l'alarme sur le téléphone même si vous utilisez d'autres haut-parleurs (Bluetooth par exemple)

::: xdripitem <small>Forcer par haut-parleur</small><span class='symbol'><small>✅</small></span>
:::

Vibrer en cas d'alerte active le vibreur du téléphone

::: xdripitem <small>Vibrer en cas d'alerte</small><span class='symbol'><small>✅</small></span>
:::

Désactiver l'alerte la désactive complètement : elle apparaît barrée dans la Liste d'alertes

::: xdripitem <small>Désactiver l'alerte</small><span class='symbol'><small>☐</small></span>
:::

<span style="background-color: gray; color: white;">&ensp;ALERTE DE TEST&ensp;</span> fait sonner cette alerte

<span style="background-color: gray; color: white;">&ensp;SAUVER L'ALERTE&ensp;</span> enregistre cette alerte nouvelle ou modifiée

<span style="background-color: gray; color: white;">&ensp;SUPPRIMER L'ALERTE&ensp;</span> supprime cette alerte

<span style="background-color: gray; color: white;">&ensp;ARRÊTER L'ALERTE AVANT QU'ELLE NE DÉCLENCHE&ensp;</span> vous permet d'empêcher l'alerte de se déclencher : par exemple, si vous avez déjà traité une hypo ou une hyper prévue et savez que la glycémie va évoluer de toute façon, vous pouvez éviter d'entendre l'alarme pendant la durée de votre choix.

### Paramètres d'alertes glycémiques {#glucose-alerts-settings}

::: xdripitem Paramètres d'alertes glycémiques
:::

##### Profil de volume d'alerte {#alert-volume-profile}

Vous pouvez personnaliser le volume de vos alertes

::: xdripitem Profil de volume d'alerte
&ensp;Haute <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Moyenne <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Montante <span style="float: right;">●&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Vibreur uniquement <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Silencieux <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;
:::

Le volume Montante est recommandé si vous ne voulez pas que l'alarme retentisse immédiatement à plein volume (utile la nuit). Vous pouvez aussi [retarder](#delay-ascending-volume) le volume ascendant pour filtrer les valeurs bruitées, et limiter le volume maximum.

Depuis le [16 oct. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.10.16), choisir Vibreur uniquement ou Silencieux demande une confirmation : avec ces profils, les alertes ne font aucun son, même celles pour lesquelles Ignorer le mode silencieux est activé. Le profil n'est modifié que si vous confirmez.

##### Priorité audio {#audio-focus}

La priorité audio vous permet de décider comment gérer les autres sons lorsqu'une alarme ou une alerte xDrip se déclenche.

::: xdripitem Priorité audio
Choisir ce qu'il faut faire avec les autres applications lors de lecture d'alertes et réglage du volume du système  
:::

Vous pouvez baisser automatiquement le volume, mettre en pause les autres applications qui jouent des sons (comme les lecteurs multimédias) ou mettre en pause tous les autres sons pour mieux entendre le son de xDrip.

::: xdripitem Priorité audio
&ensp;Ne pas ajuster les sons des autres applications <span style="float: right;">●&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Réduire le volume des autres applications <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Mettre en pause les autres applications en cours de lecture audio <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp;  
&ensp;Mettre en pause tous les autres sons <span style="float: right;">○&emsp;</span>&emsp;&emsp;&emsp; 
:::

##### Mise en veille intelligente {#smart-snoozing}

##### Alertes intelligentes {#smart-alerting}

La mise en veille intelligente et les alertes intelligentes évitent que l'alerte se déclenche ou se relance si la glycémie évolue dans la bonne direction (vers le haut pour les alertes Basses, vers le bas pour les alertes Hautes). Les seuils pour considérer une évolution suffisante dans la bonne direction sont :

- Variation supérieure à +4 mg/dl en 5 minutes pour une alerte Basse  
- Variation supérieure à -1 mg/dl en 5 minutes pour une alerte Haute

::: xdripitem Mise en veille intelligente <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Rester inactif si la glycémie évolue dans la bonne direction
:::

::: xdripitem Alertes intelligentes <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Ne pas alerter si la glycémie évolue dans la bonne direction
:::

##### Ne pas alerter pendant les appels téléphoniques {#dont-alarm-during-phone-calls}

Les alarmes ne sonnent pas si elles se déclenchent pendant un appel téléphonique.

::: xdripitem Ne pas alerter pendant les appels téléphoniques <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Alarmes silencieuses pendant les appels téléphoniques
:::

##### La pression des boutons met en veille les alarmes {#buttons-silence-alarms}

Cette option permet de mettre rapidement une alarme en veille en appuyant simplement sur le bouton de volume haut ou bas.

::: xdripitem La pression des boutons met en veille les alarmes <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Appuyer sur le volume up ou down mettra en veille une alarme active lorsque l'application est lancée
:::

##### Boutons d'alerte {#alert-buttons}

Boutons d'alerte ajoute un bouton d'action dans la notification déroulante de l'alerte.

::: xdripitem Boutons d'alerte <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Afficher les boutons d'action (comme Snooze) dans les notifications d'alerte
:::

<img src="./images/M-S-AA-GAm2.png" style="zoom:75%;" />

<img src="./images/M-S-AA-GAm3.png" style="zoom:75%;" />

##### Démarrer silencieusement {#start-snoozed}

Démarrer silencieusement applique le délai de mise en veille avant de déclencher l'alarme. Vérifiez que la `Mise en veille par défaut` de l'alarme est adaptée.

::: xdripitem Démarrer silencieusement <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Les alertes commencent silencieuses et doivent persister pendant un certain temps pour se déclencher
:::

##### Allumer l'écran {#wake-screen}

Allume l'écran pendant les alertes.

::: xdripitem Allumer l'écran<img src="../images/OFF.png" style="zoom:75%;" />
&ensp;Allumer l'écran pendant les alertes. Peut déverrouiller les appareils qui n'ont pas de verrouillage d'écran activé.
:::

##### Utiliser la lumière de la caméra {#use-camera-light}

Fait clignoter le flash de l'appareil photo arrière pendant les alertes (lorsque le téléphone est en charge).

::: xdripitem Utiliser la lumière de la caméra<img src="../images/OFF.png" style="zoom:75%;" />
&ensp;Allumer la lumière de la caméra lors des alertes si connecté à un chargeur
:::

##### Raccourci vers les alertes de niveau de glycémies {#shortcut-to-bg-level-alerts}

Vous pouvez ajouter un raccourci vers `Alertes de niveau` dans le menu principal de xDrip.

::: xdripitem Raccourci vers les alertes de niveau de glycémies<img src="../images/DIS.png" style="zoom:75%;" />
&ensp;Créer un raccourci sur la navigation principale vers l'écran de niveau de glycémies
:::

##### Suppression des alertes en cas de lectures manquées {#suppress-alerts-if-missed-readings}

::: xdripitem Suppression des alertes en cas de lectures manquées
:::

Les alertes de niveau restent actives même en l'absence de signal (changement de capteur par exemple, ou abonné sans réseau). Cette option permet de les supprimer. Si vous l'utilisez, vérifiez qu'une alerte de lecture manquée est activée.

::: xdripitem Suppression des alertes en cas de lectures manquées <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Supprime les alertes de mise en veille et actives après la période prédéfinie de lectures manquées
:::

Vous pouvez définir le nombre de minutes au bout duquel les alertes doivent s'arrêter.

::: xdripitem Supprimer les alertes de mise en veille et actives après .. minutes (minimum 10)
&ensp;Supprime les alertes de mise en veille et actives après la période prédéfinie de lectures manquées
:::

##### Canaux de Notification {#notification-channels}

Android 8.0 étant désormais la version minimale prise en charge, xDrip utilise toujours les canaux de notification Android pour vos alertes. Le paramètre qui les activait a été supprimé lors de l'abandon d'Android 7 ([12 juil. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)) : les canaux sont maintenant toujours actifs.

Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), xDrip ne crée plus que quatre canaux et joue lui-même le son et la vibration des alertes, au lieu de passer par le canal. Les anciens canaux sont supprimés automatiquement.

::: xdripitem Canaux de notification xDrip
&ensp;Alertes de niveau de glucose  
&ensp;Autres alertes  
&ensp;Général  
&ensp;Notification en cours
:::

Les réglages des canaux dans Paramètres Android / Notifications / Applications / xDrip décident seulement si la notification est affichée. Le son et la vibration dépendent des paramètres de xDrip : le [profil de volume d'alerte](#alert-volume-profile), et les options Ignorer le mode silencieux et Vibrer en cas d'alerte de chaque alerte. Désactiver un canal masque la notification mais ne rend pas l'alerte silencieuse : désactivez plutôt l'alerte dans xDrip.

##### Priorité des alertes {#alert-priority}

Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), lorsque deux alertes se chevauchent, la plus importante l'emporte : elle interrompt le son et la vibration d'une alerte moins importante déjà en cours, et une alerte moins importante ne peut pas interrompre une alerte plus importante qui sonne encore. Cela ne concerne que le son et la vibration, pas la mise en veille ni la fermeture. De la priorité la plus haute à la plus basse :

1. Lectures manquées
2. Niveau de glycémie bas
3. Haute persistante
4. Niveau de glycémie haut
5. Prévision d'hypoglycémie
6. Glycémie en chute ou en augmentation rapide
7. Expiration du capteur
8. Alarme BlueReader
9. Alertes de valeurs incorrectes (bruit)
10. Rappels
11. Redémarrage de session OB1
12. Autres notifications

Depuis le [9 oct. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.10.09), lorsque le téléphone est en mode silencieux (ou que le [profil de volume d'alerte](#alert-volume-profile) Silencieux est sélectionné) et qu'Ignorer le mode silencieux est désactivé, les alertes jusqu'à Glycémie en chute ou en augmentation rapide inscrivent quand même dans le journal qu'aucun son n'a été joué : vous pouvez ainsi voir après coup qu'une alerte s'est déclenchée.

##### Réglages du volume croissant {#ascending-volume-settings}

::: xdripitem Réglages du volume croissant
:::

##### Délai du volume ascendant {#delay-ascending-volume}

Vous pouvez retarder le démarrage du son de l'alerte à volume ascendant sans retarder la vibration, qui démarre dès le déclenchement de l'alerte.

::: xdripitem Délai du volume ascendant<img src="../images/EN.png" style="zoom:75%;" />
&ensp;Pour le profil de volume ascendant, retarder le démarrage du son d'alerte de 3 minutes. Le vibreur (si activé) démarre dès que l'alerte se déclenche, quel que soit ce paramètre.
:::

##### Augmentation vers le milieu {#ascend-to-medium}

Vous pouvez limiter le volume maximum des alertes et alarmes à volume ascendant au volume moyen au lieu du maximum.

::: xdripitem Augmentation vers le milieu<img src="../images/DIS.png" style="zoom:75%;" />
&ensp;Lorsqu'il est activé, le profil de volume ascendant augmentera vers le volume moyen au lieu du maximum
:::

### Alertes de calibration {#calibration-alerts}

Si votre capteur nécessite un étalonnage régulier, vous pouvez configurer xDrip pour qu'il vous avertisse lorsqu'un étalonnage est nécessaire.

Vous pouvez définir l'intervalle entre les étalonnages, le son à jouer, etc.

::: xdrip Alertes de calibration
:::

::: xdripitem Alertes de calibration<img src="../images/OFF.png" style="zoom:75%;" />
&ensp;Alerte lorsqu'une calibration est demandée
:::

::: xdripitem Heures entre les calibrations
&ensp;Combien d'heures entre les demandes de calibration
:::

::: xdripitem Son de demande de calibration
&ensp;Par défaut
:::

::: xdripitem Ignorer le mode silencieux<img src="../images/END.png" style="zoom:75%;" />
:::

::: xdripitem Même lors de la charge<img src="../images/END.png" style="zoom:75%;" />
&ensp;Décocher la case pour ne pas demander de calibrations lorsque le téléphone est en charge
:::

::: xdripitem Répéter les alertes<img src="../images/END.png" style="zoom:75%;" />
&ensp;Continuer d'alerter si aucune calibration n'est réalisée
:::

::: xdripitem Minutes entre les répétition d'alertes
&ensp;20
:::

##### Alerte initiale {#initial-alert}

L'alerte de calibration initiale sert au démarrage d'un capteur qui nécessite un étalonnage initial : elle se déclenche lorsque suffisamment de bonnes valeurs sont disponibles pour étalonner.

::: xdripitem Alerte initiale<img src="../images/ON.png" style="zoom:75%;" />
&ensp;Émettre un son lorsque la calibration initiale est demandée
:::

### Alerte lecture manquée {#missed-reading-alert}

::: xdripitem Alerte lecture manquée
:::

Si vous comptez sur xDrip pour vous alerter des hypos et des hypers, il est essentiel de vous assurer qu'il reçoit bien les valeurs de glycémie. Pour votre sécurité, si vous n'avez pas d'autre alarme, activez cette fonction.

La configuration est semblable à celle des [alertes de niveau de glycémie](#glucose-level-alerts-list). **Le son de l'alarme doit être défini dans Autres alertes** (voir [plus bas](#alert-preferences)).  Pour la tester, mettez votre téléphone en mode avion jusqu'à ce qu'elle se déclenche.

::: xdrip ☰&emsp;Configurer les lectures manqués
&emsp;<small>✅ Activer l'alerte de lecture manquée</small>  
&emsp;<small>Alerte si aucune donnée reçue dans:</small>  
&emsp;<small><u>&ensp;30&ensp;</u>&ensp;minutes</small>  
&emsp;<small>Sélectionner la période de l'alerte:</small>  
&emsp;<small>✅ toute la journée</small>  

&emsp;<small>Nombre de minutes avant de déclencher la même alerte après sa mise en veille:</small>  
&emsp;<small><u>&ensp;20&ensp;</u>&ensp;minutes</small>  
&emsp;<small>☐ Relancer les alertes avant la durée de mise en veille</small>  
&emsp;<small>Délai de relance de l'alerte:</small>  
&emsp;<small><u>&ensp;60&ensp;</u>&ensp;secondes</small>  
&emsp;<small>☐ Ignorer le mode silencieux</small>  
:::

### Autres alertes {#other-alerts}

::: xdrip Autres alertes
:::

#### Lectures de bruits {#noisy-readings}

::: xdripitem <small>LECTURES DE BRUITS</small>
:::

Si vous activez cette fonction et que votre capteur la prend en charge, vous pouvez configurer une alerte pour les valeurs bruitées.

::: xdripitem Alertes de valeurs incorrectes (bruit)<img src="../images/DIS.png" style="zoom:75%;" />
:::

::: xdripitem Alerte après x minutes de valeurs de bruit
&ensp;90
:::

::: xdripitem Mise en veille d'alerte
&ensp;Nombre de minutes avant de déclencher la même alerte après sa mise en veille.
:::

::: xdripitem Relancer les alertes avant la durée de mise en veille<img src="../images/DIS.png" style="zoom:75%;">
&ensp;Relancer l'alerte si non mise en veille plus tôt
:::

::: xdripitem Temps de relance de l'alerte
&ensp;Nombre de SECONDES à attendre avant de relancer la même alerte.
:::

#### Chute ou hausse de la glycémie {#falling-or-rising-bg}

::: xdripitem <small>CHUTE/HAUSSE DE LA GLYCÉMIE</small>
:::

Vous pouvez aussi configurer des alertes pour les variations rapides de glycémie et définir la variation par minute qui les déclenche. Par exemple, 3 par minute correspond à 15 mg/dl (0,85 mmol/l) toutes les 5 minutes.

::: xdripitem Glycémie en chute rapide<img src="../images/DIS.png" style="zoom:75%;">
:::

::: xdripitem seuil de chute
&ensp;3 mg/dl/min (0.17 mmol/l/min)
:::

::: xdripitem Glycémie en augmentation rapide<img src="../images/DIS.png" style="zoom:75%;">
:::

::: xdripitem seuil d'augmentation 
&ensp;3 mg/dl/min (0.17 mmol/l/min)
:::

##### Préférences d'alerte {#alert-preferences}

::: xdripitem <small>PRÉFÉRENCES D'ALERTE (POUR CES ALERTES)</small>
:::

Les alertes ci-dessus, **ainsi que Lectures manquées**, utilisent le son et la vibration définis ci-dessous.  
Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), xDrip les joue lui-même : les [canaux de notification](#notification-channels) ne contrôlent plus le son ni la vibration. Les [profils de volume d'alerte](#alert-volume-profile) Vibreur uniquement et Silencieux s'appliquent aussi à ces alertes. Lorsque le téléphone est en mode vibreur, seule la vibration est jouée ; en mode silencieux, rien n'est joué sauf si Substituer le mode silencieux pour ces alertes est activé.

::: warning Testez l'alarme
C'est une fonction importante pour dormir en sécurité. Réduisez la durée des lectures manquées et mettez votre téléphone en mode avion (sans Wi-Fi) pour forcer l'alarme à sonner.
:::

::: xdripitem Son d'alerte
&ensp;Par défaut
:::

Par défaut correspond au son propre à xDrip : l'alarme xDrip pour les lectures manquées, un son de notification plus doux pour les autres alertes. Utilisez CHOISIR LE FICHIER pour choisir une sonnerie du téléphone ou votre propre fichier.
Depuis le [25 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.25), le son plus doux est aussi utilisé lorsque la sonnerie *Par défaut* du téléphone est sélectionnée, y compris sur les installations mises à jour depuis une version antérieure au 9 sept. 2026 qui n'ont jamais modifié ce paramètre : les alertes de valeur incertaine, de hausse, de chute et similaires ne ressemblent plus à l'alarme de glycémie.

::: xdripitem Substituer le mode silencieux pour ces alertes<img src="../images/EN.png" style="zoom:75%;" />
:::

::: xdripitem Vibrer en cas d'alerte<img src="../images/EN.png" style="zoom:75%;" />
:::

### Alertes supplémentaires {#extra-alerts}

::: xdrip Alertes supplémentaires (xDrip+)
:::

##### Alerte Haute persistante {#persistent-high-alert}

::: xdripitem Alerte Haute persistante
:::

Au lieu d'une alerte Haute qui se déclenche dès que la glycémie atteint la valeur de déclenchement, vous pouvez configurer une alerte Haute persistante qui ne se déclenche que si la glycémie reste au-dessus d'une valeur définie pendant plus d'une certaine durée. Vous pouvez utiliser la [Valeur Haute](./settings#glucose-units) de xDrip ou une valeur de votre choix pour déclencher cette alerte.

::: xdripitem Activer<img src="../images/OFF.png" style="zoom:75%;">
&ensp;Notifier si le seuil ci-dessus est plus long que la durée spécifiée ci-dessous
:::

::: xdripitem Seuil : Valeur Haute<img src="../images/ON.png" style="zoom:75%;">
&ensp;Lorsque cette option est activée, la valeur Haute est le seuil.  
&ensp;Lorsqu'elle est désactivée, le seuil est la valeur spécifiée ci-dessous.  
:::

::: xdripitem Seuil
&ensp;170 mg/dl
:::

::: xdripitem pendant plus de (minutes)
&ensp;60
:::

::: xdripitem Répétition maximum toutes les (minutes)
&ensp;20
:::

::: xdripitem Son d'alerte  
&ensp;Choisissez le son utilisé pour l'alarme.
:::

::: xdripitem Ignorer le mode silencieux<img src="../images/DIS.png" style="zoom:75%;">
:::

::: xdripitem Vibrer en cas d'alerte<img src="../images/EN.png" style="zoom:75%;">
:::

##### Alerte de prévisions d'hypoglycémie {#forecasted-low-alert}

::: xdripitem Alerte de prévisions d'hypoglycémie
:::

Vous pouvez définir une alarme sur une prévision d'hypoglycémie. Cette fonction utilise l'**impulsion** (extrapolation de la tendance actuelle de la glycémie) et **pas** les paramètres de [prédiction](./predictions). Le seuil de prévision (en minutes) est le délai dans lequel une hypoglycémie est prévue (celui qui s'affiche habituellement en jaune sur l'écran du graphique).

Les prévisions d'hypoglycémie affichent un message sur l'écran de xDrip. Pour qu'une alarme sonne lorsqu'une hypoglycémie est prévue, activez Déclencher alarme sur prévision Basse.

::: xdripitem Prévisions Basses<img src="../images/ON.png" style="zoom:75%;">
&ensp;Considérant la valeur actuelle et la tendance, calculer ce que seront les prochaines lectures si la tendance persiste (extrapolation). Cela ignore l'insuline ou les glucides ingérés.
:::

::: xdripitem Déclencher alarme sur prévision Basse<img src="../images/DIS.png" style="zoom:75%;">
&ensp;Notifier lorsque les prédictions Basses atteignent le seuil
:::

::: xdripitem Seuil : Valeur basse<img src="../images/ON.png" style="zoom:75%;">
&ensp;Lorsque cette option est activée, la valeur basse est le seuil.  
&ensp;Lorsqu'elle est désactivée, le seuil est la valeur spécifiée ci-dessous.
:::

::: xdripitem Seuil
&ensp;70 mg/dl
:::

::: xdripitem Seuil de prévisions d'hypoglycémies [minutes]
&ensp;40
:::

::: xdripitem Son d'alerte 
&ensp;Choisissez le son utilisé pour l'alarme.
:::

::: xdripitem Ignorer le mode silencieux<img src="../images/DIS.png" style="zoom:75%;">
:::

::: xdripitem Vibrer en cas d'alerte<img src="../images/EN.png" style="zoom:75%;">
:::

Dans l'exemple ci-dessous, si vous réglez le Seuil de prévisions d'hypoglycémies à 50 minutes, l'alarme se déclenche. La ligne pointillée rouge est la tendance de glycémie prévue, extrapolée à partir des mesures précédentes.

<img src="./images/M-S-AA-EAb2.png" style="zoom:75%;" />

##### Notifications d'expiration des capteurs {#sensor-expiry-notifications}

::: xdripitem Notifications d'expiration des capteurs
&ensp;Notifier lorsque le capteur est proche de l'expiration.
:::

::: xdripitem Activer<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Notifier lorsque le capteur est proche de l'expiration.
:::

Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), un abonné affiche la même notification lorsque l'avertissement d'expiration du téléphone principal lui parvient, à condition que ce paramètre soit aussi activé sur l'abonné et que les traitements soient synchronisés depuis le téléphone principal. L'avertissement s'affiche une fois par avertissement du capteur, et il est ignoré s'il arrive sur l'abonné avec plus de 30 minutes de retard.

##### Nouvelle sonnerie pour les abonnés {#follower-chime-new}

Après des lectures manquées, une notification sonne lorsque de nouvelles données arrivent après plus de 20 minutes.

::: xdripitem Nouvelle sonnerie pour les abonnés<img src="../images/OFF.png" style="zoom:75%;">  
&ensp;Avertir si des données arrivent du maître si l'intervalle est > 20 mins.
:::

## Mise en veille Alertes {#snooze-alert}

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Mise en veille Alertes
:::

S'il n'y a pas d'alerte active, vous pouvez **mettre en veille à l'avance** les alertes depuis ce menu pour qu'elles ne se déclenchent pas pendant un certain temps.

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Mise en veille
<div style="text-align: center;"> Aucune alerte active existe</div>  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;Désactiver alertes Basses&emsp;</div>  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;Désactiver alertes Hautes&emsp;</div>  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;Désactiver toutes les alertes&emsp;</div>
:::

Une durée de mise en veille par défaut vous est proposée. Faites défiler vers le haut ou le bas pour la modifier.

::: xdrip Mise en veille par défaut
<div style="background-color: darkgray; color: dimgray; text-align: center;">&nbsp;  
    50 minutes  
  </div>
  <div style="background-color: darkgray; color: black; text-align: center;">&nbsp;  
    60 minutes  
  </div>
  <div style="background-color: darkgray; color: dimgray; text-align: center;">&nbsp;  
    70 minutes  
</div>
:::

Lorsqu'une alerte se déclenche, vous voyez la notification dans le volet déroulant de votre téléphone, et vous entendez éventuellement le son.

Vous pouvez mettre l'alerte en veille en balayant la notification, ou la personnaliser davantage en appuyant dessus.

<img src="./images/M-SNOc.png" style="zoom:75%;" />  

Vous pouvez ouvrir le menu de mise en veille en appuyant sur la notification ou depuis le menu principal de xDrip, Mise en veille Alertes.

Le menu de mise en veille affiche alors aussi l'alerte active.  
Appuyer sur Mise en veille la met en veille pour la durée sélectionnée.

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Mise en veille
<div style="background-color: dimgray; color: white; text-align: center;">  
<big><big>Mise en veille</big></big></div> 
<div style="background-color: dimgray; color: white; text-align: center;">&nbsp;  
<div style="background-color: black; color: dimgray; text-align: center;">&nbsp;  
    20 minutes  
  </div>
  <div style="background-color: black; color: darkgray; text-align: center;">&nbsp;  
    30 minutes  
  </div>
  <div style="background-color: black; color: dimgray; text-align: center;">&nbsp;  
    40 minutes  
</div></div>  

L'alerte active nommée "Night" existe. Alerte se reproduira à 1:25:01 (0 minutes restantes)  

<div style="background-color: dimgray; color: white; text-align: center;">  &emsp;Désactiver alertes Basses&emsp;</div>  
<div style="background-color: dimgray; color: white; text-align: center;">  &emsp;Désactiver alertes Hautes&emsp;</div>  
<div style="background-color: dimgray; color: white; text-align: center;">  &emsp;Désactiver toutes les alertes&emsp;</div> 
:::

##### TOUTES LES ALERTES ACTUELLEMENT DÉSACTIVÉES {#all-alerts-currently-disabled}

Si vous mettez en veille à l'avance (désactivez) toutes les alertes, ce message d'avertissement s'affiche.

<img src="./images/M-SNOe.png" style="zoom:75%;" />  

Pour le faire disparaître, vous devez réactiver les alertes.

::: xdrip <img src="../images/BDM.png" style="zoom:75%;" />Mise en veille
<div style="text-align: center;"> Toutes les alertes désactivées jusqu'à 15:09:12</div>  
<div style="background-color: gray; color: white; text-align: center;">  &emsp;Re-activer toutes les alertes&emsp;</div>  
:::

<br>

## Notification d'alerte visible {#visible-alert-notification}

Disponible à partir d'Android 8.

Lorsqu'une alerte se déclenche, elle apparaît dans le volet déroulant des notifications.

<img src="./images/M-SNOg.png" style="zoom:75%;" />  

La balayer la met en veille, appuyer dessus ouvre un menu de préférences.  
Distribuer en mode silencieux ne concerne que la notification Android elle-même. Depuis le [9 sept. 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.09.09), le son et la vibration de l'alerte sont joués par xDrip et suivent les paramètres d'alerte de xDrip, et non le [canal de notification](#notification-channels).

<img src="./images/M-SNOh.png" style="zoom:75%;" />

Vous pouvez revenir à la distribution avec alerte depuis le même menu.

<img src="./images/M-SNOi.png" style="zoom:75%;" />  

Paramètres vous mène aux réglages des notifications de votre téléphone.

<img src="./images/M-SNOk.png" style="zoom:75%;" />  

Vous pouvez aussi désactiver complètement les [canaux de notification](#notification-channels) de xDrip. Cela masque les notifications mais n'arrête pas le son de l'alerte.

<img src="./images/M-SNOj.png" style="zoom:75%;" />  



[*Dernière modification le 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
