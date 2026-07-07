# Squad_analyzer_FM_2024
Small tool to help you analyze your FM2024 squad :)

How to get the data out of FM:
1. Download the view file "Attributes FM24.fmf" from here.
2. Save it in the Views folder, should be something like C:\Users\YourUser\Documents\Sports Interactive\Football Manager 2024\views.
3. In FM, go into your Squad view.
4. In the dropdown for the view selection, choose Custom/Import View
5. Select "Attributes FM24.ref" and Load.
6. You should now see all attributes (COR, CRO, DRI,...) for all of your players.
7. Click somewhere in that table, press Ctrl+A and then Ctrl+P.
8. Select "Web Page", click OK, and save it in a folder of your choice. It will save it as an html file (e.g. "Untitled.html").
9. Outside of FM, navigate to that folder and double-click on the html file. It should open in a browser and you should see the same table with players and attributes that you also saw in the game itself.
10. Select all the data of that table - ideally not with Ctrl+A (because that will add an unnecessary row at the top and also copy the link to sigames.com in the bottom), but with drag/drop
11. Now go into the tool itself, into the sheet "Squad", and paste into cell A1. The players and their attributes should now be shown here.
12. The data in the green sheets should in principle update immediately.
13. However, in some sheets you might need to drag the formulas further down (if you have more players) of delete a couple of rows with #N/A (if you have less players).
14. Enjoy :)
