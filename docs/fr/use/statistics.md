---
source_hash: cf4c58239c
source_commit: 7a18e7c
---
::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_chart_areaspline_grey600_48dp.png" style="width:5%;" /> Statistiques
:::

L'écran Statistiques propose 3 affichages statistiques de base que vous pouvez configurer pour différentes périodes.

1. Sélectionnez d'abord la période sur laquelle calculer les statistiques : aujourd'hui, hier, les 7, 30 ou 90 derniers jours.
2. Vous pouvez afficher le graphique en plein écran (appuyez à nouveau dessus pour quitter le mode plein écran).
3. Vous pouvez partager l'écran sous forme de capture d'écran.

<img src="./images/M-STA1.png" style="zoom:75%;" />

<br>

Le premier écran affiche vos chiffres.

<img src="./images/M-STA2.png" style="zoom:75%;" />

Le pourcentage dans la cible est calculé à partir de la plage entre les valeurs basse et haute définies dans Menu - Unité de glycémie.  
Les nombres absolus comptent les mesures dans la cible, au-dessus et en dessous.  
La glycémie médiane est la valeur centrale de vos données : il y a autant de mesures au-dessus qu'en dessous.  
La glycémie moyenne est la moyenne arithmétique de toutes les mesures.  
L'HbA1c estimée n'est qu'un calcul mathématique basé sur la glycémie moyenne, converti en mmol/mol ou en pourcentage.  
StdDev, ou écart-type, est le résultat du calcul mathématique. Il montre la dispersion de vos glycémies.  
Le SD relatif (CV) est l'écart-type divisé par la moyenne ; il montre lui aussi la dispersion de vos mesures.  
GVI et PGS sont des paramètres introduits par Dexcom, voir [ici](https://web.archive.org/web/20160523152519/http://www.healthline.com/diabetesmine/a-new-view-of-glycemic-variability-how-long-is-your-line). 

Consultez [cette page](https://diatribe.org/understanding-average-glucose-standard-deviation-cv-and-blood-sugar-variability) pour des explications sur ces paramètres, et n'oubliez pas qu'ils sont basés sur les mesures et dépendent de leur qualité. De mauvaises mesures (imprécises) donneront de mauvaises statistiques, que ce soit à cause de la précision du capteur ou de vos étalonnages.

Vous pouvez choisir les valeurs affichées. Appuyez sur le menu (⋮) en haut à droite et sélectionnez `Parameters`, puis cochez ou décochez : Absolute #s, Median BG, Estimated A1C, Relative SD, GVI, PGS, Standard Deviation.

<br>

Balayez vers la gauche pour voir une représentation graphique de votre pourcentage dans la cible.  
Le vert correspond à la cible, le jaune au-dessus et le rouge en dessous.

<img src="./images/M-STA3.png" style="zoom:75%;" />

<br>

Balayez à nouveau pour voir le graphique des percentiles.

<img src="./images/M-STA4.png" style="zoom:75%;" />

Tournez l'écran pour un meilleur affichage.

<img src="./images/M-STA5.png" style="zoom:50%;" />

<br>

[*Dernière modification le 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
