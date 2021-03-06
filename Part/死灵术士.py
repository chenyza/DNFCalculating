from PublicReference.base import *

class 死灵术士主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '匕首':
            return round(self.CD / self.恢复 * 0.95, 1)
        if 武器类型 == '手杖':
            return round(self.CD / self.恢复 * 1.1, 1)

class 死灵术士技能0(死灵术士主动技能):
    名称 = '暗魂波'#蓄力
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 1263.903061
    成长 = 131.9969388
    CD = 3.5

class 死灵术士技能1(死灵术士主动技能):
    名称 = '暗魂波（强化版）'#蓄力
    所在等级 = 5
    等级上限 = 1
    基础等级 = 1
    基础 = 936.2244898
    成长 = 97.7755102
    CD = 3.5
    TP成长 = 0.16
    TP上限 = 5


class 死灵术士技能2(死灵术士主动技能):
    名称 = '诅咒之剑'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1707.222222
    成长 = 192.7777778
    CD = 10
    TP成长 = 0.24
    TP上限 = 5


class 死灵术士技能3(死灵术士主动技能):
    名称 = '降临：尼古拉斯（蜘蛛团）'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 377.2444444
    成长 = 42.75555556
    CD = 1
    TP成长 = 0.10
    TP上限 = 5

class 死灵术士技能4(死灵术士主动技能):
    名称 = '降临：尼古拉斯（艾克洛索）'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 745.2444444
    成长 = 85.75555556
    CD = 1
    TP成长 = 0.10



class 死灵术士技能5(死灵术士主动技能):
    名称 = '驱使僵尸（自爆）'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1811.071429
    成长 = 203.9285714
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class 死灵术士技能6(死灵术士主动技能):
    名称 = '服从（远程）'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['降临：尼古拉斯（蜘蛛团）', '降临：尼古拉斯（艾克洛索）']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.04 * self.等级, 5)


class 死灵术士技能7(被动技能):
    名称 = '黑暗之环'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (48 + self.等级 * 3)

    def 加成倍率(self, 武器类型):
        return 1.0


class 死灵术士技能8(死灵术士主动技能):
    名称 = '暗影蜘蛛阵'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4868.275
    成长 = 546.725
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 死灵术士技能9(死灵术士主动技能):
    名称 = '死亡之爪'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2304.725
    成长 = 260.275
    CD = 7
    TP成长 = 0.10
    TP上限 = 5


class 死灵术士技能10(死灵术士主动技能):
    名称 = '死灵之怨'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3118.945946
    成长 = 352.0540541
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


class 死灵术士技能11(死灵术士主动技能):
    名称 = '百鬼夜行'#自爆
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3956.627027
    成长 = 444.972973
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


class 死灵术士技能12(被动技能):
    名称 = '黑魔法书：亡者之魂'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 1
    关联技能 = ['百鬼夜行']
    关联技能2 = ['驱使僵尸（自爆）']
    关联技能3 = ['死灵之怨']
    关联技能4 = ['降临：僵尸莱迪娅']
    关联技能5 = ['死灵之缚']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.03 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.06 * self.等级, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.01 * self.等级, 5)

    def 加成倍率4(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

    def 加成倍率5(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 2:
                return round(1.2 + 0.01, 5)
            else:
                return round(1.21 + 0.01 * (self.等级 - 2), 5)

class 死灵术士技能13(死灵术士主动技能):
    名称 = '降临：暴君巴拉克（一轮平x）'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 3037.428571/1.02
    成长 = 160.5714286/1.02
    CD = 1
    TP成长 = 0.1
    TP上限 = 5

class 死灵术士技能14(死灵术士主动技能):
    名称 = '降临：暴君巴拉克（2下平x+黑手）'
    所在等级 = 35
    等级上限 = 1
    基础等级 = 1
    基础 = 3272.914286/1.02
    成长 = 173.0857143/1.02
    CD = 1
    TP成长 = 0.1

class 死灵术士技能15(死灵术士主动技能):
    名称 = '降临：暴君巴拉克（暗击拳爆炸）'
    所在等级 = 35
    等级上限 = 1
    基础等级 = 1
    基础 = 1515.057143/1.035
    成长 = 79.94285714/1.035
    CD = 3.0
    TP成长 = 0.1

class 死灵术士技能16(死灵术士主动技能):
    名称 = '降临：暴君巴拉克（强击）'
    所在等级 = 35
    等级上限 = 1
    基础等级 = 1
    基础 = 2788.485714/1.035
    成长 = 147.5142857/1.035
    CD = 2.0
    TP成长 = 0.1

class 死灵术士技能17(死灵术士主动技能):
    名称 = '降临：暴君巴拉克（杀戮乱舞）'
    所在等级 = 35
    等级上限 = 1
    基础等级 = 1
    基础 = 3829.542857/1.035
    成长 = 202.4571429/1.0351
    CD = 7.0
    TP成长 = 0.1
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 2

class 死灵术士技能18(死灵术士主动技能):
    名称 = '吸魂暗劲波'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7755.34375
    成长 = 875.65625
    CD = 35
    TP成长 = 0.1
    TP上限 = 5

class 死灵术士技能19(死灵术士主动技能):
    名称 = '巴拉克的野心'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8517.34375
    成长 = 961.65625
    CD = 25
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 0.94

class 死灵术士技能20(被动技能):
    名称 = '巴拉克的盟约'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['暗魂波', '暗魂波（强化版）', '诅咒之剑', '降临：尼古拉斯（蜘蛛团）', '降临：尼古拉斯（艾克洛索）', '驱使僵尸（自爆）', '暗影蜘蛛阵', '死亡之爪', '死灵之怨', '百鬼夜行',
            '吸魂暗劲波', '巴拉克的野心', '降临：僵尸莱迪娅', '巴拉克的愤怒', '千魂祭', '死灵之缚', '释魂暗劲波', '暗黑蜘蛛引', '暴君极刑斩', '亡者君临：巴拉克之戮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.38 + 0.02 * self.等级, 5)


class 死灵术士技能21(死灵术士主动技能):
    名称 = '降临：僵尸莱迪娅'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15002
    成长 = 1690
    CD = 45
    TP成长 = 0.1
    TP上限 = 5

class 死灵术士技能22(死灵术士主动技能):
    名称 = '巴拉克的愤怒'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 14458.4
    成长 = 1632.6
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.17
        self.CD *= 0.89

class 死灵术士技能23(被动技能):
    名称 = '屠戮之惧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 死灵术士技能24(死灵术士主动技能):
    名称 = '千魂祭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 33258.42857
    成长 = 10047.71429
    CD = 145

class 死灵术士技能25(死灵术士主动技能):
    名称 = '死灵之缚'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 11823.63636
    成长 = 1336.363636
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.29

class 死灵术士技能26(死灵术士主动技能):
    名称 = '释魂暗劲波'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 16670.94118
    成长 = 1882.058824
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 0.9

class 死灵术士技能27(死灵术士主动技能):
    名称 = '暗黑蜘蛛引'#一部分伤害分给尼古拉斯了，约2.32765倍
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 16272.8
    成长 = 1838.2
    CD = 20

class 死灵术士技能28(被动技能):
    名称 = '亡魂之息'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['降临：尼古拉斯（蜘蛛团）', '降临：尼古拉斯（艾克洛索）', '驱使僵尸（自爆）', '暗影蜘蛛阵', '死亡之爪', '死灵之怨', '百鬼夜行', '降临：暴君巴拉克（一轮平x）',
            '降临：暴君巴拉克（2下平x+黑手）', '降临：暴君巴拉克（暗击拳爆炸）', '降临：暴君巴拉克（强击）', '降临：暴君巴拉克（杀戮乱舞）', '吸魂暗劲波', '巴拉克的野心', '降临：僵尸莱迪娅',
            '巴拉克的愤怒', '千魂祭', '死灵之缚', '释魂暗劲波', '暗黑蜘蛛引', '暴君极刑斩', '亡者君临：巴拉克之戮']
    关联技能2 = ['暗魂波', '暗魂波（强化版）', '诅咒之剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.6 + 0.02 * self.等级, 5)

class 死灵术士技能29(死灵术士主动技能):
    名称 = '暴君极刑斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 39040.16667
    成长 = 4407.833333
    CD = 45

class 死灵术士技能30(死灵术士主动技能):
    名称 = '亡者君临：巴拉克之戮'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 70680
    成长 = 21347.6
    CD = 180

class 死灵术士技能31(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 死灵术士技能32(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 死灵术士技能33(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


死灵术士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('死灵术士技能列表.append(死灵术士技能' + str(i) + '())')
        i += 1
    except:
        i = -1

死灵术士技能序号 = dict()
for i in range(len(死灵术士技能列表)):
    死灵术士技能序号[死灵术士技能列表[i].名称] = i

死灵术士一觉序号 = 0
死灵术士二觉序号 = 0
死灵术士三觉序号 = 0
for i in 死灵术士技能列表:
    if i.所在等级 == 50:
        死灵术士一觉序号 = 死灵术士技能序号[i.名称]
    if i.所在等级 == 85:
        死灵术士二觉序号 = 死灵术士技能序号[i.名称]
    if i.所在等级 == 100:
        死灵术士三觉序号 = 死灵术士技能序号[i.名称]

死灵术士护石选项 = ['无']
for i in 死灵术士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        死灵术士护石选项.append(i.名称)

死灵术士符文选项 = ['无']
for i in 死灵术士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        死灵术士符文选项.append(i.名称)


class 死灵术士角色属性(角色属性):
    职业名称 = '死灵术士'

    武器选项 = ['匕首', '手杖']

    # '物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']

    # 默认
    伤害类型 = '魔法百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['智力']

    主BUFF = 2.14

    # 基础属性(含唤醒)
    基础力量 = 901.0
    基础智力 = 951.0

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0


    def __init__(self):
        self.技能栏 = deepcopy(死灵术士技能列表)
        self.技能序号 = deepcopy(死灵术士技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        
        self.技能栏[1].等级 = self.技能栏[0].等级

        self.技能栏[4].等级 = self.技能栏[3].等级
        self.技能栏[4].TP等级 = self.技能栏[3].TP等级

        for i in [14, 15, 16, 17]:
            self.技能栏[i].等级 = self.技能栏[13].等级
            self.技能栏[i].TP等级 = self.技能栏[13].TP等级

        for j in self.技能栏[self.技能序号['黑魔法书：亡者之魂']].关联技能4:
            self.技能栏[self.技能序号[j]].被动倍率 *= self.技能栏[self.技能序号['黑魔法书：亡者之魂']].加成倍率4(self.武器类型)
        for j in self.技能栏[self.技能序号['黑魔法书：亡者之魂']].关联技能5:
            self.技能栏[self.技能序号[j]].被动倍率 *= self.技能栏[self.技能序号['黑魔法书：亡者之魂']].加成倍率5(self.武器类型)

    def 伤害指数计算(self):
        self.暗属性强化 += self.技能栏[self.技能序号['黑暗之环']].属强加成()
        super().伤害指数计算()

    def 暗属性强化加成(self):
        暗属性强化值 = 0
        for i in self.技能栏:
            if i.名称 != '黑暗之环':
                暗属性强化值 += 0
            else:
                暗属性强化值 += i.属强加成()
        return (暗属性强化值)


class 死灵术士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 死灵术士角色属性()
        self.角色属性A = 死灵术士角色属性()
        self.角色属性B = 死灵术士角色属性()
        self.一觉序号 = 死灵术士一觉序号
        self.二觉序号 = 死灵术士二觉序号
        self.三觉序号 = 死灵术士三觉序号
        self.护石选项 = deepcopy(死灵术士护石选项)
        self.符文选项 = deepcopy(死灵术士符文选项)


    def 站街计算(self, 装备名称, 套装名称):
        C = deepcopy(self.角色属性A)
        C.技能栏 = deepcopy(self.角色属性A.技能栏)
        C.穿戴装备(装备名称, 套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
        C.装备基础()

        C.暗属性强化 += C.暗属性强化加成()

        return C
