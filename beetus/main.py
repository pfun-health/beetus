# #
# beetus/main.py : games menu entrypoint
# #

import pyxel

from beetus.games.snake import Snake
from beetus.params import SnakeParams

APP_WIDTH = 160
APP_HEIGHT = 120


class App:
    def __init__(self):
        #: pyxel.init = init(width, height, title=None, fps=None, quit_key=None, display_scale=None, capture_scale=None, capture_sec=None)
        pyxel.init(
            APP_WIDTH, APP_HEIGHT,
            title="Welcome to beetus 🩸. Hope you have a pfun time."
        )
        pyxel.images[0].load(0, 0, "assets/pfun-cutielogo-icon.png")
        self.current_game = None  # State: None for menu, object for current game
        self.snake_params = SnakeParams(width=APP_WIDTH, height=APP_HEIGHT)  # Instantiate default SnakeParams
        pyxel.run(self.update, self.draw)

    def return_to_menu(self):
        """Callback to switch state from game back to menu."""
        self.current_game = None
        pyxel.stop()  # Stop game music/sounds
        self.__init__()  # Re-initialize to show menu

    def update(self):
        if self.current_game:
            # Game is running, delegate update to the current running game instance
            self.current_game.update()
            return
        # Menu update logic
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S):
            # Start the Snake game, passing the callback for when it quits
            self.current_game = Snake(
                params=self.snake_params, on_quit_callback=self.return_to_menu)

    def draw(self):
        if self.current_game:
            # Delegate draw to the running game instance
            self.current_game.draw()
            return

        # Menu draw logic
        pyxel.cls(0)
        # Instructions:
        pyxel.text(55, 41, "Select a game", pyxel.frame_count % 16)
        # Draw the logo sprite below
        #: pyxel.blt = blt(x, y, img, u, v, w, h, colkey=None, rotate=None, scale=None)
        pyxel.blt(x=61, y=66, img=0, u=0, v=0, w=38, h=16)
        # Game options:
        #: pyxel.text = text(x, y, s, col, font=None)
        # dejavu_font = pyxel.Font("/usr/share/fonts/dejavu/DejaVuSerif.ttf")
        pyxel.text(x=60, y=70, s="[S]nake",
                   col=pyxel.frame_count % 16)


App()
