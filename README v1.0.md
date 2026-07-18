# Squad_analyzer_FM_2024
Small tool to help you analyze your FM2024 squad :)

Link to the tool: https://docs.google.com/spreadsheets/d/1cq4W3ippnF-5XQUIlONsd4yGip8IvGrUICYmWempTe0/edit?usp=sharing (read-only access, so you need to make a copy of it)

How to get the data out of FM and into the tool:
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

Purpose of the different sheets:
1. Readme: Take a guess :)
2. Squad: This is where you paste the content of the html file with the players and their attributes.
3 Roles_per_formation: No need to look at this - it just lists which roles exist in which formation.
4. Important_attributes_per_role: No need to look at this - it just lists which attributes are important ("green") and secondary ("blue") for each role.
5. Role_count_per_attribute: No need to look at this - it just lists for how many roles each attribute is important or secondary.
6. Attribute_weighting_for_role_rating: If you want to, you can adjust how the important, the secondary, and the other attributes are weighted when calculating the role fit. (Default: 2/1/0.)
7. Role_rating_per_player: This shows how well each player fits each role, based on their attributes and your weighting of the important, secondary, and other attributes.
8. Difference_to_base_role_per_player: This shows how much worse each player is in each role compared to their best role.
9. Best_role_per_player: This shows the 5 best roles for each player.
10. Simple_best_XI: This shows the players in the highest rated goalkeeper role and the 10 highest rated outfield player's roles - so your best starting XI purely based on role ratings. The lineup that comes out of this might not make much sense in reality.
11. Player_flexibility: This shows how many roles each player can fill with at least X % (configurable) of his rating for his best role.
12. Best_player_per_role: This shows the 5 best players for each role. (Basically the opposite of "Best_role_per_player".)
13. Role_depth: This shows how many players can fill out each role with a rating above a configurable threshold. (Basically the opposite of "Player_flexibility".)
14. Top_5_Special_attributes: This shows the top 5 players for "special" attributes that are not included in any role (penalties,...) as well as the squad's average rating for each.
15. Top_5_All_attributes: This shows the top 5 players for all attributes as well as the squad's average rating for each.

Note: This is a hobby project so it's in no way guaranteed to be perfect. If you have any issues, let me know (ideally on reddit, @ami167) and I'll see what I can do :)
