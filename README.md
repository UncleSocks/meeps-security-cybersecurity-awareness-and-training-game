![logo](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/c5b14863-d780-49b4-a6e0-72bdc57b9d22)


MEEPS SECURITY is a simulation game designed to extend cybersecurity training and awareness by playing as an L1 Security Operation Center (SOC) analyst. Players handle incoming calls regarding cybersecurity incidents, evaluating and submitting the appropriate threat to the callers within the given service level agreement (SLA). The player must correctly resolve at least 80% of tickets to pass the assessment during the shift.

**Note:** The game is playable but still under development.

# Gameplay

The main menu has three buttons: START SHIFT, CREATE TICKETS, and LOG OFF. To play MEEPS SECURITY, select the "START SHIFT" button. This will take you to the main game loop, where you play as an L1 SOC analyst. 

MEEPS SECURITY also allows players to create their own custom tickets by selecting the "CREATE TICKET" button.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/2510b5d9-9faf-46c3-b347-392ac0107e94)

The "LOG OFF" button exits the game -- you can also click on the close window button.

## Starting Your Shift

When starting your shift, you will anticipate calls from various MEEPS SECURITY clients regarding cybersecurity incidents. 

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/8762a4d7-10e2-48c0-86f3-4bbc45fdcddc)

A pop-up window will be displayed when an incoming call must be answered within the specified SLA. Failure to answer within SLA will deny you the opportunity for a possible score.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/831045de-8828-40f7-b06c-862076ae6ca0)

After answering the call, MEEPS SECURITY will display the current caller information, specifically their name, organization, email, and contact number, together with their cyber security concern (ticket). MEEPS SECURITY provides the players with a list of threats, a brief description of the threat, its indicators, and countermeasures. The player must analyze the ticket, select the appropriate threat (from the list), and submit it to the caller. The player will be granted a score when the correct threat is submitted. In addition, the players must be able to submit the appropriate threat within the allotted SLA for a score to be granted.

**Note:** More threats and scenarios will be added over time.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/c651298a-4344-4456-81e1-2ac5e8048382)

After your shift, your performance will be evaluated. The players must have submitted at least 80% correct threats to pass the assessment. The shift report also provides the total number of tickets handled, any missed calls and missed tickets.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/66c959f0-5629-427d-a11c-6ed31a68a9ff)

Click the "END SHIFT" button to end the game. 


Currently, MEEPS SECURITY does not save your progress. It selects a random ticket from the SQLite database.


## Creating Tickets

MEEPS SECURITY also allows you to create your own tickets by selecting the "CREATE TICKET" on the main menu. It aims to allow users to add their own scenarios to train SOC analysts -- or for those who want to expand the game.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/a4d91d64-a262-4daa-a16e-fe8f2dc736b3)

Enter the ticket title and description, then choose the threat (answer) relating to the ticket. Click the "CREATE TICKET" button to add the custom ticket. MEEP SECURITY automatically correlates the Guest account to all custom tickets.

**Note:** You can definitely manually create new accounts and correlate them to a certain ticket.

![image](https://github.com/UncleSocks/meeps-security-cybersecurity-awareness-and-training-game/assets/79778613/b72fbffc-c1b6-44ac-8b23-67bd70256f6d)

A confirmation pop-up window will notify the player that the new ticket has been successfully inserted into the database.



