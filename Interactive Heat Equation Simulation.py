import time
import numpy as np
import pygame

metals = {"Steel": 1.172E-5, "Lead": 4.0E-6, "Nickel": 2.3E-5, "Magnesium": 1.6E-5, "Titanium": 8.8E-6, "Platinum": 9.7E-6}
# Heat equation parameters:
# thermal diffusivity coefficient
def choose_metal():
    k = 0
    print("Choose a material for the simulation:")
    for metal in enumerate(metals.keys()):
        print(metal)
    choice = int(input())
    selected_metal = list(metals.keys())[choice]
    k = metals[selected_metal]
    return k

k = choose_metal()
mouse_clicked = False

Lx = 0.1
Ly = 0.1

# Spatial and temporal parameters:
nx = 100  # grid resolution
ny = 100
dt = 0.01 # time step
tf = 10  # final time
glt = 0  # global time tracker

# Boundary conditions (temperature behavior at edges).
T0 = 10  # initial temperature
T1 = 0;  # boundary conditions (initial temperature at edges
T2 = 0;
T3 = 0;
T4 = 0;


# Compute cell size
dx = Lx / nx;
dy = Ly / ny;


r1 = k * dt / dx ** 2
r2 = k * dt / dy ** 2

# failsafe if conditions unsuitable
if r1 > 0.5 or r2 > 0.5:
    raise TypeError('Unstable Solution!')

# Initialize temperature field
T = np.zeros((nx, ny, int(tf/dt)))

# Initial condition
for i in range(0, nx - 1):
    for j in range(1, ny - 1):
        T[i, j, 0] = T0

# Boundary conditions set-up
for i in range(0, nx):
    T[i, 0, 0] = T1
    T[i, ny - 1, 0] = T2

for j in range(0, ny):
    T[0, j, 0] = T3
    T[nx - 1, j, 0] = T4

# Generate 2D mesh
X = np.linspace(0, Lx, nx, endpoint=True)
Y = np.linspace(0, Ly, ny, endpoint=True)
X, Y = np.meshgrid(X, Y)

# Pygame setup
pygame.init()
win_size = 600
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("Interactive Heat Equation Module")

# Function to map Pygame coordinates to the grid
def map_to_grid(pos, nx, ny, screen_width, screen_height):
    x = int(pos[0] / screen_width * nx)
    y = int(pos[1] / screen_height * ny)
    return x, y

# Color mapping function
def get_color(value):
    # Map temperature to color (blue to red)
    color_value = min(255, max(0, int(255 * value / 100)))
    return (color_value, 0, 255 - color_value)

# Indicates pygame is running
run = True

# Infinite loop
while run:
    pygame.time.delay(10)
    time.sleep(0.1)  # Reducing sleep time to make the simulation more responsive

    # Update the temperature field - equation
    t = int(glt / dt)
    if t + 1 < int(tf / dt):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                a = (T[i + 1, j, t] - 2 * T[i, j, t] + T[i - 1, j, t]) / dx**2  # d2dx2
                b = (T[i, j + 1, t] - 2 * T[i, j, t] + T[i, j - 1, t]) / dy**2  # d2dy2
                T[i, j, t + 1] = k * dt * (a + b) + T[i, j, t]
        glt += dt

    # Draw the updated temperature field
    for i in range(nx):
        for j in range(ny):
            color = get_color(T[i, j, t])
            rect = pygame.Rect(i * win_size // nx, j * win_size // ny, win_size // nx, win_size // ny)
            pygame.draw.rect(win, color, rect)

    # Event handling - still not working
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            mouse_pos = pygame.mouse.get_pos()
            grid_x, grid_y = map_to_grid(mouse_pos, nx, ny, win_size, win_size)

            T[grid_x, grid_y, int(glt / dt)] = 10000.0  # Adjust this value as needed for intensity
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False
        elif event.type == pygame.MOUSEMOTION and mouse_clicked:
            mouse_pos = pygame.mouse.get_pos()
            x, y = event.pos
            grid_x, grid_y = map_to_grid(mouse_pos, nx, ny, win_size, win_size)

            # Set a high temperature at the clicked point
            T[grid_x, grid_y, int(glt / dt)] = 10000.0  # Adjust this value as needed for intensity

        elif event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# Close the pygame window
pygame.quit()
