import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import csv
from youtube_data_search import youtube_search

find = youtube_search("Dude Perfect")
for key in find:
    print(key, find[key])

'''
OUTPUT:
('VIEW COUNT', [u'15954753', u'23810456', u'20766368', u'15448489', u'21599317', u'42125026', u'29613139', u'664895', u'101714029', u'20416367', u'25271155', u'33484963', u'41569390', u'50626929', u'88791499', u'21214172', u'105923427', u'16734491', u'81682530', u'51749573', u'83931518', u'35763035', u'35255463', u'161838300', u'82551817'])
('VIDEO ID', [u'wSB9JvsBT4M', u'muzeGsrYpnQ', u'6re9XAwo4b4', u'No8-mBek3rs', u'RohJfM-VFS0', u'DkW87-Z9FAY', u'FepIkIILumA', u'BLRBODK7IwE', u'VRJmcxCrAOA', u'v-dfygYIfLs', u'9m9oO84Q2fk', u'Hk5dxn5dj2M', u'S9KxqRUcnCU', u'th2T6rygqNU', u'VJwoSfTOhyM', u'hYirFqEc8Tg', u'A2FsgKoGD04', u'QU1byle-nmA', u'gm2_6DX_0Bw', u'dlOPwVsI-O4', u'P8V_bx0L4RY', u'qZHycHI3F1Q', u'WpqUOW19aJQ', u'UeG1ftTmLAg', u'ggR_SPwP6cw'])
('LIKE COUNT', [u'436747', u'514213', u'445626', u'388493', u'373970', u'2208654', u'581747', u'22374', u'1845330', u'525143', u'485099', u'528695', u'1211441', u'1218256', u'1034277', u'467664', u'1661262', u'381927', u'1122740', u'354535', u'1208737', u'833794', u'691006', u'4135377', u'933731'])
('VIDEO TITLE', [u'Bowling Trick Shots 2 | Dude Perfect', u'Nerf Blasters Floating Island Battle | Dude Perfect', u'Dirt Bike Battle | Dude Perfect', u'All Sports Golf Battle 3 | Dude Perfect', u'The Net Gun | Overtime Ep. 4 | Dude Perfect', u'Ping Pong Trick Shots 4 | Dude Perfect', u'Fortnite with Ninja | Dude Perfect', u'DUDE PERFECT: FOOTBALL VS SOCCER TRICK SHOTS! BEHIND THE SCENES!', u'Real Life Trick Shots 2 | Dude Perfect', u'Old School Trick Shots | Dude Perfect', u'Giant Darts Battle | Dude Perfect', u'Deep Sea Fishing Battle | Dude Perfect', u'Boomerang Trick Shots | Dude Perfect', u'Giant Sumo Battle | Dude Perfect', u'Water Bottle Flip 2 | Dude Perfect', u'Crossbow Trick Shots | Dude Perfect', u'Real Life Trick Shots | Dude Perfect', u'Go Kart Soccer Battle | Dude Perfect', u'World Record Edition | Dude Perfect', u'Bubble Gum Blowing Battle | Dude Perfect', u'Water Bottle Flip Edition | Dude Perfect', u'Football vs Soccer Trick Shots | Dude Perfect', u'Model Rocket Battle | Dude Perfect', u'Ping Pong Trick Shots 3 | Dude Perfect', u'Beach Stereotypes | Dude Perfect'])
('DISLIKE COUNT', [u'8011', u'18925', u'11636', u'8240', u'12023', u'36931', u'26679', u'227', u'40038', u'12195', u'13111', u'22410', u'22927', u'17279', u'31826', u'10324', u'33185', u'8650', u'27646', u'8644', u'31304', u'14148', u'10203', u'95184', u'34280'])
'''

DudePerfect = pd.DataFrame(find, columns = ["VIDEO TITLE", "VIDEO ID", "VIEW COUNT", "LIKE COUNT", "DISLIKE COUNT"])
DudePerfect.to_csv("YouTube_Search_Results.csv", sep="|")

DudePerfect.head()
'''
OUTPUT:
                                         VIDEO TITLE     VIDEO ID VIEW COUNT  \
0               Bowling Trick Shots 2 | Dude Perfect  wSB9JvsBT4M   15954753
1  Nerf Blasters Floating Island Battle | Dude Pe...  muzeGsrYpnQ   23810456
2                    Dirt Bike Battle | Dude Perfect  6re9XAwo4b4   20766368
3            All Sports Golf Battle 3 | Dude Perfect  No8-mBek3rs   15448489
4        The Net Gun | Overtime Ep. 4 | Dude Perfect  RohJfM-VFS0   21599317

  LIKE COUNT DISLIKE COUNT
0     436747          8011
1     514213         18925
2     445626         11636
3     388493          8240
4     373970         12023
'''

DudePerfect.tail()
'''
OUTPUT:
                                      VIDEO TITLE     VIDEO ID VIEW COUNT  \
20       Water Bottle Flip Edition | Dude Perfect  P8V_bx0L4RY   83931518
21  Football vs Soccer Trick Shots | Dude Perfect  qZHycHI3F1Q   35763035
22             Model Rocket Battle | Dude Perfect  WpqUOW19aJQ   35255463
23         Ping Pong Trick Shots 3 | Dude Perfect  UeG1ftTmLAg  161838300
24               Beach Stereotypes | Dude Perfect  ggR_SPwP6cw   82551817

   LIKE COUNT DISLIKE COUNT
20    1208737         31304
21     833794         14148
22     691006         10203
23    4135377         95184
24     933731         34280

'''

X = range(len(DudePerfect))
X_VIDEO_TITLE = DudePerfect["VIDEO TITLE"]
Y_VIEW_COUNT = DudePerfect["VIEW COUNT"]
Y_LIKE_COUNT = DudePerfect["LIKE COUNT"]

plt.subplot(1, 2, 1)
plt.bar(X, Y_VIEW_COUNT, align = "center", color = "orange")
plt.xticks(X, X_VIDEO_TITLE, rotation=90)
plt.ylabel("Number of Views (in 100 Million)")

plt.subplot(1, 2, 2)
plt.bar(X, Y_LIKE_COUNT, align = "center", color = "green")
plt.xticks(X, X_VIDEO_TITLE, rotation=90)
plt.ylabel("Number of Likes")

plt.show()