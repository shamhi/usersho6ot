import random


accept = [
    '<emoji id=5375175408012516662>🌟</emoji>',
    '<emoji id=5377370922279779996>🌟</emoji>',
    '<emoji id=5375163072866432989>🌟</emoji>',
    '<emoji id=5377410002187205490>🌟</emoji>',
    '<emoji id=5375087150729540263>🌟</emoji>',
    '<emoji id=5377790166922442009>🌟</emoji>',
    '<emoji id=5377502816430471486>🌟</emoji>',
    '<emoji id=5375367444590247261>🌟</emoji>',
    '<emoji id=5375598221772996400>🌟</emoji>',
    '<emoji id=5375499540604401121>🌟</emoji>',
    '<emoji id=5375395301748127020>🌟</emoji>',
    '<emoji id=5375357841043371164>🌟</emoji>',
    '<emoji id=5377359437537229623>🌟</emoji>',
    '<emoji id=5375053203308035935>🌟</emoji>',
    '<emoji id=5375188696641321716>🌟</emoji>',
    '<emoji id=5375227888217897673>🌟</emoji>',
    '<emoji id=5375565416812789037>✅</emoji>',
    '<emoji id=5375352888946077785>✅</emoji>',
    '<emoji id=5377728778954881693>✅</emoji>',
    '<emoji id=5375172186787035266>✅</emoji>',
    '<emoji id=5375055724453837637>✅</emoji>',
    '<emoji id=5377850429608574168>✅</emoji>',
    '<emoji id=5375247275700271687>✅</emoji>',
    '<emoji id=5375504222118754078>✅</emoji>',
    '<emoji id=5377740826338145943>✅</emoji>',
    '<emoji id=5375374724559813456>✅</emoji>',
    '<emoji id=5377763795823249705>✅</emoji>',
    '<emoji id=5375157360559930462>✅</emoji>',
    '<emoji id=5375450006746577351>✅</emoji>',
    '<emoji id=5377391104331103107>✅</emoji>',
    '<emoji id=5375300314251410685>✅</emoji>',
    '<emoji id=5447447969458566198>✅</emoji>',
]

deny = [

]

nums = {
    0: '<emoji id=5305749482170758709>0️⃣</emoji>',
    1: '<emoji id=5305763715692377402>1️⃣</emoji>',
    2: '<emoji id=5307907239380528763>2️⃣</emoji>',
    3: '<emoji id=5305783000095537258>3️⃣</emoji>',
    4: '<emoji id=5305255243104138538>4️⃣</emoji>',
    5: '<emoji id=5305288155438526869>5️⃣</emoji>',
    6: '<emoji id=5305642863902604489>6️⃣</emoji>',
    7: '<emoji id=5305603955793867793>7️⃣</emoji>',
    8: '<emoji id=5305371288825509083>8️⃣</emoji>',
    9: '<emoji id=5307703499016910744>9️⃣</emoji>',
}


loads = [
    "<emoji id=5307723788442410997>🫥</emoji>"
    "<emoji id=5307750348520168450>🫥</emoji>"
    "<emoji id=5307736638984559509>🫥</emoji>"
    "<emoji id=5308033876491247752>🫥</emoji>"
    "<emoji id=5305683825005700455>🫥</emoji>"
    "<emoji id=5326006107011816493>🫥</emoji>"
    "<emoji id=5307981757063110606>🫥</emoji>"
    "<emoji id=5307780589384900520>🫥</emoji>"
    "<emoji id=5308017534140685461>🫥</emoji>"
    "<emoji id=5323463142775202324>🫠</emoji>"
    "<emoji id=5307581225592954663>🫥</emoji>"
    "<emoji id=5309799327093236710>🫥</emoji>"
    "<emoji id=5309893756244206277>🫥</emoji>"
    "<emoji id=5327902038720257153>🫥</emoji>"
    "<emoji id=5325919653615115810>🫥</emoji>"
    "<emoji id=5332773291843133224>🫥</emoji>"
    "<emoji id=5334530569122358729>🫥</emoji>"
    "<emoji id=5334885140147479028>🫥</emoji>"
    "<emoji id=5325834523068342417>🫥</emoji>"
    "<emoji id=5334904192622403796>🫥</emoji>"
    "<emoji id=5325534794480624559>😵</emoji>"
    "<emoji id=5307646968657356266>‍</emoji>"
    "<emoji id=5327840856911125897>💫</emoji>"
    "<emoji id=5334643333488713810>🫥</emoji>"
]


def rload():
    return random.choice(loads)


def rcheck():
    return random.choice(accept)


def rdeny():
    return random.choice(deny)
