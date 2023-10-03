# design doc sketch

(NOTE: reading this might spoil your experience with the future versions of the game)

## sleep

driving a car is tiring, so you need to rest. few possible sleeping places:
- in a car (last resort option, costs nothing, always available)
- in a tent (tent takes space and you need to be in non-urban area)
- in a hotel (costs money, but comfortable)
- get invited by one of your passengers to sleep at their place (should be quite rare, but the most fun)

conditions of your sleep should affect your energy/mood/whatever else stats there might be

## hitchhikers

- should have destination. if we make road non-linear, you'll have to choose path, with whom do you travel longer,
  whether to drive someone to their destination or keep on your journey
- you can ask them to pay for the gas (by dragging them to the cashier at gas station)
- you can have conversations with them which may affect your mood and their attitude towards you
- some hikers can offer you money for the trip on their own, which you can take or decline
- there should be a way to ask them for money directly, but they can refuse
- possibly you can rob them (by leaving their luggage to yourself? but then how do you sell it?)
- possibly they can rob you too
- you can ask them to drive instead of you (so you can rest or even sleep), but not everyone has a driver license

## places

- rural area: accommodation and restaurants are cheaper
- city: have all kinds of shops, hotels. sleeping in a car might be not welcomed by the police
- wilderness: you can camp if you have a tent

## seasons

it makes sense to start in summer, because it's easier to sleep in limited conditions, but adding different
seasons would increase fun and challenge

## road

most likely we want to make it non-linear, so the player can occasionally choose between which area to visit

## gas

usually you buy gas at gas stations, but in case you run out of it you may have to resort to asking people who
drive by to share some

## items

- tent+sleeping bag to sleep in
- spare tire
- winter tires (?)

## car space

currently we have fixed slots for everything, but it might be more fun to implement less rigid system where
you can for example fit more people at the expense of them being less happy

## economy

to make endless trip work, we assume some basic gas and food budget for the player

this could be implemented either in terms of daily allowance (and then you can save up or economize on gas
(by having your passengers to pay for it), food and accommodation) that is enough to keep going, but barely
or alternatively by having credit card, so you can occasionally go beyond your budget

## additional game modes

while original and perhaps the main mode is endless travel through infinitely generating map, it would make
sense to add additional hand-crafted maps which challenge player to beat them on time. for these, custom
economic setups can be made

## graphics

### travel

pseudo-3d style seems to work fine, but can also be replaced with 3d

in any case, we should make the travel more appealing. add changing scenery, show landmarks
from further down the road (this can be implemented by having the road hilly where you can see things
beyond current hill)

possible places to add:
- rail road where you might have to wait for the train to pass
- other cars passing by (this is necessary if we want to implement asking for gas mechanics, but is otherwise
  just for the atmosphere)
- bridges
- different landscapes corresponding to the area you're in

### management

to keep things simple, we probably want to keep management part of the game to fit on one screen, implementing
additional mechanics with the same top-down view

if we implement less rigid car-fitting mechanics, portrait-based view of people would make less sense. not sure
what to replace it with, though
