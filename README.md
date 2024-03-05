
MEEPS Security is a simulation game designed to extend cybersecurity training and awareness through the perspective of an L1 SOC analyst. Players handle incoming calls regarding cybersecurity incidents, evaluating a list of cyber threats and delivering the appropriate solution within the designated SLA.

## Game Features (So Far)

**NOTE: This is still under development**

The basic game loop is functional. Players will receive an incoming call alert at a random interval, which must be answered within the presented SLA. 

![image](https://github.com/UncleSocks/meeps-security-a-soc-training-game/assets/79778613/076badbe-cf0b-4153-9569-cdd98efaf725)

Upon accepting the call, the players will be presented with a cybersecurity incident, which would require them to evaluate and determine the appropriate solution from the listed threats. Each threat, when selected, displays the description, impact, and mitigation of the threat. In addition, it also provides the current caller's information and image.

![image](https://github.com/UncleSocks/meeps-security-a-soc-training-game/assets/79778613/4bb1682f-5866-4fec-8867-50abed0b06b3)

When the correct threat is sent, the player gains a point. If the player fails to answer the incoming call within the designated SLA, a point is lost. In addition, if the submitted threat is wrong or the player fails to provide any answer within the given SLA, no point will be awarded.
