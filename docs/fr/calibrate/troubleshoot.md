---
source_hash: 54556a9422
source_commit: 7a18e7c
---
### Algorithme natif {#native-algorithm}

Si vous utilisez xDrip avec l'algorithme natif d'un G6, G7, ONE, ONE+ ou Stelo, voir [ici](https://navid200.github.io/xDrip/docs/Dexcom_page.html).

### Algorithme de xDrip {#xdrip-algorithm}

Activez les [tables de données](../use/lesscommon#show-data-tables) pour plus d'informations.

#### Pas de données après l'étalonnage initial {#no-data-after-initial-calibration}

<img src="./images/CAL16.png" style="zoom:75%;"  />

Si vous avez vérifié la connexion avec le capteur/transmetteur et qu'aucune donnée n'apparaît après l'étalonnage initial, c'est peut-être parce que vous étalonnez trop haut et que l'ordonnée à l'origine calculée dépasse la limite de sécurité. [Réinitialisez](./calibrate#reset-all-calibrations) toutes les calibrations et réessayez à glycémie stable, dans la plage basse.

#### Pas de données après l'ajout d'une nouvelle calibration {#no-data-after-adding-a-new-calibration}

<img src="./images/CAL18.png" style="zoom:75%;"  />

Vous avez probablement fait sortir les calibrations des limites de sécurité. Consultez le Tableau de calibrations et, si nécessaire, [désactivez](./calibrate#disable-a-calibration) la calibration en cause.

Un capteur qui nécessite une forte ordonnée à l'origine positive n'est peut-être pas sûr. Si vous pensez que votre capteur est encore fiable, [réinitialisez](./calibrate#reset-all-calibrations) toutes les calibrations et réessayez à glycémie stable, dans la plage basse.

#### La nouvelle calibration est ignorée {#new-calibration-is-ignored}

<img src="./images/CAL19.png" style="zoom:75%;"  />

Consultez le Tableau de calibrations : vous y verrez très probablement vos calibrations affichées en rouge, car elles sont désactivées pour des raisons de sécurité.

Votre capteur n'est très probablement plus fiable. Si vous pensez qu'il l'est, [réinitialisez](./calibrate#reset-all-calibrations) toutes les calibrations et réessayez à glycémie stable, dans la plage basse.

#### Ordonnée à l'origine ou pente au-delà de la limite de sécurité {#intercept-or-slope-above-safety-limit}

::: warning Sécurité
Les limites qui vous empêchent d'étalonner sont conçues pour votre propre sécurité.  
**Vous ne pouvez pas vous fier à un système incapable de détecter une hypoglycémie.**
:::

Ouvrez votre Tableau de calibrations et vérifiez la dernière calibration.

<img src="./images/CAL17.png" style="zoom:75%;"  />

::: warning L'ordonnée à l'origine maximale autorisée est de 39
Une ordonnée à l'origine supérieure à 39 mg/dl empêche l'affichage de la glycémie pour des raisons de sécurité.
:::

Les limites de pente dépendent de votre capteur :

| Capteur                                    | Pente minimale | Pente maximale |
| ------------------------------------------ | ------------- | ------------- |
| G5 ou G6 algorithme non natif (3 calibrations ou plus) | 0,7           | 1,6           |
| G5 ou G6 algorithme non natif (exactement 2 calibrations) | 0,75          | 1,5           |
| Libre (source de données brutes, Pentes du Libre non fixées activé) | 0,5           | 1,6           |
| Libre (source de données brutes, pente fixe par défaut) | 1 (fixe)     | 1 (fixe)     |
| Libre 2 application patchée                       | 1 (fixe)     | 1 (fixe)     |

Comme les limites de sécurité de la pente et de l'ordonnée à l'origine empêchent xDrip d'avoir une ordonnée à l'origine trop élevée, les calibrations qui mèneraient à cette situation sont ignorées.

Dans l'exemple ci-dessous, la ligne orange est celle qui correspond le mieux aux calibrations ; pourtant, xDrip utilise la rouge par sécurité, car son ordonnée à l'origine est sûre. La valeur d'ordonnée à l'origine du plugin montre ce qui correspondrait mieux aux calibrations.

<img src="./images/CAL20.png" style="zoom:75%;"  />

<br>

[*Dernière modification le 7/12/2024*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2024.11.26)
