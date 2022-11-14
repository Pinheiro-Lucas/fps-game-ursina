from dotenv import dotenv_values
from src.client import Server

env = dotenv_values()
server = Server()
respawns = [(-18, -2.5, -1), (61, -5.5, 5), (22, 2, 58),
            (81, 2, 73), (5.5, -2.5, 75), (-23, -2.5, 70),
            (-82, 2, 75), (-82, 1, 9), (-77, -2.5, -19),
            (-27, -2.5, -22), (-31.5, -2.5, 18.5), (75, 2, -70),
            (30, -2.5, -79.5), (-29, 2.5, -78.5), (0.5, -2.5, -35.5)]
hooks = [(3, 4, 3), (14, 4, -26), (63.5, 6, -22.5), (-32, 4, 81),
         (-60.4, 4, -39.5), (-86.5, 6, 26.5), (-83.5, 6, 81),
         (2, 4, 78.5), (53.5, 7.5, 64), (38, 4, -72.5)]
