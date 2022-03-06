"""Orbit sim main program."""

import pygame

from constellations.first_constellation import constellation, general_parameters
from physicalobject_model import PhysicalObjectModel
from physicalobject_views import PhysicalObjectView, distance
from camera import Camera


game_window = pygame.display.set_mode(flags=pygame.RESIZABLE)
pygame.display.set_caption("orbit simulator")
pygame.init()
elapsed_time = 0


body_models = []
body_viewers = []
for name, body in constellation.items():
    body_model = PhysicalObjectModel(
        body["x"],
        body["y"],
        body["radius"],
        body["init_velocity_x"],
        body["init_velocity_y"],
        body["mass"],
        general_parameters["time_step"],
    )
    body_models.append(body_model)

    body_viewers.append(
        PhysicalObjectView(
            name,
            general_parameters["scale_factor"],
            body["colour"],
            body["image"],
            body_model,
        )
    )


camera = Camera(game_window, body_models, body_viewers)


if __name__ == "__main__":
    mouse_button_down_pos = None
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_button_down_pos = event.pos  # Keep track of mouse button down to distinguish click from drag
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and distance(mouse_button_down_pos, event.pos) <= 10:
                camera.trackBody(*event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    camera.zoomOut()
                if event.button == 5:
                    camera.zoomIn()

            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                camera.pan(*event.rel)

        # keep track of the elapsed time in days
        elapsed_time += general_parameters["time_step"] / (3600 * 24)

        # update the camera system and draw bodies
        camera.update(elapsed_time)

        pygame.display.update()

    pygame.quit()
