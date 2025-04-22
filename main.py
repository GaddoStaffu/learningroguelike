import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    event_handler = EventHandler()
    with tcod.context.new(
        width=screen_width,
        height=screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                
                action = event_handler.dispatch(event)
                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    dx, dy = action.dx, action.dy
                    player_x += dx
                    player_y += dy
                
                elif isinstance(action, EscapeAction):
                    raise SystemExit()
                
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()