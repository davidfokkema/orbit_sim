AU = 149_597_871 * 10 ** 3
mass_sun = 1.98847 * 10 ** 30
radius_sun = 696_342_000

constellation = {
    "Star 1": {
        "x": 0,
        "y": 0,
        "radius": 1.711 * radius_sun,
        "init_velocity_x": 0,
        "init_velocity_y": -10000,
        "mass": 4 * mass_sun,
        "tail_length": 100,
        "image": "resources/star1.png",
    },
    "Star 2": {
        "x": 5 * AU,
        "y": 0,
        "radius": 1.711 * radius_sun,
        "init_velocity_x": 0,
        "init_velocity_y": 0,
        "mass": 1 * mass_sun,
        "tail_length": 100,
        "image": "resources/star1.png",
    },
}

general_parameters = {
    "time_step": 3600 * 0.5,
    "scale_factor": 10 / AU,
}
