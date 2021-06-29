import numpy as np
from PIL import ImageGrab
import pytesseract
import cv2
import pyautogui
import datetime
import keyboard

f = open('Valores-atuais.txt', 'r+')
f.truncate(0)


dt = datetime.date.today()
dt = datetime.datetime(dt.year, dt.month, dt.day)
print(dt)
dt = str(dt)




class Item:
    def _init_(self,id, name, tetocompra, tetovenda):
        self.name=name
        self.id=id
        self.tetocompra=tetocompra
        self.tetovenda=tetovenda


itens = []
itens.append(Item(1,'Angelic Axe',1000000,0))
itens.append(Item(2,'Assassin Dagger',1000000,0))
itens.append(Item(3,'Berserker',1000000,0))
itens.append(Item(4,'Blacksteel Sword',1000000,0))
itens.append(Item(5,'Blade of Corruption',1000000,0))
itens.append(Item(6,'Blade of Destruction',1000000,0))
itens.append(Item(7,'Bloody Edge',1000000,0))
itens.append(Item(8,'Bone Sword',1000000,0))
itens.append(Item(9,'Bright Sword',1000000,0))
itens.append(Item(10,'Broadsword',1000000,0))
itens.append(Item(11,'Carlin Sword',1000000,0))
itens.append(Item(12,'Cobra Sword',1000000,0))
itens.append(Item(13,'Combat Knife',1000000,0))
itens.append(Item(14,'Cowtana',1000000,0))
itens.append(Item(15,'Crimson Sword',1000000,0))
itens.append(Item(16,'Crimson Sword (Rashid)',1000000,0))
itens.append(Item(17,'Crude Umbral Blade',1000000,0))
itens.append(Item(18,'Crude Umbral Slayer',1000000,0))
itens.append(Item(19,'Crystal Sword',1000000,0))
itens.append(Item(20,'Crystalline Sword',1000000,0))
itens.append(Item(21,'Dagger',1000000,0))
itens.append(Item(22,'Demonrage Sword',1000000,0))
itens.append(Item(23,'Djinn Blade',1000000,0))
itens.append(Item(24,'Dragon Slayer',1000000,0))
itens.append(Item(25,'Eldritch Claymore',1000000,0))
itens.append(Item(26,'Emerald Sword',1000000,0))
itens.append(Item(27,'Epee',1000000,0))
itens.append(Item(28,'Falcon Longsword',1000000,0))
itens.append(Item(29,'Fire Sword',1000000,0))
itens.append(Item(30,'Giant Sword',1000000,0))
itens.append(Item(31,'Gilded Eldritch Claymore',1000000,0))
itens.append(Item(32,'Glooth Blade',1000000,0))
itens.append(Item(33,'Gnome Sword',1000000,0))
itens.append(Item(34,'Haunted Blade',1000000,0))
itens.append(Item(35,'Havoc Blade',1000000,0))
itens.append(Item(36,'Heavy Machete',1000000,0))
itens.append(Item(37,'Ice Rapier',1000000,0))
itens.append(Item(38,'Impaler of the Igniter',1000000,0))
itens.append(Item(39,'Incredible Mumpiz Slayer',1000000,0))
itens.append(Item(40,'Jagged Sword',1000000,0))
itens.append(Item(41,'Katana',1000000,0))
itens.append(Item(42,'Knife',1000000,0))
itens.append(Item(43,'Lion Longsword',1000000,0))
itens.append(Item(44,'Longsword',1000000,0))
itens.append(Item(45,'Machete',1000000,0))
itens.append(Item(46,'Magic Longsword',1000000,0))
itens.append(Item(47,'Magic Sword',1000000,0))
itens.append(Item(48,'Mean Knight Sword',1000000,0))
itens.append(Item(49,'Mercenary Sword',1000000,0))
itens.append(Item(50,'Mystic Blade',1000000,0))
itens.append(Item(51,'Nightmare Blade',1000000,0))
itens.append(Item(52,'Pharaoh Sword',1000000,0))
itens.append(Item(53,'Poet\'s Fencing Quill',1000000,0))
itens.append(Item(54,'Pointed Rabbitslayer',1000000,16000))
itens.append(Item(55,'Poison Dagger',1000000,15000))
itens.append(Item(56,'Rapier',1000000,15000))
itens.append(Item(57,'Ratana',1000000,15000))
itens.append(Item(58,'Relic Sword',1000000,13500))
itens.append(Item(59,'Ron the Ripper\'s Sabre',1000000,11000))
itens.append(Item(60,'Runed Sword',1000000,11500))
itens.append(Item(61,'Sabre',1000000,11500))
itens.append(Item(62,'Sai',1000000,8500))
itens.append(Item(63,'Scimitar',1000000,5000))
itens.append(Item(64,'Serpent Sword',1000000,5000))
itens.append(Item(65,'Shimmer Sword',1000000,5000))
itens.append(Item(66,'Shiny Blade',1000000,2500))
itens.append(Item(67,'Short Sword',1000000,5000))
itens.append(Item(68,'Silver Dagger',1000000,4000))
itens.append(Item(69,'Slayer of Destruction',1000000,2000))
itens.append(Item(70,'Soulcutter',1000000,2000))
itens.append(Item(71,'Soulshredder',1000000,1900))
itens.append(Item(72,'Spike Sword',1000000,0))
itens.append(Item(73,'Summerblade',1000000,0))
itens.append(Item(74,'Sword',1000000,1000))
itens.append(Item(75,'Tagralt Blade',1000000,0))
itens.append(Item(76,'Templar Scytheblade',1000000,0))
itens.append(Item(77,'Thaian Sword',1000000,0))
itens.append(Item(78,'The Avenger',1000000,0))
itens.append(Item(79,'The Calamity',1000000,0))
itens.append(Item(80,'The Epiphany',1000000,0))
itens.append(Item(81,'The Justice Seeker',1000000,0))
itens.append(Item(82,'Twiceslicer',1000000,0))
itens.append(Item(83,'Twin Hooks',1000000,0))
itens.append(Item(84,'Two Handed Sword',1000000,0))
itens.append(Item(85,'Umbral Blade',1000000,0))
itens.append(Item(86,'Umbral Master Slayer',1000000,0))
itens.append(Item(87,'Umbral Masterblade',1000000,0))
itens.append(Item(88,'Umbral Slayer',1000000,0))
itens.append(Item(89,'Warlord Sword',1000000,0))
itens.append(Item(90,'Winterblade',1000000,0))
itens.append(Item(91,'Wooden Sword',1000000,0))
itens.append(Item(92,'Wyvern Fang',1000000,0))
itens.append(Item(93,'Zaoan Sword',1000000,0))
itens.append(Item(94,'Abyss Hammer',1000000,0))
itens.append(Item(95,'Amber Staff',1000000,0))
itens.append(Item(96,'Arcane Staff',1000000,0))
itens.append(Item(97,'Banana Staff',1000000,0))
itens.append(Item(98,'Battle Hammer',1000000,0))
itens.append(Item(99,'Blessed Sceptre',1000000,0))
itens.append(Item(100,'Bone Club',1000000,0))
itens.append(Item(101,'Bonebreaker',1000000,0))
itens.append(Item(102,'Brutetamer\'s Staff',1000000,0))
itens.append(Item(103,'Chaos Mace',1000000,0))
itens.append(Item(104,'Clerical Mace',1000000,0))
itens.append(Item(105,'Club',1000000,0))
itens.append(Item(106,'Club of the Fury',1000000,0))
itens.append(Item(107,'Cobra Club',1000000,0))
itens.append(Item(108,'Cranial Basher',1000000,0))
itens.append(Item(109,'Crowbar',1000000,0))
itens.append(Item(110,'Crude Umbral Hammer',1000000,0))
itens.append(Item(111,'Crude Umbral Mace',1000000,0))
itens.append(Item(112,'Crystal Mace',1000000,0))
itens.append(Item(113,'Daramian Mace',1000000,0))
itens.append(Item(114,'Dark Trinity Mace',1000000,0))
itens.append(Item(115,'Deepling Squelcher',1000000,0))
itens.append(Item(116,'Deepling Staff',1000000,0))
itens.append(Item(117,'Demonbone',1000000,0))
itens.append(Item(118,'Diamond Sceptre',1000000,0))
itens.append(Item(119,'Drachaku',1000000,0))
itens.append(Item(120,'Dragon Hammer',1000000,0))
itens.append(Item(121,'Dragonbone Staff',1000000,0))
itens.append(Item(122,'Eldritch Warmace',1000000,0))
itens.append(Item(123,'Energized Demonbone',1000000,0))
itens.append(Item(124,'Falcon Mace',1000000,0))
itens.append(Item(125,'Ferumbras\' Staff (Club)',1000000,0))
itens.append(Item(126,'Furry Club',1000000,0))
itens.append(Item(127,'Giant Smithhammer',1000000,0))
itens.append(Item(128,'Gilded Eldritch Warmace',1000000,0))
itens.append(Item(129,'Glooth Club',1000000,0))
itens.append(Item(130,'Glooth Whip',1000000,0))
itens.append(Item(131,'Glutton\'s Mace',1000000,0))
itens.append(Item(132,'Hammer of Destruction',1000000,0))
itens.append(Item(133,'Hammer of Prophecy',1000000,0))
itens.append(Item(134,'Hammer of Wrath',1000000,0))
itens.append(Item(135,'Heavy Mace',1000000,0))
itens.append(Item(136,'Iron Hammer',1000000,0))
itens.append(Item(137,'Jade Hammer',1000000,0))
itens.append(Item(138,'Jungle Flail',1000000,0))
itens.append(Item(139,'Lich Staff',1000000,0))
itens.append(Item(140,'Life Preserver',1000000,0))
itens.append(Item(141,'Light Mace',1000000,0))
itens.append(Item(142,'Lion Hammer',1000000,0))
itens.append(Item(143,'Lunar Staff',1000000,0))
itens.append(Item(144,'Mace',1000000,0))
itens.append(Item(145,'Mace of Destruction',1000000,0))
itens.append(Item(146,'Maimer',1000000,0))
itens.append(Item(147,'Mallet Handle',1000000,0))
itens.append(Item(148,'Mammoth Whopper',1000000,0))
itens.append(Item(149,'Metal Bat',1000000,0))
itens.append(Item(150,'Moohtant Cudgel',1000000,0))
itens.append(Item(151,'Morning Star',1000000,0))
itens.append(Item(152,'Mortal Mace',1000000,0))
itens.append(Item(153,'Mycological Mace',1000000,0))
itens.append(Item(154,'Northern Star',1000000,0))
itens.append(Item(155,'Obsidian Truncheon',1000000,0))
itens.append(Item(156,'Ogre Klubba',1000000,0))
itens.append(Item(157,'One Hit Wonder',1000000,0))
itens.append(Item(158,'Onyx Flail',1000000,0))
itens.append(Item(159,'Orcish Maul',1000000,0))
itens.append(Item(160,'Ornate Mace',1000000,0))
itens.append(Item(161,'Pair of Iron Fists',1000000,0))
itens.append(Item(162,'Queen\'s Sceptre',1000000,0))
itens.append(Item(163,'Resizer',1000000,0))
itens.append(Item(164,'Rotten Demonbone',1000000,0))
itens.append(Item(165,'Sapphire Hammer',1000000,0))
itens.append(Item(166,'Scythe',1000000,0))
itens.append(Item(167,'Shadow Sceptre',1000000,0))
itens.append(Item(168,'Silver Mace',1000000,0))
itens.append(Item(169,'Skull Staff',1000000,0))
itens.append(Item(170,'Skullcrusher',1000000,0))
itens.append(Item(171,'Snake God\'s Sceptre',1000000,0))
itens.append(Item(172,'Soulcrusher',1000000,0))
itens.append(Item(173,'Soulmaimer',1000000,0))
itens.append(Item(174,'Spiked Squelcher',1000000,0))
itens.append(Item(175,'Spiky Club',1000000,0))
itens.append(Item(176,'Staff',1000000,0))
itens.append(Item(177,'Stale Bread of Ancientness',1000000,0))
itens.append(Item(178,'Strange Mallet',1000000,0))
itens.append(Item(179,'Studded Club',1000000,0))
itens.append(Item(180,'Sulphurous Demonbone',1000000,0))
itens.append(Item(181,'Swampling Club',1000000,0))
itens.append(Item(182,'Taurus Mace',1000000,0))
itens.append(Item(183,'The Stomper',1000000,0))
itens.append(Item(184,'Thunder Hammer',1000000,0))
itens.append(Item(185,'Umbral Hammer',1000000,0))
itens.append(Item(186,'Umbral Mace',1000000,0))
itens.append(Item(187,'Umbral Master Hammer',1000000,0))
itens.append(Item(188,'Umbral Master Mace',1000000,0))
itens.append(Item(189,'Unliving Demonbone',1000000,0))
itens.append(Item(190,'War Hammer',1000000,0))
itens.append(Item(191,'Chain Bolter',1000000,0))
itens.append(Item(192,'Cobra Crossbow',1000000,0))
itens.append(Item(193,'Crossbow',1000000,0))
itens.append(Item(194,'Crossbow of Destruction',1000000,0))
itens.append(Item(195,'Crude Umbral Crossbow',1000000,0))
itens.append(Item(196,'Crystal Crossbow',1000000,0))
itens.append(Item(197,'Modified Crossbow',1000000,0))
itens.append(Item(198,'Ornate Crossbow',1000000,0))
itens.append(Item(199,'Rift Crossbow',1000000,0))
itens.append(Item(200,'Royal Crossbow',1000000,0))
itens.append(Item(201,'Soulpiercer',1000000,0))
itens.append(Item(202,'The Devileye',1000000,0))
itens.append(Item(203,'The Ironworker',1000000,0))
itens.append(Item(204,'Thorn Spitter',1000000,0))
itens.append(Item(205,'Triple Bolt Crossbow',1000000,0))
itens.append(Item(206,'Umbral Crossbow',1000000,0))
itens.append(Item(207,'Umbral Master Crossbow',1000000,0))
itens.append(Item(208,'Cobra Wand',1000000,0))
itens.append(Item(209,'Deepling Ceremonial Dagger',1000000,0))
itens.append(Item(210,'Deepling Fork',1000000,0))
itens.append(Item(211,'Dream Blossom Staff',1000000,0))
itens.append(Item(212,'Eldritch Wand',1000000,0))
itens.append(Item(213,'Energized Limb',1000000,0))
itens.append(Item(214,'Falcon Wand',1000000,0))
itens.append(Item(215,'Ferumbras\' Staff (Wand)',1000000,0))
itens.append(Item(216,'Gilded Eldritch Wand',1000000,0))
itens.append(Item(217,'Jungle Wand',1000000,0))
itens.append(Item(218,'Lion Wand',1000000,0))
itens.append(Item(219,'Shimmer Wand',1000000,0))
itens.append(Item(220,'Sorc and Druid Staff',1000000,0))
itens.append(Item(221,'Soultainter',1000000,0))
itens.append(Item(222,'The Scorcher',1000000,0))
itens.append(Item(223,'Wand of Cosmic Energy',1000000,0))
itens.append(Item(224,'Wand of Darkness',1000000,0))
itens.append(Item(225,'Wand of Decay',1000000,0))
itens.append(Item(226,'Wand of Defiance',1000000,0))
itens.append(Item(227,'Wand of Destruction',1000000,0))
itens.append(Item(228,'Wand of Dimensions',1000000,0))
itens.append(Item(229,'Wand of Draconia',1000000,0))
itens.append(Item(230,'Wand of Dragonbreath',1000000,0))
itens.append(Item(231,'Wand of Everblazing',1000000,0))
itens.append(Item(232,'Wand of Inferno',1000000,0))
itens.append(Item(233,'Wand of Starstorm',1000000,0))
itens.append(Item(234,'Wand of Voodoo',1000000,0))
itens.append(Item(235,'Wand of Vortex',1000000,0))
itens.append(Item(236,'Cobra Rod',1000000,0))
itens.append(Item(237,'Deepling Ceremonial Dagger',1000000,0))
itens.append(Item(238,'Deepling Fork',1000000,0))
itens.append(Item(239,'Dream Blossom Staff',1000000,0))
itens.append(Item(240,'Eldritch Rod',1000000,0))
itens.append(Item(241,'Energized Limb',1000000,0))
itens.append(Item(242,'Falcon Rod',1000000,0))
itens.append(Item(243,'Gilded Eldritch Rod',1000000,0))
itens.append(Item(244,'Glacial Rod',1000000,0))
itens.append(Item(245,'Hailstorm Rod',1000000,0))
itens.append(Item(246,'Jungle Rod',1000000,0))
itens.append(Item(247,'Lion Rod',1000000,0))
itens.append(Item(248,'Moonlight Rod',1000000,0))
itens.append(Item(249,'Muck Rod',1000000,0))
itens.append(Item(250,'Necrotic Rod',1000000,0))
itens.append(Item(251,'Northwind Rod',1000000,0))
itens.append(Item(252,'Ogre Scepta',1000000,0))
itens.append(Item(253,'Rod of Destruction',1000000,0))
itens.append(Item(254,'Shimmer Rod',1000000,0))
itens.append(Item(255,'Snakebite Rod',1000000,0))
itens.append(Item(256,'Soulhexer',1000000,0))
itens.append(Item(257,'Springsprout Rod',1000000,0))
itens.append(Item(258,'Terra Rod',1000000,0))
itens.append(Item(259,'The Chiller',1000000,0))
itens.append(Item(260,'Underworld Rod',1000000,0))
itens.append(Item(261,'Bow',1000000,0))
itens.append(Item(262,'Bow of Cataclysm',1000000,0))
itens.append(Item(263,'Bow of Destruction',1000000,0))
itens.append(Item(264,'Composite Hornbow',1000000,0))
itens.append(Item(265,'Crude Umbral Bow',1000000,0))
itens.append(Item(266,'Eldritch Bow',1000000,0))
itens.append(Item(267,'Elethriel\'s Elemental Bow',1000000,0))
itens.append(Item(268,'Elvish Bow',1000000,0))
itens.append(Item(269,'Falcon Bow',1000000,0))
itens.append(Item(270,'Gilded Eldritch Bow',1000000,0))
itens.append(Item(271,'Hive Bow',1000000,0))
itens.append(Item(272,'Icicle Bow',1000000,0))
itens.append(Item(273,'Jungle Bow',1000000,0))
itens.append(Item(274,'Lion Longbow',1000000,0))
itens.append(Item(275,'Living Vine Bow',1000000,0))
itens.append(Item(276,'Musician\'s Bow',1000000,0))
itens.append(Item(277,'Mycological Bow',1000000,0))
itens.append(Item(278,'Rift Bow',1000000,0))
itens.append(Item(279,'Shimmer Bow',1000000,0))
itens.append(Item(280,'Silkweaver Bow',1000000,0))
itens.append(Item(281,'Soulbleeder',1000000,0))
itens.append(Item(282,'Umbral Bow',1000000,0))
itens.append(Item(283,'Umbral Master Bow',1000000,0))
itens.append(Item(284,'Warsinger Bow',1000000,0))
itens.append(Item(285,'Yol\'s Bow',1000000,0))
itens.append(Item(286,'Axe',1000000,0))
itens.append(Item(287,'Axe of Carving',1000000,0))
itens.append(Item(288,'Axe of Carving (Charged)',1000000,0))
itens.append(Item(289,'Axe of Carving (Heavily Charged)',1000000,0))
itens.append(Item(290,'Axe of Carving (Overcharged)',1000000,0))
itens.append(Item(291,'Axe of Destruction',1000000,0))
itens.append(Item(292,'Axe of Mayhem',1000000,0))
itens.append(Item(293,'Axe of Mayhem (Charged)',1000000,0))
itens.append(Item(294,'Axe of Mayhem (Heavily Charged)',1000000,0))
itens.append(Item(295,'Axe of Mayhem (Overcharged)',1000000,0))
itens.append(Item(296,'Axe of Remedy',1000000,0))
itens.append(Item(297,'Axe of Remedy (Charged)',1000000,0))
itens.append(Item(298,'Axe of Remedy (Heavily Charged)',1000000,0))
itens.append(Item(299,'Axe of Remedy (Overcharged)',1000000,0))
itens.append(Item(300,'Barbarian Axe',1000000,0))
itens.append(Item(301,'Battle Axe',1000000,0))
itens.append(Item(302,'Beastslayer Axe',1000000,0))
itens.append(Item(303,'Butcher\'s Axe',1000000,0))
itens.append(Item(304,'Chopper of Carving',1000000,0))
itens.append(Item(305,'Chopper of Carving (Charged)',1000000,0))
itens.append(Item(306,'Chopper of Carving (Heavily Charged)',1000000,0))
itens.append(Item(307,'Chopper of Carving (Overcharged)',1000000,0))
itens.append(Item(308,'Chopper of Destruction',1000000,0))
itens.append(Item(309,'Chopper of Mayhem',1000000,0))
itens.append(Item(310,'Chopper of Mayhem (Charged)',1000000,0))
itens.append(Item(311,'Chopper of Mayhem (Heavily Charged)',1000000,0))
itens.append(Item(312,'Chopper of Mayhem (Overcharged)',1000000,0))
itens.append(Item(313,'Chopper of Remedy',1000000,0))
itens.append(Item(314,'Chopper of Remedy (Charged)',1000000,0))
itens.append(Item(315,'Chopper of Remedy (Heavily Charged)',1000000,0))
itens.append(Item(316,'Chopper of Remedy (Overcharged)',1000000,0))
itens.append(Item(317,'Cobra Axe',1000000,0))
itens.append(Item(318,'Crude Umbral Axe',1000000,0))
itens.append(Item(319,'Crude Umbral Chopper',1000000,0))
itens.append(Item(320,'Crystalline Axe',1000000,0))
itens.append(Item(321,'Daramian Axe',1000000,0))
itens.append(Item(322,'Daramian Waraxe',1000000,0))
itens.append(Item(323,'Deepling Axe',1000000,0))
itens.append(Item(324,'Demonwing Axe',1000000,0))
itens.append(Item(325,'Double Axe',1000000,0))
itens.append(Item(326,'Dragon Lance',1000000,0))
itens.append(Item(327,'Drakinata',1000000,0))
itens.append(Item(328,'Dreaded Cleaver',1000000,0))
itens.append(Item(329,'Dwarven Axe',1000000,0))
itens.append(Item(330,'Eldritch Greataxe',1000000,0))
itens.append(Item(331,'Execowtioner Axe',1000000,0))
itens.append(Item(332,'Executioner',1000000,0))
itens.append(Item(333,'Falcon Battleaxe',1000000,0))
itens.append(Item(334,'Farmer\'s Avenger',1000000,0))
itens.append(Item(335,'Fire Axe',1000000,0))
itens.append(Item(336,'Gilded Eldritch Greataxe',1000000,0))
itens.append(Item(337,'Glooth Axe',1000000,0))
itens.append(Item(338,'Glorious Axe',1000000,0))
itens.append(Item(339,'Golden Axe',1000000,0))
itens.append(Item(340,'Golden Sickle',1000000,0))
itens.append(Item(341,'Great Axe',1000000,0))
itens.append(Item(342,'Guardian Axe',1000000,0))
itens.append(Item(343,'Guardian Halberd',1000000,0))
itens.append(Item(344,'Halberd',1000000,0))
itens.append(Item(345,'Hand Axe',1000000,0))
itens.append(Item(346,'Hatchet',1000000,0))
itens.append(Item(347,'Headchopper',1000000,0))
itens.append(Item(348,'Heavy Trident',1000000,0))
itens.append(Item(349,'Hellforged Axe',1000000,0))
itens.append(Item(350,'Heroic Axe',1000000,0))
itens.append(Item(351,'Hive Scythe',1000000,0))
itens.append(Item(352,'Ice Hatchet',1000000,0))
itens.append(Item(353,'Impaler',1000000,0))
itens.append(Item(354,'Knight Axe',1000000,0))
itens.append(Item(355,'Lion Axe',1000000,0))
itens.append(Item(356,'Mino Lance',1000000,0))
itens.append(Item(357,'Mythril Axe',1000000,0))
itens.append(Item(358,'Naginata',1000000,0))
itens.append(Item(359,'Noble Axe',1000000,0))
itens.append(Item(360,'Obsidian Lance',1000000,0))
itens.append(Item(361,'Ogre Choppa',1000000,0))
itens.append(Item(362,'Orcish Axe',1000000,0))
itens.append(Item(363,'Ornamented Axe',1000000,0))
itens.append(Item(364,'Phantasmal Axe',1000000,0))
itens.append(Item(365,'Plague Bite',1000000,0))
itens.append(Item(366,'Ravager\'s Axe',1000000,0))
itens.append(Item(367,'Ravenwing',1000000,0))
itens.append(Item(368,'Reaper\'s Axe',1000000,0))
itens.append(Item(369,'Rift Lance',1000000,0))
itens.append(Item(370,'Ripper Lance',1000000,0))
itens.append(Item(371,'Royal Axe',1000000,0))
itens.append(Item(372,'Ruthless Axe',1000000,0))
itens.append(Item(373,'Scythe of the Reaper',1000000,0))
itens.append(Item(374,'Sickle',1000000,0))
itens.append(Item(375,'Solar Axe',1000000,0))
itens.append(Item(376,'Soulbiter',1000000,0))
itens.append(Item(377,'Souleater (Axe)',1000000,0))
itens.append(Item(378,'Steel Axe',1000000,0))
itens.append(Item(379,'Stonecutter Axe',1000000,0))
itens.append(Item(380,'Throwing Axe',1000000,0))
itens.append(Item(381,'Titan Axe',1000000,0))
itens.append(Item(382,'Twin Axe',1000000,0))
itens.append(Item(383,'Umbral Axe',1000000,0))
itens.append(Item(384,'Umbral Chopper',1000000,0))
itens.append(Item(385,'Umbral Master Axe',1000000,0))
itens.append(Item(386,'Umbral Master Chopper',1000000,0))
itens.append(Item(387,'Vile Axe',1000000,0))
itens.append(Item(388,'War Axe',1000000,0))
itens.append(Item(389,'Warrior\'s Axe',1000000,0))
itens.append(Item(390,'Zaoan Halberd',1000000,0))
contadorgeral = 0

def checkitem():
    pyautogui.leftClick(100,584)
    pyautogui.keyDown('Ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyDown('Return')
    pyautogui.PAUSE = 0.05
    pyautogui.keyUp('Ctrl')
    pyautogui.keyUp('a')
    pyautogui.keyUp('Return')
    contador = contadorgeral
    i = int(contador)
    Item = str(itens[i].name)
    pyautogui.typewrite(''+Item, interval=0.005)
    pyautogui.leftClick(61, 282)
    pyautogui.sleep(1.5)

    print('O item avaliado agora é o: ' + str(itens[i].name) + '| ID: '+ str(itens[i].id))
    print('Venderei quando acima de: ' + str(itens[i].tetovenda) + 'gps')
    print('Comprarei quando abaixo de: ' + str(itens[i].tetocompra) + 'gps')
    print('---')

def lertela():
    report = open('Valores-atuais.txt', 'a')
    # -| Bloco de captura das ofertas |-#
    imagecompra = ImageGrab.grab(bbox=(405, 372, 485, 385))
    imagevenda = ImageGrab.grab(bbox=(410, 190, 485, 205))
    imageestoque = ImageGrab.grab(bbox=(380, 330, 421, 350))

    # -| Movimentação para leitura de histórico do item |-#
    pyautogui.leftClick(561, 621)
    pyautogui.sleep(1.5)
    histcompra = ImageGrab.grab(bbox=(385, 355, 425, 367))
    histvenda = ImageGrab.grab(bbox=(385, 420, 425, 432))
    pyautogui.leftClick(481, 624)

    # -| DEBUGGER - Visualização da captura de tela |-#
    # cv2.imshow("Imagecompra", np.array(imagecompra))
    # cv2.imshow("Imagevenda", np.array(imagevenda))
    # cv2.imshow("Imageestoque", np.array(imageestoque))
    # cv2.imshow("histcompra", np.array(histcompra))
    # cv2.imshow("histvenda", np.array(histvenda))
    # cv2.waitKey(0)

    txtcompra = pytesseract.image_to_string(imagecompra, lang='tibia',
                                            config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    txtvenda = pytesseract.image_to_string(imagevenda, lang='tibia',
                                           config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    textestoque = pytesseract.image_to_string(imageestoque, lang='tibia',
                                              config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    texthistcompra = pytesseract.image_to_string(histcompra, lang='tibia',
                                                 config='--psm 7 -c tessedit_char_whitelist=0123456789,')
    texthistvenda = pytesseract.image_to_string(histvenda, lang='tibia',
                                                config='--psm 7 -c tessedit_char_whitelist=0123456789,')

    # -| Tratamento e transformação da leitura para número inteiro |-#
    txtcompra = txtcompra.replace('\n', '')
    txtcompra = txtcompra.replace('\f', '')
    txtcompra = txtcompra.replace(',', '')
    txtcompra = txtcompra.replace(' ', '')
    if ((txtcompra) == ('')):
        txtcompra = 00
    txtcompra = int(txtcompra)

    # -| Tratamento e transformação da leitura para número inteiro |-#
    txtvenda = txtvenda.replace('\n', '')
    txtvenda = txtvenda.replace('\f', '')
    txtvenda = txtvenda.replace(',', '')
    txtvenda = txtvenda.replace(' ', '')
    if ((txtvenda) == ('')):
        txtvenda = 00
    txtvenda = int(txtvenda)

    # -| Tratamento e transformação da leitura para número inteiro |-#
    textestoque = textestoque.replace('\n', '')
    textestoque = textestoque.replace('\f', '')
    textestoque = textestoque.replace(',', '')
    textestoque = textestoque.replace(' ', '')
    if ((textestoque) == ('')):
        textestoque = 00
    txtestoque = int(textestoque)

    # -| Tratamento e transformação da leitura para número inteiro |-#
    texthistcompra = texthistcompra.replace('\n', '')
    texthistcompra = texthistcompra.replace('\f', '')
    texthistcompra = texthistcompra.replace(',', '')
    texthistcompra = texthistcompra.replace(' ', '')
    if ((texthistcompra) == ('')):
        texthistcompra = 00
    texthistcompra = int(texthistcompra)

    # -| Tratamento e transformação da leitura para número inteiro |-#
    texthistvenda = texthistvenda.replace('\n', '')
    texthistvenda = texthistvenda.replace('\f', '')
    texthistvenda = texthistvenda.replace(',', '')
    texthistvenda = texthistvenda.replace(' ', '')
    if ((texthistvenda) == ('')):
        texthistvenda = 00
    texthistvenda = int(texthistvenda)

    report.write((itens[i].name) + ';' + str(txtvenda) + ';' + str(txtcompra) + ';' + str(texthistcompra) + ';' + str(texthistvenda) + '\n')

    # -| Impressão do valor de compra |-#
    print("Compra: " + (str(txtcompra)))
    print("Venda: " + (str(txtvenda)))
    print("Estoque: " + (str(textestoque)))
    print("Qtd comprado: " + (str(texthistcompra)))
    print("Qtd vendido: " + (str(texthistvenda)))
    if ((txtvenda)==00 and (txtcompra)==00):
        #print('Oferta situacional!')
        lertela.valvenda = int(txtvenda)-1
        lertela.valcompra = int(txtcompra)+1
        lertela.valestoque = str(txtestoque)
    else:
        #print('A diferença total entre eles é de:', textvenda - textcompra)
        lertela.valvenda = int(txtvenda)
        lertela.valcompra = int(txtcompra)
        lertela.valestoque = str(textestoque)

def comprar():
    i = int(contadorgeral)
    teto = int(itens[i].tetocompra)
    if((lertela.valcompra)<=(teto*10)):
        pyautogui.leftClick(219, 537)
        pyautogui.leftClick(487, 558)
        comprando = str((lertela.valcompra)+1)
        pyautogui.typewrite(''+(comprando), interval=0.05)
        if((lertela.valcompra)<=10000):
            pyautogui.keyDown('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.keyUp('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>10000 and (lertela.valcompra)<=30000):
            pyautogui.keyDown('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(540, 537)
            pyautogui.keyUp('Shift')
            pyautogui.PAUSE = 0.05
            pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>30000 and (lertela.valcompra)<=40000):
             pyautogui.keyDown('Shift')
             pyautogui.PAUSE = 0.05
             pyautogui.leftClick(540, 537)
             pyautogui.keyUp('Shift')
             pyautogui.PAUSE = 0.05
             pyautogui.leftClick(735, 579)
        elif((lertela.valcompra)>40000):
           #pyautogui.leftClick(540, 537)
           pyautogui.leftClick(735, 579)
    elif():
        pass

def vender():
    i = int(contadorgeral)
    teto = int(itens[i].tetovenda)
    if((lertela.valvenda) > (10)):
        pyautogui.leftClick(230, 522)
        pyautogui.leftClick(487, 558)
        vendendo = str((lertela.valvenda) -1)
        pyautogui.typewrite('' + (vendendo), interval=0.05)
        pyautogui.keyDown('Shift')
        pyautogui.keyDown('Ctrl')
        pyautogui.PAUSE = 0.05
        pyautogui.leftClick(545, 534)
        pyautogui.PAUSE = 0.05
        pyautogui.keyUp('Shift')
        pyautogui.keyUp('Ctrl')
        pyautogui.PAUSE = 0.05
        pyautogui.keyUp('Shift')
        pyautogui.leftClick(545, 534)
        pyautogui.leftClick(735, 579)
    else:
        pass


def main():
    checkitem()
    lertela()
    #if((((str(lertela.valestoque)) != '0') and (lertela.valcompra > 45000))):
    #    pass
    #else:
    #    comprar()
    #if(((str(lertela.valestoque)) == '0')):
    #    pass
    #else:
    #    vender()


for i in range(400):
    main()
    contadorgeral = contadorgeral+1
    pyautogui.sleep(2)
    #print('dentro do loop:'+str(contadorgeral))

report.close()