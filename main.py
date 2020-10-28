import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "SuPyplex"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORAL)
        self.playerList = None
        self.player = None

    def setup(self):
        self.playerList = arcade.SpriteList()
        self.player = arcade.Sprite("assets/Mpx32.bmp")
        self.player.center_x = 0
        self.player.center_x = 0
        self.playerList.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.playerList.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
