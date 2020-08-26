#-----------------------------------------------------------------------
# body.py
#-----------------------------------------------------------------------

import stddraw

class Body:

    # Construct a new Body object whose position is specified by
    # Vector object r, whose velocity is specified by Vector object
    # v, and whose mass is specified by float mass.
    count = 0;

    def __init__(self, r, v, mass):
        self._r = r        # Position
        self._v = v        # Velocity
        self._mass = mass  # Mass
        self._posi=[self._r]
        self._color=stddraw.colors[Body.count%stddraw.colorsn]
        Body.count+=1

    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt.

    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)

    # Return the force between Body objects self and other.

    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draw self to standard draw.

    def draw(self,trackn):
        stddraw.setPenColor(self._color)
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])
        if trackn<1:
            trackn=1
        n=len(self._posi)
        if n<trackn:
            self._posi.append(self._r)
        if len(self._posi)>=trackn:
            del self._posi[0]
        stddraw.setPenRadius(0.0125)
        for i in range(n-1):
            stddraw.line(self._posi[i][0], self._posi[i][1], \
                self._posi[i+1][0], self._posi[i+1][1])
