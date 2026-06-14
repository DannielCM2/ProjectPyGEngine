from engine.game import Game
from game import scenes

def start_game():
    game = Game()

    game.scene_manager.cache_scene('default', scenes.DefaultScene)

    game.scene_manager.load_scene("default")

    game.run()