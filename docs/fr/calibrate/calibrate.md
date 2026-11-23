---
source_hash: b31e419e7a
source_commit: 7a18e7c
---
::: warning Étalonnage
Ne faites jamais aveuglément confiance à un capteur de glucose : vérifiez régulièrement les valeurs par une glycémie capillaire.  
Une ligne plate (toujours la même valeur) n'est **jamais** bon signe.
:::

### Considérations générales {#general-considerations}

L'étalonnage est essentiel à la précision des mesures du CGM. Utilisez toujours un lecteur de glycémie fiable et placez-vous dans les meilleures conditions pour obtenir la mesure capillaire la plus précise possible au moment d'étalonner.

Parmi les prérequis les plus importants :

1. **Glycémie stable.** N'étalonnez jamais lorsque la glycémie monte ou descend rapidement.
2. **Dans la cible (important pour l'étalonnage initial du Libre).** Essayez d'étalonner lorsque la glycémie est dans la plage normale (80-180 mg/dl ou 5-10 mmol/l).
3. **N'étalonnez pas trop.** Mieux vaut quelques étalonnages précis que trop nombreux : vous risquez fort d'embrouiller xDrip. Pour les G6, G7, ONE, ONE+, suivez les recommandations du fabricant.

### Algorithmes natif et xDrip {#native-and-xdrip-algorithms}

xDrip peut appliquer ses propres algorithmes de calibration aux capteurs qui envoient des données brutes.

La calibration native des G6, G7, ONE, ONE+ signifie que xDrip n'utilise pas son algorithme : il envoie les valeurs de calibration à l'émetteur et le laisse les traiter avec son propre algorithme propriétaire.

Les capteurs Libre 1, 14 jours, Pro, 2 (EU) et 2+ (EU) n'envoient que des données brutes et ont besoin soit de la calibration xDrip, soit d'un plugin de calibration externe appelé [algorithme hors processus](../use/OOP) (OOP en abrégé).

L'application patchée du Libre 2 utilise son propre algorithme propriétaire (une ancienne version, toutefois).

| Capteur                          | Calibration xDrip              | Calibration native |
| ------------------------------- | ------------------------------- | ------------------ |
| G6 avec pile remplacée                  | Disponible                       | Disponible          |
| G6, G7, ONE, ONE+                   | Non disponible                   | Obligatoire          |
| Libre 1                         | Obligatoire                       | OOP1 (obsolète)    |
| Libre 2 EU application patchée          | Décalage limité (voir ci-dessous)      | Par conception          |
| Libre 2/2+ EU, Libre 14 jours US | [Facultative](../use/OOP#oop2) | OOP2               |

##### Application patchée Libre 2 {#libre-2-patched-app}

Avec l'application patchée, vous pouvez étalonner, mais la correction est appliquée comme un décalage, dans la limite de -40 mg/dl à +20 mg/dL [-2,2 mmol/l à +1,1 mmol/l]. Les calibrations hors de ces limites sont **ignorées**.

### Paramètres de calibration de xDrip {#xdrip-calibration-settings}

::: warning Calibration xDrip uniquement
Les informations ci-dessous concernent la calibration xDrip.  
Pour le mode natif G6/G7/ONE/ONE+, voir [ici](https://navid200.github.io/xDrip/docs/Dexcom_page.html).
:::

Avant d'étalonner, vérifiez vos [paramètres](./advancedcal).

Une option à activer est l'affichage des [tables de données](../use/lesscommon#show-data-tables) dans le menu principal. Elle aide vraiment à comprendre ce qui se passe quand les choses tournent mal.

### Premier étalonnage {#first-calibration}

Si votre capteur nécessite des calibrations, une fois qu'il est connecté à xDrip et que trois valeurs ont été reçues, cette demande devrait s'afficher :

::: xdripitem Calibrer le capteur?
&emsp;Nous avons quelques valeurs!  


&ensp;Ensuite, nous avons besoin d'un premier test de glycémie capillaire.  

&ensp;Prêt à calibrer maintenant ?  

&emsp;NON&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;CALIBRER&ensp;</span>
:::

Les deux valeurs d'étalonnage initial sont un héritage du G4. Pour les utiliser correctement, faites deux mesures différentes (deux bandelettes) : c'est l'approche recommandée. Si vous saisissez habituellement la même valeur, vous pouvez en faire le comportement par défaut [ici](./advancedcal#calibrations).

::: xdrip ☰&emsp;Étalonnage initial
&emsp;<u>Entrer la première valeur de glycémie</u>  
&emsp;<u>Entrer la seconde valeur de glycémie</u>  

&emsp;<small>Pour pouvoir commencer, effectuer deux tests de glycémie capillaire et entrer les valeurs ici!</small>    
:::

Si vous utilisez la calibration native, la valeur est envoyée à l'émetteur pour être traitée.

Si vous utilisez la calibration xDrip, cette valeur est traitée 10 minutes plus tard afin de compenser tous les retards physiologiques et chimiques de la mesure du CGM : **c'est pourquoi il est extrêmement important d'étalonner à glycémie stable**.

Voyons graphiquement ce qui se passe sur l'écran principal :

1. Première valeur (ramenée à la valeur de calibration)
2. Deuxième valeur (ramenée à la valeur de calibration)
3. Pas encore visible, mais c'est la troisième valeur : la valeur réelle au moment où vous avez étalonné
4. Valeur suivante dans 5 minutes
5. Valeur suivante dans 10 minutes et point de calibration (qui sera utilisé dans 10 minutes)

<img src="./images/CAL03.png" />

Si votre glycémie est restée stable pendant ce temps, vous devriez voir la courbe passer par le point de calibration.

<img src="./images/CAL04.png" />

Dans votre tableau de calibrations, vous verrez de nouvelles entrées correspondant aux mesures brutes utilisées pour définir la calibration :

1. La valeur que vous avez saisie (convertie si nécessaire en mg/dl)
2. La même valeur dans l'unité que vous utilisez dans xDrip (ici en mg/dl, mais elle s'affiche aussi en mmol/l)
3. La glycémie brute du capteur
4. La pente et l'ordonnée à l'origine calculées
5. La date et l'heure effectives de la calibration (soit l'heure réelle + 10 minutes) et la date et l'heure de la mesure brute correspondante
6. Il y a deux jeux de mesures brutes pour une calibration : un plus bas, un plus haut

<img src="./images/CAL05.png" style="zoom:75%;"  />

Votre graphe de calibration ressemble maintenant à ceci.  
Selon l'écart entre les échantillons sanguins et la variabilité de la glycémie du moment, la pente n'est pas forcément exactement 1.

<img src="./images/CAL06.png" style="zoom:75%;"  />

### Étalonnages suivants {#successive-calibrations}

Par sécurité, vous vérifierez régulièrement votre glycémie réelle, au moins une fois par jour, car vous ne pouvez pas faire aveuglément confiance à un capteur. Saisissez ces glycémies capillaires comme [traitements](../use/mainUI#treatments).  
Pour avoir des glycémies qui ne varient pas trop vite, n'étalonnez pas lorsque des glucides ou de l'insuline sont actifs à ce moment-là.

::: info Fréquence
À moins que votre capteur ne l'exige expressément, n'étalonnez pas systématiquement à chaque glycémie capillaire.  
Pour les capteurs Libre, il n'est pas forcément nécessaire d'étalonner si l'écart est inférieur à 15 %.
:::

**N'étalonnez pas trop** : vous pouvez faire autant de glycémies capillaires que vous le souhaitez et les saisir comme traitements dans xDrip, mais ajoutez des calibrations avec beaucoup de précaution.

Sur votre graphe de calibration, les points de calibration actifs apparaissent en bleu, les anciens ou invalides en gris.

<img src="./images/CAL15.png" style="zoom:75%;"  />

Si, à glycémie stable, la valeur de xDrip 10 minutes après votre glycémie capillaire s'en écarte trop, ajoutez un nouveau point de calibration.

Comme l'évolution de la glycémie est souvent difficile à prévoir, vous pouvez utiliser une astuce :

- Vérifiez que Utiliser les valeurs BG des traitements n'est pas réglé sur Never use them dans [Calibration avancée](./advancedcal).
- Saisissez votre glycémie capillaire comme traitement.

<img src="./images/CAL07.png" style="zoom:75%;"  />

- Attendez 10 minutes et jugez si c'était un bon moment pour étalonner (assez stable).

<img src="./images/CAL08.png" style="zoom:75%;"  />

- Si c'était le cas, appuyez sur votre traitement (la nouvelle glycémie capillaire, point carré blanc sur le graphique) et transformez-le en calibration.

::: xdripitem Action de test sanguin

&emsp;Que voulez-vous faire?  

  &emsp;RIEN&emsp;EFFACER&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;CALIBRER&ensp;</span>
:::

Vous avez maintenant un point de calibration supplémentaire.

<img src="./images/CAL09.png" style="zoom:75%;"  />

### Désactiver une calibration {#disable-a-calibration}

Il peut arriver qu'un point de calibration soit manifestement mauvais et que vous vouliez le supprimer.

Ouvrez le Tableau de calibrations et faites un **appui long** sur la calibration à désactiver.

<img src="./images/CAL10.png" style="zoom:75%;"  />

::: xdripitem Disable this calibration?
Flagged calibrations will no longer have an effect.  

&emsp;&emsp;&emsp;NON&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;OUI&ensp;</span>
:::

Elle s'affiche en rouge et n'est plus utilisée dans les calculs.

<img src="./images/CAL11.png" style="zoom:75%;"  />

### Réinitialiser toutes les calibrations {#reset-all-calibrations}

Cette méthode ne s'applique qu'aux capteurs compatibles avec la calibration xDrip.

**Ne l'utilisez pas pour les capteurs à calibration native uniquement (G6 récent, G7, ONE, ONE+, etc.).**

Le moyen le plus rapide de reprendre l'étalonnage à zéro (Calibration initiale), lorsqu'il devient évident que les calibrations actuelles sont fausses ou que vous n'avez pas de données après avoir étalonné, est de réinitialiser toutes les calibrations.

Dans le menu principal, choisissez Arrêter le capteur.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Arrêter le capteur  
:::

**N'arrêtez pas le capteur** : réinitialisez seulement toutes les calibrations.

::: xdripitem <img src="../images/BDM.png" style="zoom:75%;" /> Arrêt du capteur <span class='symbol'></span>
  &emsp;N'arrêtez votre capteur que lorsque vous planifiez de l'enlever, sinon laissez fonctionner!  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;NE PAS ARRÊTER, SIMPLEMENT RÉINITIALISER LES CALIBRATIONS&ensp;</span>
:::

::: xdripitem Êtes-vous sûr?
  &emsp;Voulez-vous supprimer et réinitialiser les calibrations de ce capteur ?  

 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;NON &emsp;&emsp;&emsp;<span style="background-color: white; color: black;">&ensp;OUI&ensp;</span>
:::

xDrip vous ramène alors à l'[étalonnage initial](#first-calibration). Veillez à effectuer cette opération à glycémie stable, dans la cible.

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
