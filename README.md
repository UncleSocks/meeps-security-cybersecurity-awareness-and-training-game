![logo](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/c5b14863-d780-49b4-a6e0-72bdc57b9d22)


MEEPS SECURITY is a simulation game designed to extend cybersecurity training and awareness by playing as an L1 Security Operation Center (SOC) analyst. Players handle incoming calls regarding cybersecurity incidents, evaluating and submitting the appropriate threat to the callers within the given service level agreement (SLA). The player must correctly resolve at least 80% of tickets to pass the assessment during the shift.

**Note:** The game is playable but still under development.

## Main Menu

The main menu has three buttons: START SHIFT, CREATE TICKETS, and LOG OFF. To play MEEPS SECURITY, select the "START SHIFT" button. This will take you to the main game loop, where you play as an L1 SOC analyst. 

MEEPS SECURITY also allows players to create their own custom tickets by selecting the "CREATE TICKET" button.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/578efc1d-da81-4d1a-968e-55ccac992c4d)

The "LOG OFF" button exits the game -- you can also click on the close window button.

## Starting Your Shift

When starting your shift, you will anticipate calls from various MEEPS SECURITY clients regarding cybersecurity incidents. 

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/f2436ebc-71ee-4e35-9364-769077e10b25)

A pop-up window will be displayed when an incoming call must be answered within the specified SLA. Failure to answer within SLA will deny you the opportunity for a possible score.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/dab533ad-b786-41f3-9244-4200f9f66357)

After answering the call, MEEPS SECURITY will display the current caller information, specifically their name, organization, email, and contact number, together with their cyber security concern (ticket). MEEPS SECURITY provides the players with a list of threats, a brief description of the threat, its indicators, and countermeasures. The player must analyze the ticket, select the appropriate threat (from the list), and submit it to the caller. When the correct threat is submitted, the player will be granted a score. In addition, the players must be able to submit the appropriate threat within the allotted SLA for a score to be granted.

**Note:** More threats and scenarios will be added over time.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/2ee38c2f-c9ff-46aa-955e-444c9ca28a10)

After your shift, your performance will be evaluated. The players must have submitted at least 80% correct threats to pass the assessment. The shift report also provides the total number of tickets handled, any missed calls and missed tickets.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/084114d0-3e9f-446f-845e-dee48dec3344)

Click the "END SHIFT" button to end the game. 


Currently MEEPS SECURITY does not save your progress. It selects a random ticket from the SQLite database.


## Creating Tickets

MEEPS SECURITY also allows you to create your own tickets by selecting the "CREATE TICKET" on the main menu. It aims to allow users to add their own scenarios to train SOC analysts -- or for those who want to expand the game.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/3170cacd-09f8-4b2e-86bd-e93d6f8ad4dd)

Enter the ticket title and description, then choose the threat (answer) relating to the ticket. Click the "CREATE TICKET" button to add the custom ticket. MEEP SECURITY automatically correlates the Guest account to all custom tickets.

**Note:** You can definitely manually create new accounts and correlate them to a certain ticket.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/bc54dfa1-f69a-4905-97c8-d4bfffcb2095)

A confirmation pop-up window will be displayed to notify the player that the new ticket has been successfully inserted to the database.



