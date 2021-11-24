from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


from .portrayal import portrayCell
from .model import ConwaysGameOfLife


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
RULES = '23/3'

# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, CANVAS_WIDTH, CANVAS_HEIGHT)

model_params = {
    "height": UserSettableParameter("slider", "Grid height", 50, 1, 100),
    "width": UserSettableParameter("slider", "Grid width", 50, 1, 100,),
    "rules": RULES
}

server = ModularServer(
    ConwaysGameOfLife, [canvas_element], "Game of Life", model_params
)
