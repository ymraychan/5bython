from block import Block
from get_levels import *
import pygame
from entity.entity import Entity
from entity.character import Character
from entity.moving_entity import MovingEntity
from properties import block_properties
from typing import Final

class Level:
    lvl_id: int
    blocks: list[list[Block]]
    border_img: list[pygame.Surface] = [pygame.image.load(f"visuals/borders/tb{_:04d}.png") for _ in range(38)]
    bg_surf: pygame.Surface
    text_surf: pygame.Surface
    static_block_surf: pygame.Surface
    camera_x: float
    camera_y: float
    entities: list[Entity]
    restart_countdown: int
    num_deaths: Final[int]

    def draw_static_blocks(self, surf: pygame.Surface) -> None:
        for _ in self.blocks:
            for tile in _:
                if tile:
                    if tile.info[16] == 1 and tile.id != 6:
                        tile.draw(surf)

    def draw_borders(self, surf: pygame.Surface) -> None:
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[0])):
                this_tile = self.blocks[i][j]
                
                if not (this_tile and this_tile.info and this_tile.info[13]):
                    continue
                    
                def isEmpty(ni, nj):
                    if 0 <= ni < len(self.blocks) and 0 <= nj < len(self.blocks[0]):
                        neighbor = self.blocks[ni][nj]
                        return not (neighbor and neighbor.info and neighbor.info[13])
                    return False

                leftEmpty = isEmpty(i, j - 1)
                rightEmpty = isEmpty(i, j + 1)
                bottomEmpty = isEmpty(i + 1, j)
                topEmpty = isEmpty(i - 1, j)
                score = 0
                if rightEmpty: score += 1
                if leftEmpty: score += 2
                if bottomEmpty: score += 4
                if topEmpty: score += 8

                if score > 0:
                    surf.blit(self.border_img[score - 1], (j * 30, i * 30))
                    
                if not topEmpty and not leftEmpty and isEmpty(i - 1, j - 1):
                    surf.blit(self.border_img[34], (j * 30, i * 30))
                if not topEmpty and not rightEmpty and isEmpty(i - 1, j + 1):
                    surf.blit(self.border_img[35], (j * 30, i * 30))
                if not bottomEmpty and not rightEmpty and isEmpty(i + 1, j + 1):
                    surf.blit(self.border_img[36], (j * 30, i * 30))
                if not bottomEmpty and not leftEmpty and isEmpty(i + 1, j - 1):
                    surf.blit(self.border_img[37], (j * 30, i * 30))

    def load_entities(self) -> list[Entity]:
        raw: list[tuple[int, float, float, int] | tuple[int, float, float, int, str]] = get_entity_dat(self.lvl_id)
        listEntities: list[Entity] = []
        for entity in raw:
            match entity:
                case (id, x, y, state):
                    e = Character(id, x, y, state, self.lvl_id, self.blocks)
                case (id, x, y, state, movementStr):
                    e = MovingEntity(id, x, y, state, movementStr)
            
            listEntities.append(e)
        return listEntities

    def load_blocks(self) -> list[list[Block]]:
        blocks: list[list[Block]] = []
        for _ in range(get_level_height(self.lvl_id)):
            blocks.append([Block(0, 0, 0, name=".")] * get_level_width(self.lvl_id))
        l = get_level_blocks(self.lvl_id)
        for i in range(get_level_height(self.lvl_id)):
            if get_level_block_mode(self.lvl_id) == "L":
                for j in range(get_level_width(self.lvl_id)):
                    x = j*30
                    y = i*30

                    blocks[i][j] = Block(level=self.lvl_id, name=l[i][j], x=x, y=y)
            else:
                for j in range(get_level_width(self.lvl_id)):
                    x = j*30
                    y = i*30

                    blocks[i][j] = Block(level=self.lvl_id, name=f"{l[i][j*2]}{l[i][j*2+1]}", x=x, y=y)
        return blocks

    def __init__(self, lvl_id: int) -> None:
        self.lvl_id = lvl_id
        self.blocks = self.load_blocks()
        self.entities = self.load_entities()
        self.static_block_surf = pygame.Surface((get_level_width(lvl_id)*30, get_level_height(lvl_id)*30), pygame.SRCALPHA)
        self.draw_static_blocks(self.static_block_surf)
        self.draw_borders(self.static_block_surf)
        self.camera_x = 0 # TODO: Implement camera
        self.camera_y = 0 # TODO: Implement camera
        self.bg_surf = pygame.transform.scale(pygame.image.load(f"visuals/bg/bg{get_level_bg_id(lvl_id):04d}.png"), (960, 540)).convert()
        self.text_surf = pygame.font.Font("fonts/helveticabold.ttf", 32).render(f"{lvl_id+1:03d}. {get_level_name(lvl_id)}", True, (255, 255, 255)).convert_alpha()
        self.num_deaths = get_necessary_deaths(lvl_id)
        self.restart_countdown = -1

    def draw_bg(self, surf: pygame.Surface) -> None:
        surf.blit(self.bg_surf, (0, 0))

    def draw_blocks(self, surf: pygame.Surface) -> None:
        surf.blit(self.static_block_surf, (self.camera_x, self.camera_y))
        for _ in self.blocks:
            for tile in _:
                if tile:
                    if tile.info[16] > 1 or tile.id == 6:
                        tile.draw(surf)



    def draw_entities(self, surf: pygame.Surface) -> None:
        for entity in self.entities:
            entity.draw(surf)

    def draw_level_text(self, surf: pygame.Surface) -> None:
        surf.blit(self.text_surf, (12.85, 495.45))
    
    def draw(self, screen: pygame.Surface) -> None:
        self.draw_bg(screen)
        self.draw_blocks(screen)
        self.draw_entities(screen)
        self.draw_level_text(screen)

    def update_anim_blocks(self, surf: pygame.Surface) -> None:
        for _ in self.blocks:
            for b in _:
                if b:
                    b.add_frame()

    def possibly_restart(self, surf: pygame.Surface, keysInstant: list[pygame.event.Event]):
        for key in keysInstant:
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_r:
                    self.restart_countdown = 10
        if self.restart_countdown == 0:
            self.__init__(self.lvl_id)
        if self.restart_countdown > 0:
            self.restart_countdown -= 1 
        else:
            self.restart_countdown = -1
        # TODO: Add the screen shake and white alpha effect.

    def update_entities(self, surf: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        for entity in self.entities:
            entity.update(surf, keysPressed, keysInstant)

    def update(self, screen: pygame.Surface, keysPressed: pygame.key.ScancodeWrapper, keysInstant: list[pygame.event.Event]) -> None:
        self.update_anim_blocks(screen)
        self.update_entities(screen, keysPressed, keysInstant)
        self.possibly_restart(screen, keysInstant)
