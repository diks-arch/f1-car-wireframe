from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight, Vec4
import math

class F1CarWireframe(ShowBase):
    def __init__(self):
        super().__init__()

        self.setBackgroundColor(0, 0, 0)
        self.setup_lights()

        self.car = self.render.attachNewNode("F1_Car")

        #MAIN BODY
        self.add_part(0, 0, 0.5, (7, 1.2, 0.4))
        self.add_part(3.5, 0, 0.3, (2.5, 0.6, 0.25))
        self.add_part(-0.5, 0, 1.0, (1.5, 0.8, 0.6))

        #FRONT WING 
        self.add_part(5.5, 0, 0.2, (0.3, 3.5, 0.1))  # main plate

        #supports
        self.add_part(4.8, 0.6, 0.3, (0.2, 0.2, 0.4))
        self.add_part(4.8, -0.6, 0.3, (0.2, 0.2, 0.4))

        #REAR WING
        self.add_part(-3.5, 0, 1.5, (0.3, 2.5, 0.1))
        self.add_part(-3.5, 0, 1.9, (0.3, 2.5, 0.1))

        #pillars
        self.add_part(-3.2, 0.6, 1.2, (0.2, 0.2, 0.6))
        self.add_part(-3.2, -0.6, 1.2, (0.2, 0.2, 0.6))

        #side pods
        self.add_part(0.5, 1.2, 0.6, (2.5, 0.5, 0.3))
        self.add_part(0.5, -1.2, 0.6, (2.5, 0.5, 0.3))

        #Wheels
        wheel_positions = [
            (2.5, 1.5), (2.5, -1.5),
            (-2.5, 1.5), (-2.5, -1.5)
        ]

        for x, y in wheel_positions:
            self.add_wheel(x, y, 0.4)

        #Camera
        self.angle = 0
        self.radius = 30
        self.height = 8

        self.taskMgr.add(self.rotate_camera, "RotateCamera")

    #Parts
    def add_part(self, x, y, z, scale):
        part = self.loader.loadModel("models/misc/rgbCube")
        part.reparentTo(self.car)
        part.setPos(x, y, z)
        part.setScale(scale)
        part.setRenderModeWireframe()
        part.setColor(Vec4(1, 1, 1, 1))

    #Wheels
    def add_wheel(self, x, y, z):
        wheel = self.loader.loadModel("models/misc/sphere")
        wheel.reparentTo(self.car)
        wheel.setScale(0.8)
        wheel.setPos(x, y, z)
        wheel.setRenderModeWireframe()
        wheel.setColor(Vec4(1, 1, 1, 1))

    #Lights
    def setup_lights(self):
        alight = AmbientLight('alight')
        alight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.render.setLight(self.render.attachNewNode(alight))

        dlight = DirectionalLight('dlight')
        dlight.setColor(Vec4(1, 1, 1, 1))
        dlnp = self.render.attachNewNode(dlight)
        dlnp.setHpr(45, -45, 0)
        self.render.setLight(dlnp)

    #Camera rotation
    def rotate_camera(self, task):
        self.angle += 0.01

        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)

        self.camera.setPos(x, y, self.height)
        self.camera.lookAt(0, 0, 0)

        return task.cont


app = F1CarWireframe()
app.run()
