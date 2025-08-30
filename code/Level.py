from xml.dom.minidom import Entity

import pygame

from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name # Nome do level "Level 1"
        self.game_mode = game_mode # Modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()


        pass
