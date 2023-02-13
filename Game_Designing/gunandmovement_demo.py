from pyexpat import model
from turtle import position
from black import diff
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform


game_test = Ursina()



Sky()
# for z in range(20):
#     for x in range(20):
#         Entity(
#             model="cube", color=color.dark_gray, collider="box", ignore=True,
#             position = (x, 0, z),
#             parent=scene,
#             orgin_y = 0.5,
#             texture = "white_cube")



ground = Entity(model="plane", texture="grass", collider="mesh", scale=(200, 1, 200))
player = FirstPersonController(position=(0,2,-5))

robo_entity = Entity(model=r'Assets\finnaly_letri.obj', texture=r'Assets\DefaultMaterial_Base_Color.png', scale=5, y=3, x = 2, z=.11)



# weapon = Entity(model=r'Assets\improvedwireframe.obj', parent=camera.ui, scale=5,color=color.gold, texure="white_cube", position=(0.8, -0.6), rotation=(-10,-20,-10))

controller = FirstPersonController()
        

scifi_shotgun = Entity(parent=controller.camera_pivot, scale=4, position=Vec3(0.7,-1,1.5), model=r'Assets\scifi_shotty.obj', texture=r"Assets\shotgun_color.png.png")
controller.speed = 20






    


enemy= FrameAnimation3d('monke_animation/dk', color=color.black, fps=10, scale=1, position=(uniform(-45,45),1,uniform(33,45)))
enObject = Entity(model=r'monke_animation\dk_1.obj', collider='box', parent=enemy,scale=1, position=(0,30,0))




moving_monk = enemy.add_script(SmoothFollow(target=controller, speed=.5))










enemy.look_at(player)







        

class Bullet(Entity):
    def __init__(self, speed=100, lifetime=15, **kwargs):
        super().__init__(**kwargs)
        self.lifetime = lifetime
        self.speed = speed
        self.start = time.time()

    def update(self):
        ray = raycast(self.world_position, self.forward, distance= self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            destroy(self)


def input(key):
    if key == 'left mouse down':
        Bullet(model=r"Assets\10176_Coconut_Whole_v01-it3.obj", texture=r"Assets\Coconut_01.jpg", scale=0.01, position=controller.camera_pivot.world_position, rotation=controller.camera_pivot.world_rotation)


def update():
    
    
    enemy.look_at(controller)



 
game_test.run()