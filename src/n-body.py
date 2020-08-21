import pygame

global G, PI
G = 6.754*0.00001
PI = 3.14159265358979323


class System(object):
    name = ""
    objects = []

    def __init__(self, name):
        self.name = name

    def add_object(self, obj):
        self.objects.append(obj)

    def work_power(self):
        for obj in self.objects:
            obj.power = []
            if obj.speed == [0, 0]:
                pass
            else:
                obj.speed[0] = obj.speed[0] * obj.mass
                obj.speed[1] = obj.speed[1] * obj.mass
                obj.power.append(obj.speed)
            for o in self.objects:
                v0 = o.position[0] - obj.position[0]
                v1 = o.position[1] - obj.position[1]
                distance_2 = v0 ** 2 + v1 ** 2
                if distance_2 == 0:
                    pass
                else:
                    v0 *= G/distance_2*(obj.mass*o.mass)
                    v1 *= G/distance_2*(obj.mass*o.mass)
                    obj.power.append([v0, v1])

    def work_force(self):
        for obj in self.objects:
            for n in range(len(obj.power) - 1):
                f1 = obj.power[0]
                f2 = obj.power[1]
                f_t = [f1[0]+f2[0], f1[1]+f2[1]]
                del obj.power[0]
                del obj.power[0]
                obj.power.append(f_t)
            obj.position[0] += obj.power[0][0]/obj.mass
            obj.position[1] += obj.power[0][1]/obj.mass
            obj.speed = [obj.power[0][0]/obj.mass, obj.power[0][1]/obj.mass]
            # print(obj.speed)

    def display(self, scr, show_orbit, length=500):
        for obj in self.objects:
            pygame.draw.circle(scr, obj.color, (int(obj.position[0]), int(obj.position[1])), obj.volume)
            if show_orbit:
                obj.positions = obj.positions[:]
                obj.positions.insert(0, [int(obj.position[0]), int(obj.position[1])])
                pygame.draw.aalines(scr, obj.color, False, obj.positions, 3)
                if len(obj.positions) > length:
                    del obj.positions[-1]
                elif len(obj.positions) > len(self.objects):
                    if obj.position_ in obj.positions:
                        for n in range(len(self.objects)):
                            del obj.positions[-1]

    def display_data(self, scr, c):
        font = pygame.font.SysFont("Consolas", 25)
        fps = font.render("FPS: "+str(round(c.get_fps(), 2)), False, (255, 255, 255))
        scr.blit(fps, (50, 50))
        if self.objects:
            for index, obj in enumerate(self.objects):
                pos = font.render(obj.name+": "+str(int(obj.position[0])) + "  " +
                                  str(int(obj.position[1])), False, (255, 255, 255))
                scr.blit(pos, (50, 80+index*35))


class Objects(object):
    mass = 0       
    power = []      
    speed = []      
    position = []   
    position_ = []  
    move_to = []    
    positions = [] 
    volume = 0      
    color = []      
    name = ""       

    def __init__(self, name, mass, speed, position, volume, color):
        self.mass = mass
        self.position = position
        self.volume = volume
        self.speed = speed
        self.color = color
        self.name = name
        self.positions.append(position[:])
        self.position_ = position[:]


universe = System("Earth University")

earth = Objects("Earth", 1000, [0, 0], [200, 200], 5, [115, 15, 249])
sun = Objects("Sun", 1000, [0, 0], [500, 600], 5, [255, 0, 0])
moon = Objects("Moon", 1000, [0, 0], [500, 300], 5, [0, 255, 0])
mars = Objects("Mars", 1000, [0, 0], [600, 400], 5, [15, 215, 249])

universe.add_object(earth)
universe.add_object(sun)
universe.add_object(moon)
universe.add_object(mars)

universe.work_power()
universe.work_force()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1500, 1200])
pygame.display.set_caption("Force")

keep = True

while keep:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep = False

    screen.fill((0, 0, 0))

    universe.work_power()
    universe.work_force()
    universe.display(screen, True)
    universe.display_data(screen, clock)

    pygame.display.update()
    clock.tick(200)

pygame.quit()


