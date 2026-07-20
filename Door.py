from pgzero.rect import Rect
from block import Block
import properties
from typing import Final

class Door(Block):
    doorLightX: Final[list[list[int]]] = properties.doorLightX
    doorLightFade: list[float]
    doorLightFadeDire: list[int]

    def map_range(self, value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> int:
        return int(out_min + (float(value - in_min) / float(in_max - in_min) * (out_max - out_min)))

    def __init__(self, frame: int = 0, x: int = 0, y: int = 0) -> None:
        super().__init__(block_id=6, name=None, frame=frame, x=x, y=y)
        
        self.doorLightFade = [0.0] * 30
        self.doorLightFadeDire = [0] * 30
        
    def draw(self, screen) -> None:
        door_rect = Rect((self.x - 30), (self.y - 90), 60, 120)
        screen.draw.filled_rect(door_rect, (80, 80, 80))
        
        charCount2 = 1
        
        for i in range(charCount2):
            r = self.map_range(self.doorLightFade[i], 0, 1, 40, 0)
            g = self.map_range(self.doorLightFade[i], 0, 1, 40, 255)
            b = self.map_range(self.doorLightFade[i], 0, 1, 40, 0)
            
            current_row = i // 6
            last_row = (charCount2 - 1) // 6
            
            row_idx = (charCount2 - 1) % 6 if current_row == last_row else 5
            col_idx = i % 6
            
            light_x = (self.x - 30) + self.doorLightX[row_idx][col_idx]
            light_y = self.y - 80 + (current_row * 10)
            
            screen.draw.filled_rect(Rect(light_x, light_y, 5, 5), (r, g, b))
            
            if self.doorLightFadeDire[i] != 0:
                self.doorLightFade[i] += self.doorLightFadeDire[i] * 0.0625
                self.doorLightFade[i] = max(0.0, min(1.0, self.doorLightFade[i]))
                
                if self.doorLightFade[i] == 1.0 or self.doorLightFade[i] == 0.0:
                    self.doorLightFadeDire[i] = 0
