import stddraw

class Body(object):

    # 建立一个新的星球，
    # vector r 用于表示位置
    # vector v 用于表示速度
    # float mass 表示其质量
    def __init__(self, r, v, mass):
        self._r = r 
        self._v = v 
        self._mass = mass


    def Move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + a.scale(dt)
        self._r = self._r + self._v.scale(dt)

    def forceForm(self, other):
        G = 6.67E-11
        delta = other._r - self._r
        dist = abs(delta)
        magitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magitude)

    # 画出该星球
    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])
        
        
        