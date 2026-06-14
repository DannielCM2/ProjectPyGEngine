import game
import glfw

from engine import Scene

class DefaultScene(Scene):
    def __init__(self, engine):
        super().__init__(engine=engine)
        self.on_load()

    def on_load(self):
        self.objects.append(game.Cube3D(self.engine.window.ctx))

    def update(self, dt):
        if self.input.was_pressed(glfw.KEY_ESCAPE):
            print("Loading level2")
            return
            self.scene_manager.load_scene('level2')