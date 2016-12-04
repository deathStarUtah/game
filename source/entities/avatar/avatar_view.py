import pygame

from source.entities.entity import entity_view

from source.entities.entity import action

from animation_config import run
from animation_config import stand
from animation_config import walk

class AvatarView(entity_view.EntityView):
    def __init__(self):
        entity_view.EntityView.__init__(self)

        self.height = 74
        self.width = 32
        pass

    def on_render(self, camera):
        if self.velocity() == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(camera, self.direction, camera.center)
        elif self.velocity() <= self.velocity_base:
            if self.animation == None or self.animation.action != "walk":
                self.animation = action.Action(walk.walk_data)
            self.animation.on_render(camera, self.direction, camera.center)
        elif self.velocity() <= self.max_velocity:
            if self.animation == None or self.animation.action != "run":
                self.animation = action.Action(run.run_data)
            self.animation.on_render(camera, self.direction, camera.center)
        else:
            print("Entity.on_render() invalid option.")
        pass
