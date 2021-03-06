from PublicReference.base import *

class 月蚀主动技能(主动技能):
    秒伤基础 = 0
    秒伤成长 = 0
    def 等效CD(self, 武器类型):
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.10, 1)
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.00, 1)

    def 秒伤百分比(self):
        if self.等级 == 0:
            return 0
        else:
            return int((self.秒伤基础 + self.秒伤成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率)

class 月蚀技能0(被动技能):
    名称 = '召唤兽强化'
    所在等级=15
    等级上限=30
    基础等级=20
    关联技能=['契约召唤：桑德尔', '契约召唤：袄索', '精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林', '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯', '契约召唤：路易斯', '精灵召唤：伊伽贝拉', '契约召唤：牛头王库鲁塔', '契约召唤：征服者卡西利亚斯', '咒令：愤怒咆哮', '传说召唤：逆月者拉莫斯','咒令：逆月之蚀' ]
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.0+0.045+0.02*self.等级,3)

class 月蚀技能1(被动技能):
    名称 = '心灵感应'
    所在等级=15
    等级上限=16
    基础等级=6
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.03+0.02*self.等级,3)
   
class 月蚀技能2(月蚀主动技能):
    名称='精灵献祭'
    所在等级=20
    等级上限=60
    基础等级=43  
    基础 = 1903.9803 + 380.9019*8 + 1921.9019 + 1903.9803
    成长 = 215.0196 + 43.0980*8 + 215.0196 + 215.0196
    CD=20.0
    演出时间 = 2
    TP成长=0.05
    TP上限 = 5
    
    
class 月蚀技能3(月蚀主动技能):
    名称='契约召唤：桑德尔'
    所在等级=25
    等级上限=60
    基础等级=41  
    基础=1880.6458
    成长=212.3541
    秒伤基础 = 238.125 + 332.4583/1.5
    秒伤成长 = 26.875 + 37.5416/1.5
    CD=12
    演出时间 = 3.5
    TP成长=0.10
    TP上限 = 5

class 月蚀技能4(月蚀主动技能):
    名称='契约召唤：袄索'
    所在等级=30
    等级上限=60
    基础等级=38
    基础=3099.1556
    成长=349.8444
    秒伤基础 = 87.1555 + 246.2222/3 + 11.7111/5*6 + 620.0222/6
    秒伤成长 = 9.8444 + 27.7777/3 + 0.2888/5*6 + 620.0222/6
    CD=15
    演出时间 = 7.38
    TP成长=0.10
    TP上限 = 5
    
class 月蚀技能5(月蚀主动技能):
    名称='精灵召唤：亡魂默克尔'
    所在等级=30
    等级上限=60
    基础等级=38  
    基础=360.3555*6
    成长=40.6444*6
    秒伤基础 = 107.8222 + 163.5111/1.5 + 102.4222*4/7
    秒伤成长 = 12.1778 + 18.4888/1.5 + 11.5778*4/7
    CD=15
    TP成长=0.10
    TP上限 = 5
    演出时间 = 1.5

class 月蚀技能6(月蚀主动技能):
    名称='精灵召唤：极光格雷林'
    所在等级=30
    等级上限=60
    基础等级=38   
    基础=2160.1778
    成长=243.8222
    秒伤基础 = 23.333*3 + 102.3777/2*5 
    秒伤成长 = 2.666*3 + 11.6222/2*5 
    CD=15
    演出时间 = 3.9
    TP成长=0.10
    TP上限 = 5

class 月蚀技能7(月蚀主动技能):
    名称='精灵召唤：火焰赫瑞克'
    所在等级=30
    等级上限=60
    基础等级=38   
    基础 = 432.2444 + 647.8444 + 863.4444 + 70.9333*3
    成长 = 48.7555 + 73.1555 + 97.5666 + 8.0666*3
    秒伤基础 = 179.6666 + 204.9111/1.5 + 50.2/1.5
    秒伤成长 = 20.3333 + 23.0888/1.5 + 5.8/1.5
    CD=15
    演出时间 = 3.4
    TP成长=0.10
    TP上限 = 5

class 月蚀技能8(月蚀主动技能):
    名称='精灵召唤：冰影阿奎利斯'
    所在等级=30
    等级上限=60
    基础等级=38   
    基础 = 304.888*7
    成长 = 32.5111*7
    秒伤基础 = 22.3777*3 + 208.4888/2 + 231.8888/5*3
    秒伤成长 = 2.622*3 + 23.5111/2 + 26.1111/5*3
    CD=15
    演出时间 = 3.8
    TP成长=0.10
    TP上限 = 5

class 月蚀技能9(月蚀主动技能):
    名称='契约召唤：路易斯'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础 = 661.4047 + 2647.6904
    成长 = 74.5952 + 298.3095
    秒伤基础 = 165.3571 + 109.5714/5*10 + 174.2380/1.5 + 228.1666/1.5
    秒伤成长 = 18.6428 + 12.4285/5*10 + 19.7619/1.5 + 25.8333/1.5
    CD=20
    TP成长=0.10
    TP上限 = 5
    演出时间 = 8.25
    是否有护石=1
    def 装备护石(self):
        self.基础 *= 1.2779
        self.成长 *= 1.2779
        
class 月蚀技能10(月蚀主动技能):
    名称='精灵召唤：伊伽贝拉'
    所在等级=40
    等级上限=60
    基础等级=33   
    基础 = 555.2820*1.3*8
    成长 = 62.7179*1.3*8
    秒伤基础 = 82.5641*1.3/0.6 + 190.3846*1.3/3.1*3 + 415.9230*1.3/5*3 + 646.1025*1.3*4/9.3
    秒伤成长 = 9.4358*1.3/0.6 + 21.6153*1.3/3.1*3 + 26.0769*1.3/5*3 + 72.8974*1.3*4/9.3
    CD=31
    TP成长=0.10
    TP上限 = 5
    演出时间 = 7.7
    是否有护石=1
    def 装备护石(self):
        self.秒伤基础*=0.5618*1.15*2
        self.秒伤成长*=0.5618*1.15*2
        self.基础 *= 1.15
        self.成长 *= 1.15


class 月蚀技能11(月蚀主动技能):
    名称='束缚印记'
    所在等级=45
    等级上限=11
    基础等级=1
    基础=14368.5714
    成长=1622.4285
    CD=25
    
class 月蚀技能12(月蚀主动技能):
    名称='契约召唤：牛头王库鲁塔'
    所在等级=45
    等级上限=60
    基础等级=31 
    基础 = 1568.9189 + 2195.0540 + 2823.2432
    成长 = 177.0810 + 247.9459 + 318.7567
    秒伤基础 = 403.4594 + 651.4594/2 + 1283.1351/3
    秒伤成长 = 45.5404 + 73.5405/2 + 144.8648/3
    CD=40
    演出时间 = 6.85
    TP成长=0.10
    TP上限 = 5
    是否有护石=1
    def 装备护石(self):
        self.秒伤基础*=1.23
        self.秒伤成长*=1.23
        self.基础 *= 1.23
        self.成长 *= 1.23
    
class 月蚀技能13(被动技能):
    名称='强击光环'
    所在等级=48
    等级上限=40
    基础等级=20
    关联技能=['精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林', '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯']
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return 1.15   

class 月蚀技能14(被动技能):
    名称='灵魂支配'
    所在等级=48
    等级上限=40
    基础等级=20
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.105+0.015*self.等级,3)

class 月蚀技能15(月蚀主动技能):
    名称='契约召唤：征服者卡西利亚斯'
    所在等级=50
    等级上限=40
    基础等级=12
    基础 = 6190.6875*1.1426 + 3714.4375*1.1426*5
    成长 = 1869.3125*1.1426 + 1121.5625*1.1426*5
    秒伤基础 = 229.8*1.1426 + 516.2666*1.1426/2 + 1100.6666*1.1426/2
    秒伤成长 = 69.2*1.1426 + 155.7333*1.1426/1.9 + 332.3333*1.1426/2
    CD=200
    演出时间 = 9.1
  

class 月蚀技能16(月蚀主动技能):
    名称 = '精灵召唤：融合精灵海伊轮'
    所在等级 = 60
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (2 + 2*self.等级)

class 月蚀技能17(月蚀主动技能):
    名称='咒令：愤怒咆哮'
    所在等级=70
    等级上限=40
    基础等级=18   
    基础 = 3945.5*4 + 10522
    成长 = 445.5*4 + 1188
    CD=50
    TP成长=0.10
    TP上限 = 5
    演出时间 = 2
    是否有护石=1
    def 装备护石(self):
        self.倍率*=1.124

class 月蚀技能18(被动技能):
    名称='蚀月附灵'
    所在等级=75
    等级上限=40
    基础等级=11
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级,3)
    冷却关联技能=['契约召唤：桑德尔', '契约召唤：袄索', '精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林',  '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯', '契约召唤：路易斯', '精灵召唤：伊伽贝拉', '契约召唤：牛头王库鲁塔', '契约召唤：征服者卡西利亚斯', '咒令：愤怒咆哮', '传说召唤：逆月者拉莫斯','咒令：逆月之蚀' ]
    def CD缩减倍率(self, 武器类型):
        return 0.8


class 月蚀技能19(月蚀主动技能):
    名称='传说召唤：月蚀之影'
    所在等级=80
    等级上限=40
    基础等级=13   
    基础 = 3783.6154
    成长 = 432.3846
    攻击次数 = 15.0
    演出时间 = 3
    CD=43

class 月蚀技能20(月蚀主动技能):
    名称='传说召唤：逆月者拉莫斯'
    所在等级=85
    等级上限=40
    基础等级=5
    基础 = 1992.4*1.15*3
    成长 = 601.6*1.15*3
    秒伤基础 = 717.6*1.15/3*2 + 192.4*1.15/3 + 335*1.15/3 + 430*1.15/3 + 238.8*1.15/6 + 837.4*1.15/6
    秒伤成长 = 216.4*1.15/3*2 + 57.6*1.15/3 + 101*1.15/3 + 130*1.15/3 + 72.2*1.15/6 + 252.6*1.15/6
    演出时间 = 4.5
    CD=10

class 月蚀技能21(月蚀主动技能):
    名称='咒令：逆月之蚀'
    所在等级=85
    等级上限=40
    基础等级=5
    基础 = 4782.4*1.15 + 1912.5*1.15*5 + 2733.2*1.15*8 + 14346*1.15
    成长 = 1443.7*1.15 + 577.7*1.15*5 + 824.9*1.15*8 + 4332*1.15
    演出时间 = 5
    CD=180


class 月蚀技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 月蚀技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 月蚀技能24(被动技能):
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

class 月蚀技能25(被动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    是否主动 = 1
    关联技能 = ['无']
    冷却关联技能=['契约召唤：征服者卡西利亚斯', '咒令：愤怒咆哮', '精灵献祭','咒令：逆月之蚀' ]
    def CD缩减倍率(self, 武器类型):
        return round(1 - 0.0216 * self.等级 , 3)

class 月蚀技能26(月蚀主动技能):
    名称='鞭挞'
    所在等级=10
    等级上限=60
    基础等级=32  
    基础 = 37.4 + 55.575
    成长 = 137.6 + 206.425
    CD=1
    TP成长=0.05
    TP上限 = 5

class 月蚀技能27(月蚀主动技能):
    名称='魔力印记'
    备注='(秒伤)'
    所在等级=25
    等级上限=11
    基础等级=1  
    基础 = 322
    成长 = 61
    攻击次数 = 2
    演出时间 = 1
    def 等效CD(self, 武器类型):
        return 1

class 月蚀技能28(月蚀主动技能):
    名称='驱散魔法'
    所在等级=10
    等级上限=20
    基础等级=10
    是否有伤害 = 0

    def 智力加成(self):
        if self.等级 == 0:
            return 0
        else:
            return -38 * 4 + self.等级 * 9 * 4

月蚀技能列表 = []
i = 0
while i >= 0:
    try:
        exec('月蚀技能列表.append(月蚀技能'+str(i)+'())')
        i += 1
    except:
        i = -1

月蚀技能序号 = dict()
for i in range(len(月蚀技能列表)):
    月蚀技能序号[月蚀技能列表[i].名称] = i

月蚀一觉序号 = 0
月蚀二觉序号 = 0
月蚀三觉序号 = 0
for i in 月蚀技能列表:
    if i.所在等级 == 50:
        月蚀一觉序号 = 月蚀技能序号[i.名称]
    if i.所在等级 == 85:
        月蚀二觉序号 = 月蚀技能序号[i.名称]
    if i.所在等级 == 100:
        月蚀三觉序号 = 月蚀技能序号[i.名称]

月蚀护石选项 = ['无']
for i in 月蚀技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        月蚀护石选项.append(i.名称)

月蚀符文选项 = ['无']
for i in 月蚀技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        月蚀符文选项.append(i.名称)

class 月蚀角色属性(角色属性):

    职业名称 = '月蚀'

    武器选项 = ['法杖', '魔杖']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.790
   
    #基础属性(含唤醒)
    基础力量 = 807.0
    基础智力 = 952.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0
    秒伤比率 = 1
  
    def __init__(self):
        self.技能栏= deepcopy(月蚀技能列表)
        self.技能序号= deepcopy(月蚀技能序号)
    
    def 伤害计算(self, x = 0):
        
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)

        #召唤物秒伤
        for i in self.技能栏:
            if i.是否有伤害==1 and i.是否主动 == 1:
                技能总伤害[self.技能序号[i.名称]] += self.秒伤比率 * i.秒伤百分比() * (self.时间输入 - i.演出时间 * 技能释放次数[self.技能序号[i.名称]]) * self.伤害指数 * i.被动倍率 * (1+self.白兔子技能*0.20+self.年宠技能*0.10*(10 / (self.时间输入 % 50))+self.斗神之吼秘药*0.12)

        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据
    
        if  self.技能栏[self.技能序号['觉醒之抉择']].关联技能 == ['契约召唤：征服者卡西利亚斯']:
            self.技能栏[self.技能序号['契约召唤：征服者卡西利亚斯']].秒伤基础 /=self.技能栏[self.技能序号['觉醒之抉择']].加成倍率(self.武器类型)
            self.技能栏[self.技能序号['契约召唤：征服者卡西利亚斯']].秒伤成长 /=self.技能栏[self.技能序号['觉醒之抉择']].加成倍率(self.武器类型)
  
    def 伤害指数计算(self):
        self.冰属性强化 += self.技能栏[self.技能序号['精灵召唤：融合精灵海伊轮']].属强加成()
        self.光属性强化 += self.技能栏[self.技能序号['精灵召唤：融合精灵海伊轮']].属强加成()
        self.火属性强化 += self.技能栏[self.技能序号['精灵召唤：融合精灵海伊轮']].属强加成()
        self.暗属性强化 += self.技能栏[self.技能序号['精灵召唤：融合精灵海伊轮']].属强加成()
        self.进图智力 += self.技能栏[self.技能序号['驱散魔法']].智力加成()
        super().伤害指数计算()

class 月蚀(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 月蚀角色属性()
        self.角色属性A = 月蚀角色属性()
        self.角色属性B = 月蚀角色属性()
        self.一觉序号 = 月蚀一觉序号
        self.二觉序号 = 月蚀二觉序号
        self.三觉序号 = 月蚀三觉序号
        self.护石选项 = deepcopy(月蚀护石选项)
        self.符文选项 = deepcopy(月蚀符文选项)

    def 界面(self):
        super().界面()

        self.秒伤比率=MyQComboBox(self.main_frame2)
        for i in range(9):
            self.秒伤比率.addItem('AI期望：' + str(80 + i * 5) + '%')
        self.秒伤比率.setCurrentIndex(4)
        self.秒伤比率.resize(120,20)
        self.秒伤比率.move(315,480)
        self.秒伤比率.setToolTip('AI期望为各召唤兽各技能百分比/CD总和\n\n各召唤兽AI输出时间单独计算\n\n时间输入 - 附灵演出时间 * 附灵次数')

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性)
        属性.秒伤比率 = 0.8 + self.秒伤比率.currentIndex() * 0.05
