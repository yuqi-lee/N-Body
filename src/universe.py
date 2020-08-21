#-*- coding: UTF-8 -*-


# -----------------------------------------------------------------------
# universe.py
# -----------------------------------------------------------------------



import sys
import stdarray
import stddraw
from body import Body
from instream import InStream
from vector import Vector


# -----------------------------------------------------------------------

class Universe:

    # 读取文件数据，建立一个新的宇宙对象

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)

    # Simulate the passing of dt seconds in self.

    def increaseTime(self, dt):

        # Initialize the forces to zero.
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))

        # Compute the forces.
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]
                    f[i] = f[i] + bodyi.forceFrom(bodyj)

        # 移动星球
        for i in range(n):
            self._bodies[i].move(f[i], dt)

            # 画出自己

    def draw(self):
        for body in self._bodies:
            body.draw()


# -----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.

def main():
    filename = '4body.txt'
    dt = float(20000)
    #filename = sys.argv[1]
    #dt = float(sys.argv[2])
    universe = Universe(filename)
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python universe.py 2bodyTiny.txt 20000

# python universe.py 2body.txt 20000

# python universe.py 3body.txt 20000

# python universe.py 4body.txt 20000
