+++
date = '2026-08-23T00:59:17-03:00'
draft = false
title = 'The Long Way Ahead...'
feature = "OPFOR.png"
authors = ['lord-pump']

# ALAN'S NOTE:

# One or more author ids from data/en/authors.toml.

# Use a single teammate...
# authors = ['lord-pump']
# ...or credit several teammates on the same post, e.g.:
# authors = ['lord-pump', 'theinfinityglitch']
# ...or post as the whole team:
# authors = ['blufor-studio']

# To make a link: Visit the [Hugo](https://gohugo.io) website!
+++

## A brief look at the past...
At the time I'm writing this, **OPFOR** is merely an example of military jargon, 
yet another fancy acronym to describe any and all opposing forces from the eyes 
of allied forces. However, around two years ago, that same word marked the beginning 
of something far greater and bigger.

A young(er) ***Lord Pump***, blissfully oblivious to the nightmares and wonders 
that programming and videogame design entail, was already quite the fanatic of 
military simulations (or "milsims", for short) and other war games. Having seen 
some cardboard beasts like *Red Strike 1989* or the *Next War series*, as well 
as digital masterpieces like the *Arma series*, *Squad*, *Command: Modern Operations* 
and similars, he asked himself a simple question: *"Why weren't there any games 
capable of simulating every single aspect of a conflict instead of segmenting it 
into layers?"*. In other words, ***why can't it be all in one place?***.

The answer to that question was as blunt as it was obvious. The amount of work 
necessary for achieving such a feat was certainly insane: creating all the necessary 
assets, logic and data (and also handling them in a way that didn't melt an average 
computer) was indeed a *complex task at best* or an *insurmountable one at worst*. 
Fortunately for us, that answer wasn't satisfactory in the slightest and thus I 
committed myself into analyzing the problem until I could find a way to make it 
happen.

Today, **OPFOR** is no longer a dream, but a very far away goal that a group of 
enthusiastic and incredibly talented individuals happen to share. These people 
and their amazing skills share my eagerness to achieve such objective, and together 
at **[BLUFOR STUDIOS]** we have joined forces to try and make it the reality of tomorrow.

Now, we won't be getting into the nitty-gritty details of *how* we are going to 
achieve that (we'll save that for a future time though); however we will do a little 
bit of a briefing as to *what* exactly does that goal entail, or in other words:


## What makes OPFOR be OPFOR?
Well, as we saw in our previous question, it is simply **a game that makes it possible 
to fully simulate a war at any given scale and point you decide**: you could be a 
General and control a group of massive formations in a limited combat operation, or 
perhaps you are merely a tank gunner who got shoved into a devastatingly long war 
of attrition that goes on for years on end. The problem with this approach is that 
it'd feel way more like a *playable simulation* rather than an *actual game*, so 
we needed something more "precise" as to what we were going with.

For starters, there's a plethora of considerations that must be taken into account. 
Contrary to popular belief, a war has plenty more things to it than just having some 
glorified firecrackers go **"ka-boom"**. Ranging from nation-specific issues like 
*"what weapon systems do we field?"*, *"how big our stockpile of that munition is?"*, 
*"what specific structures should we strike first?"*; all the way to less "broad" 
questions like *"how long will it take for the CAS to arrive?"* or (if you were 
unfortunate enough to get caught in the crossfire yourself) **"how am I meant to 
survive?"**. Building a system that consistently binds all those experiences 
altogether is far from being easy, and you already know that. But you're reading this to 
hear about the solutions we found, not the problems we have. Therefore (and without 
further delay), I'll quote that one time when Julius Caesar said:

### Divide and conquer!
...well, to be precise for the history nerds out there (myself included), he most 
likely went with the Latin version of the saying: *"divide et impera"*. Point is, 
we took the (very) wise decision of splitting every single possible "task", "job" 
or otherwise "playable activity" within a war into three different echelons, according 
to their size in terms of *range of effect*. This resulted in the **High Command**, 
**Low Command** and **Tactical** echelons being made. 

- The **High Command** echelon compiles every single "job" that takes place on (or 
manages) ***strategic-size formations and assets***. These are units that are made 
up by a massive number of individuals, like *Corps* or above in NATO unit scale; 
as well as missile systems, sensors and other military-grade paraphernalia capable 
of inflicting damage to and/or affect a big chunk of terrain. ICBM management, long-range 
A2/AD assets, and strategic airlifts (as the name implies) are just some of the lengthy 
list of chores this echelon takes care of.

- The **Low Command** echelon behaves like the little brother of *High Command*, albeit 
it's far more useful on a practical sense. While the aforementioned formations cover 
vast amounts of terrain, wars aren't really fought on that scale and a more detailed 
insight of the conflict is usually needed to give troops functional plans that don't 
boil down to *"survive"*. This echelon covers the ***operational-size formations and 
assets***, which means it commands units that (despite being smaller in size) allow for 
more precision and finesse at the time of devising your plans.

- **Tactical** echelon is probably the one the gaming community will relate the 
most to. The "boots in the ground, getting your hands dirty" experience of being 
right into the frontline. You are one soldier in a very big conflict, and your 
decision-making stills are less about *"how do I win this war?"* and more of *"how 
do I make eliminate that target without killing myself in the process?"*. As the 
name implies, it's the one in charge of ***tactical-size formations and assets***, 
or in other words you and your squadmates (if you're a trooper), crew (if you're 
inside a ground vehicle), wingman (if you're a flyboy, like me!) or whatever other 
team you happen to be in at the time of playing.

Once the echelons' differences are set up, it is just a matter of sorting the "jobs" 
out and **making sure they all work together**. While this last part might seem 
insignificant in comparison to what we have already disclosed, it's actually one 
of the most important pillars of **OPFOR**'s essence.

### One simulation to rule them all
Beyond the gameplay, the graphics, the logic and other very important components, 
it's the internal simulation that really brings it all together. OPFOR runs it in 
the background, allowing it to know the state of any unit on the map as well as 
managing said units. Since it can see (and work with) **all echelons** altogether 
AND at the same time, it can influence said missions and change the conditions in 
real time to ensure a smooth, unified experience where *every act has a consequence*.

This methodology introduces yet another interesting set of properties into our game: 
no longer missions are individual, independent sorties where blasting off 10 tanks 
in a particular formation is irrelevant. Said losses are **permanent** and both sides 
**have to deal with them**. Personnel, gear, ammunition and every single piece of 
equipment or personnel is accounted for at all times, and that doesn't limit itself 
to specific assets; buildings, civilian conditions and infrastructure, as well as 
a wide arrange of other features is also saved and stored to ensure that every target 
hit is a little victory on itself that affects future operations.

Of course, the relevance and weight of said victories is proportional to the echelon 
of command it would "belong" to. **Tactical** losses are the day-to-day casualties 
of typical combat, but enough of those operations planned through the **Low Command** 
echelon is bound to seriously hurt your enemy; and a successful set of those will 
ultimately grant you a strategical advantage on **High Command**. This, in turn, 
also implies that whatever decisions (good or bad) are taken in the highest echelon 
will carry grave consequences to the lower echelons, meaning having a solid chain 
of command and good leadership is key to ensure your side has a fighting chance at 
all, like multiple conflicts across real-life history have proven time and time again.

This has a very particular side effect on players who are playing in **High Command**, 
as their own poor decision-making would not really yield any consequences that compare 
in severity to being killed in action because some politician and/or commander told 
you that you had to follow a specific RoE, or assault a position with impossible odds 
stacked against your unit. It's for this reason that **OPFOR** includes another interesting 
set of mechanics, which could not be better described without the use of yet another 
historical quote (often times attributed to Stalin himself, even though erroneously 
so):

### The death of a man is a tragedy...
...but the death of millions is a statistic. At least, that's one of the many variants 
that saying has; but what it really means in this context is also tied to the previous 
concept of **"there's a consequence to everything in OPFOR"**. Most videogames, 
specifically shooters, are known for the absolute lack of self-preservation whatsoever 
other than *"not losing the game"* (which despite being the point on more arcade-y 
FPS titles like *Battlefield* or *Call of Duty*, it's not really very fitting for milsim 
titles like *Arma, Squad, Steel Beasts, DCS, etc*). However, providing a player who 
is sitting in the comfort of their sofa and pressing some keys with the sensation of 
being a soldier with his life on the line, as well as balancing that with the other 
echelons' perspectives is a very complex issue that **cannot be solved with a single 
mechanic**.

One of the typical ways in which videogames solve this problem is by making the results 
of "losing" a game far more of a hassle than just taking a kick to one's ego. **Permadeath** 
modes are the most basic example of this methodology: the player loses the whole 
save if they fail; however that is usually more of an extreme challenge over the 
base game's experience rather than a standalone experience, and there's always the 
ever-present chance of it triggering due to a bug or imbalance of the game itself 
which isn't necessarily a player's mistake, *adding to the frustration of losing.* 
More mechanics of this kind include **inventory or resource loss**, or having to 
**travel your way back** to the frontline again, amongst others.

I don't want to get into much detail as to how **OPFOR** will be tackling these 
issues, first of all because it's going to be better addressed in later posts, it 
is one of the features that will take the longest to get implemented into the game, 
and we also want to save some surprises for the future. Long story short, we will 
include plenty of mechanics to ensure a **high-stakes, balanced gameplay** on the 
sense that every bullet counts, you cannot brush off impacts, you have to account 
for adrenaline and stress as well as the "fight or flight" response, amongst many 
other factors. This applies to *every enemy and ally* the same way it works for the 
player, and even though outdated gear and untrained forces can still win what would 
first seem like a losing battle, odds are they won't even if the player is one of 
them.

Another important way of how these methods will work cohesively in a way that is 
playable but also immersive comes from the fact that *the player's character* isn't 
who the player actually is. Instead you control their "mind", meaning the character 
is still capable of *freezing* or *reacting instinctively*. It will have high odds 
of giving priority to *pain response* rather than obeying the player commands when 
getting hit, and just like in real life you will *fumble when reloading* if there's 
a machine gun firing at your position. However, often times (particularly in games 
like these), **realism and gameplay** find themselves in **diametrically opposite ends** 
on what refers to game design. Talking about which, this is actually the perfect 
moment to talk about the next big topic: 


## The aesthetics of OPFOR
Beyond all the small details and specific trickery that we'll be using to **make OPFOR 
"feel" like OPFOR**, there's a very important underlying question that acts as the 
root of our *entire design philosophy*. Even though we are still a long way away from 
releasing most of the stuff we will be commenting on here, it's still worth giving 
a *first impression* as to what our aim actually is, so you can properly judge beforehand 
if **OPFOR** is your kind of game, or not.

### Realism, or immersion?
Although we clearly ain't conformist in the slightest, sometimes *sacrifices must 
be made*. While we try to achieve the best results on both of these categories, 
if we ever need to prioritize one of them above the other it'll be done so in a 
way that ensures **the most coherent feel gameplay-wise**. In other words, we will 
try to adequate to reality and also provide an enjoyable experience, but we prioritize 
*"the game feel"* over *"pinpoint realistic accuracy"* if we find ourselves in an 
extreme case. For example, making the game completely HUD-less from a first-person 
perspective could be troublesome for a handful of features, but we aim to **minimize 
its use on the game** and also design it in a way that blends with it in order to 
maximize immersion whenever possible.

### On the topic of graphics
It's pretty much standard issue these days to see milsim games showing off their 
*hyper-realistic high fidelity assets* in all their glory, and while that's not necessarily 
bad in and on itself, we believe it's a *poor decision* to operate ourselves in such 
fashion. Not only that'd make asset creation take a **considerably longer time** to do, 
but it'd also have a **negative impact in performance** for lower end devices, newer 
graphical fidelity technologies could **leave it deprecated** and it'd not "stand out" 
on that aspect, amongst other issues. It's for this reason that we've decided to 
take a rather "unique" approach: a ***stylished, low poly asset*** design phylosophy 
with ***high-detail pixel art*** is the most general sketch of what we're aiming 
to work with, making the most out of *illumination*, *particle effects*, *sound design* 
and other features to complement the atmosphere of the game and provide an enhanced 
sense of immersion.

### Can it run in *[insert potato computer]*?
While we do make a great effort on providing good performance in lower-end devices, 
**OPFOR** is still a **very heavy game** running a lot of things both in the background 
and also right in front of the player. We cannot promise levels of optimization akin 
to those of DooM (the original ones that runs on *literally anything*), but that 
doesn't mean we won't be trying our best to make the game *playable on something 
other than a NASA supercomputer*. One of the many ways we ensure our compromise with 
said standards is the fact that we always test our game on *multiple devices*, amongst 
which there's an array of both **high and low end computers** so we can get a *good idea* 
of the performance the playerbase would get at an average.

### How "exactly" does one play OPFOR?
The core fundamentals of playing **OPFOR** boils down to granting the player the 
ability to engage in any and all roles available at a conflict, which changes every 
time you run a new game. This means you can be a *tank gunner*, a *sniper* from 
Special Forces, an *air-superiority fighter jet pilot*, or even one of the *higher-ups* 
giving the orders. Explaining every single possible job at this point would be an 
impossible task, not only because they are on active development as we speak and 
most of them will take a **considerable amount of time** to get implemented but 
also because there's such a big amount of them that **it'd become an article** 
in and on itself.

Regarding the "where" and "who", **OPFOR** is mainly being developed as a ***first-person 
singleplayer experience for PCs*** sporting Windows and Linux operating systems. That 
being said, compatibility with other computer-based OS (like Mac) is intended, as 
well as multiplayer experiences in **cooperative** and **PvP** within the usual 
atmosphere of the game are intended to be available as well later down the line.

### The million dollar question...
...or in other words, is **OPFOR**'s price tag *a million dollars?* Same as with the 
gameplay or the performance questions, the following is just a *declaration of intentions* 
rather than *something set in stone*. Our aim is to **release public early access** once 
we achieve playability of a *good part of the High Command echelon* at a price of 
***roughly 20€***, then ramp up the price progressively until a ***max of around 40€*** 
once the game is "complete" in terms of gameplay (i.e. not accounting for additional 
units, factions, eras, etc. added afterwards which don't significantly alter gameplay 
but do add content to the game), from which it will *no longer increase*. Subscription 
systems, sponsorships, loot crate systems, purchasable cosmetics and similars will 
**NOT** be added anytime into the game as we believe in a **"single payment"** 
philosophy, meaning you get the whole game by simply paying once for it, *regardless 
of future price escalations*. As for **DLCs or Dowloadable Content**, it still remains 
unclear if we'll make use of them or not, but *they will be free* unless it provides 
some sort of *story mode/narrative* external to the main game itself, in which case 
we won't make it more expensive than the base game either and it'll be completely 
optional with ***no repercussions on the gameplay***.

Even with the big ones out of the way, there's still plenty of questions out there 
left to answer, like *"will OPFOR provide modding support?"* (yes), *"what nations 
or units will show up?"* (all fictional, with some randomness involved), *"what 
time period are we fighting in?"* (1990-2000s type of technology for the most advanced 
nations), etc. However, as with most of the other topics in this part of the article, 
we will uncover them in greater detail as we go. Talking about which, it's about 
time we tell you how we are...

## Paving the way there!
While we will deliver a proper **roadmap** of our development plans, alongside the 
corresponding explanations; we want to give you a broad sketch of where we will be 
focusing our efforts. As we have stated a couple of times before, our main aim right 
now is to complete the ***internal simulation***, ensuring it's up and running perfectly 
so we can add the rest of gameplay and functionality *on top of it*. After that, 
we will progressively add the rest of echelons, going from **High Command** to **Low 
Command** and then **Tactical**. 

This is obviously **not a hard limit** and we might find ourselves adding new capabilities 
to previous echelons later down the line: more weapon systems, platforms, mechanics, 
you name it! We'll also be providing *constant updates* on our ongoing progress, *sharing 
blog posts* like these with the latest news and making sure everything runs as **smoothly 
as possible** despite our limitations.

In the end, all of us know this is going to be a **very long marathon**. As awesome 
as the dream is, turning it into a reality is going to take a lot of *effort and time*; 
but is it really a sacrifice if we get to enjoy the ride? This is going to be a journey 
that we will share with you, blog by blog, update by update, and hopefully one day 
we will look back at this with pride, knowing that it's *no longer a fantasy*. That it's 
the *ultimate military simulation*, right in our hands. That it is... ***OPFOR***.