import random

table_in_text = '''1 Sourdough roll glistening with freshly applied butter and a garnish of parsley.
2 Braided loaf filled with minced and roasted fruits. Apple filled braids are particular popular in colder weather
3 A very dense loaf of yellow-looking bread cooked with yolks of owlbear eggs, very filling.
4 A two meter long twisted salty pretzel with a thin core of brown mustard. Feeds up to 12.
5 A sesame seed hamburger bun
6 A cheesy breadstick.
7 A danish (strawberry, lemon, snozzbery, cheese, etc. Choose new each time.)
8 A small loaf of warm pumpernickle
9 Barkskin biscuit that has a tough, almost woody, exterior, often soaked in milk or tea to soften.
10 A small loaf of cinnamon raisin bread.
11 Fairy bread - half slice of whitebread cut in the diagonal spred generously with butter and covered in rainbow sprinkles. Make a DC 10 Constitution save, on success, you gain 1d4 to initiative rolls for 8 hours, on fail you immediately vomit.
12 Dwarven ale bread is a very dense but flavorful bread made from ales and stouts (generally of dwarven make). Despite being baked, the potency of the drinks used in its making can still provide the eater a slight buzz when consumed. Often used as a desert by dwarves.
13 Jötnbrød (YERT-n-breh), a boule of dark rye bread enriched with bone meal, resulting in a beefy, slightly crunchy bread. A large handful is equivalent to a trail ration, but produces horrid constipation.
14 Sawyers flat, a horrid, matzo-like crispbread cut with maple (best), birch (ehhh), or pine (oh gods) sawdust. Often eaten by unskilled laborers, or during famine/drought.
15 A greenish, fist-sized loaf of bread that uses a flour made from exotic, far away seeds.
16 Raisin dotted sweetened bread rolled into spirals and heavily glazed. Topped with pistachios.
17 Small redish roll baked from a dried powered radish root instead of wheat. a Podling speciality.
18 Bagel (asiago, whole wheat, multigrain, blueberry, cherry, goodberry, etc. Choose new each time.)
19 A foot long bagette baked with whole garlic cloves.
20 Pepperloaf. A loaf of bread made with flour cut with ground pepper seeds and with minced pepper mixed into the dough. A delacacy among dragonborns.
21 Fresh cornbread and butter served with a side of honey, maple syrup, and/or fruit jam/jelly.
22 A slice of toasted wholewheat bread
23 Kobold loaf - delacacy among kobolds bread baked with mushrooms and cocaroaches.
24 A focaccia bread with asiago cheese
25 A hot and delicious cinnamon roll.
26 A hot cross bun.
27 A loaf of brown bread topped with whole oats.
28 A burrito-sized flour tortilla
29 Bowlcap a type of round, dense bread roll made to be crusty on one side but soft and steamed on the other. Typically eaten by laborers, the soft side is usually pressed down over the rim of a wooden bowl to act as a lid, containing and preserving the contents, until mealtime.
30 Flower bread is made from various types of powdered flowers giving it light floral taste and aroma.
31 Honey bread, bread but with honey.
32 A salted soft pretzel
33 Plum loaf. A sweet whitebread cooked from a sheet of dough sprinkled with chunks of plums and then rolled up.
34 Goodberry biscuit, made with the eponymous berries, grants 5hp when consumed, can be divided among five people, but cannot be admininstered to the unconscious.
35 Marbled rye bread
36 Spider bread that was baked by drow. Don’t ask. (Seriously)
37 A handful of croutons.
38 Tiny dense black rye roll that is studded with cloves
39 Fist-sized cup of hard bread, usually filled with stew.
40 A Ship's biscuit, barely edible but capable of lasting years at sea
41 A traveler's biscuit - similar, to ship's biscuit, but more palatable due to the addition of lard and salt, and with a shelf life of only a year.
42 Monkey's tail is a coil of thin pretzel-like bread that is boiled in soda ash, topped with salt and pepper, and then baked.
43 Cassava ball - A cheesy bread roll whose crisp crust gives way to a tender, lightly sour interior.
44 A dinner roll.
45 loaf of whitebread rich in protien because it is made with a meal made of ground dried maggots.
46 Mutton-bread, a double-fist-sized roll of steamed bread, that is filled with minced mutton spiced with plenty of pepper. The mutton is cooked inside the bread, so its juices leak out when bitten into.
47 Small crunchy rhubarb roll
48 A Red roll made with pig's blood instead of water, and stuffed with boiled pig stomach or intestine. Very nourishing, but smelly.
49 Golden pear bread, shiny and egg enriched, contains a generous filling of wine-stewed pears, cinnamon, and brown sugar.
50 "Peasant's breakfast", a barely-leavened flatbread that is split and stuffed with a chopped boiled egg
51 A finger-sized roll of brown bread drizzled with blackstrap molasses or watered-down maple syrup.
52 Damper bread - It's a simple blend of water, flour and salt that can be cooked directly in the ashes.
53 Fragrant caraway seed bun with a golden brown top glistening with butter.
54 Salt-roll a small round roll of chewy brown bread, topped with a truly alarming amount of flaky sea salt.
55 Nut breads, sweet or savory, baked with whatever nuts are locally grown.
56 A naan.
57 Mushroom bread, sometimes with unexpected medicinal properties.(roll 1d20 on a 20, full heal, on a 19, heal 1d4)
58 Tiny frosted rollp full of spices, nuts, or fruits.
59 A bread creation formed in the shape of a fantastical beast, castle, or scene
60 A scone stuffed with Bacon, sharp cheese, green onion, and hot pepper.
61 Chicken Bread, it's got the chicken baked in! So its great for those on the go.
62 Almond croissant sliced in half and filled with dark chocolate spread.
63 Siren’s Tack, a dry and dense bread, that is as hard as a brick. When eaten alone, this hardtack is basically a rock that sits in your gut. They are surprisingly filling, but a bit hard to keep down. It’s traditional to boil them in broth (to soften and flavor it) and serve under fish and gravy in port towns.
64 A tight ball made of a loaf of whitebread with the crusts removed mashed together.
65 Lifeleaf Wafer are small disks of flour, water, salt and finely chopped lifeleaf that are baked till hard. Naturally restorative, unnaturally salty. (heals 1 hp)
66 A hot, freshly boiled dumpling that smells as if it were cooked in a lamb stew. (you take 1 fire damage)
67 A twist of bread interweaving dark pumpernickle and wheat breads.
68 Faeriebread. A miniscule roll sprinked with faerie dust. When eaten, roll a d4 to see the effect (fly, greater invisibilty, blink, polymorph into a rabbit. The effects wear off after 1 hour.
69 Dwarvish baguette. Short and stout like its namesake.
70 Halfling pipeweed bread. Cooked with leaves of pipeweed, halflings make this bread to help them quit smoking pipeweed. Bitter but energizing.
71 Lembas bread. Broken into small bites, this small flatbread can feed up to 30.
72 Twice baked traveler's bread provides a tough but crisp foodstuff that is perfect for trail rations
73 Amaranth biscuits yield a subtle nutty flavor that goes well with many spreads.
74 A loaf of oat bread
75 Goodberry Biscuit - light, flaky, buttery biscuit infused with goodberry juice and drenched in a sweet sugary glaze. (heals 2 hp)
76 Elven Bolani, a common snack for elven miners - After rolling out the yeast-leavened dough into a thin sheet, the elf bakers layer bolani with a generous filling of potatoes, lentils, fresh herbs and scallions add bright flavor to the chewy, comforting dish, which gets a crispy crust when it's fried in shimmering-hot oil.
77 A small roll with a piece of apricot in the center.
78 A jalapeño loaf with melted cheddar on top.
79 A Fist-Sized dragon's blood roll When eaten, it adds 1 elemental damage to all attacks you make, and provides resistance to the dragon's element. roll 1d8 to determine the element. The effect fades after 1 hour.
80 A Loaf of soda bread.
81 Turtle bread, a round loaf that is baked at extremely high heat so that it is hard on the outside, and super soft on the inside.
82 A small loaf of sourdough bread with pineapple chunks mixed into it.
83 The most perfectly cooked Brioche roll you have ever had.
84 A perfectly toasted half-loaf of garlic bread.
85 Stone bread is perfect for adventurers as it will never go stale due to it already rock hard. It can double up as a rather effective improvised weapon. Mage by goliaths
86 Black moss breadstick, a jet-black appearance belies an earthy almost charcoal-like flavor that transitions to a mocha aftertaste.
87 Owlbear Claws are delicious semi-circular loaves of bread made with honey and fig. They are a foot across with large ‘claws’ cut out on one side. Will feed a party of five.
88 A chocolate and hazelnut swirled bun with magical blue sugar (that sparkles) sprinkled on top of them. When consumed you can change your eye colour for a minute.
89 A crumbly biscuit made with bear fat.
90 Prism dough is a bread that is risen to look like a triangular based prism. It tastes sweeter at the top of the spire and sourer nearer the base.
91 Chiploaf - A loaf of soft white bread encased in which is a whole chipmonk. A goblin delicacy
92 Troll Rolls are warm basil rolls, jarred with melted honey butter and sugared flesh.
93 A thick slice of sporebread smeared lightly with fire lichen paste. Made from bluestalk spores ground to a nutritious, bland flour. A staple of Duregar diets.
94 Seastar roll. A small dinner roll baked with minced sea star.
95 A loaf Tinker's bread. A speciality of tinker gnomes, itsa small whitebread baked with a gear, sprocket, or screw inside. (DC 15 Dex save or take 1 slashing or piercing damage eating it.)
96 Seedloaf - a whole wheat bread with a wide variatey of seeds baked in. A Kenku speciality. The quality of a seed loaf can be appraised by the number of seed types. The best are packed with seeds to the point where there is just enough dough for the loaf to hold together.
97 Bread of gradiation - Made by drabongorn monks from a pizza-like dough, they stretch one side very thin, and leave a large mound of dough on one side. This results in a one bread that all degrees of cooked from burnt to raw. They contelmpate the many factets of humanoid nature as they slowly consume this bread, as part of their meditions.
98 A pita pocket
99 A gnomish glowroll. Cooked with a paste made from glowing mushrooms, it is offputting to look at, but very filling. An aquired taste.
100 Buttered english muffin, best served warm to ensure that the butter soaks into the soft and spongy crust.'''

table_as_list = [item.strip().lstrip('1234567890 ') for item in table_in_text.splitlines()]

breads = dict(zip(range(1,101),table_as_list))

def get_random_bread():
    number = random.randint(1,100)
    return str(number) + ': ' + breads[number]

def bread_by_number(number):
    return str(number) + ': ' + breads[number]
