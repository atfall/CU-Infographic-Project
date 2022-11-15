import streamlit as st

"""
Showcase of planets/satellites (small boxes) orbiting around a star. 
Uses a custom velocity function to manually calculate the gravity, assuming 
the star is in the middle and is massive enough that the satellites does not 
affect it.
This is a port of the Planet demo included in Chipmunk.
"""

import math
import random

random.seed(5)  # Feel free to adjust, this is just to make each run equal


import pymunk
import pymunk.pygame_util

gravityStrength = 5.0e6


def planetGravity(body, gravity, damping, dt):
    # Gravitational acceleration is proportional to the inverse square of
    # distance, and directed toward the origin. The central planet is assumed
    # to be massive enough that it affects the satellites but not vice versa.
    sq_dist = body.position.get_dist_sqrd((300, 300))
    g = (
        (body.position - pymunk.Vec2d(300, 300))
        * -gravityStrength
        / (sq_dist * math.sqrt(sq_dist))
    )
    pymunk.Body.update_velocity(body, g, damping, dt)


def add_box(space):
    body = pymunk.Body()
    body.position = pymunk.Vec2d(random.randint(50, 550), random.randint(50, 550))
    body.velocity_func = planetGravity

    # Set the box's velocity to put it into a circular orbit from its
    # starting position.
    r = body.position.get_distance((300, 300))
    v = math.sqrt(gravityStrength / r) / r
    body.velocity = (body.position - pymunk.Vec2d(300, 300)).perpendicular() * v
    # Set the box's angular velocity to match its orbital period and
    # align its initial angle with its position.
    body.angular_velocity = v
    body.angle = math.atan2(body.position.y, body.position.x)

    box = pymunk.Poly.create_box(body, size=(10, 10))
    box.mass = 1
    box.friction = 0.7
    box.elasticity = 0
    box.color = pygame.Color("white")
    space.add(body, box)
