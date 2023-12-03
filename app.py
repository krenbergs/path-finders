from flask import Flask
from flask import render_template
import random
import numpy as np
import noise

app = Flask(__name__)

@app.route("/")
def home():
    environment = generate_3d_environment(size=10, seed=random.random()*1000)
    path=[]
    return render_template("index.html", coordinates=environment, red_cube_coords=path)


def generate_3d_maze(n):
    # Initialize list of wall coordinates
    walls = []
    
    # Randomly assign walls
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if random.choice([0, 1]) == 1:
                    walls.append([x, y, z])
    
    return walls

def generate_3d_environment(size, scale=0.1, octaves=6, persistence=0.5, lacunarity=2.0, height_threshold=0.0, seed=0):
    # Create a 3D grid of coordinates in the range of 0 to n
    x = np.linspace(0, size, size)
    y = np.linspace(0, size, size)
    z = np.linspace(0, size, size)
    coords = np.array(np.meshgrid(x, y, z)).T.reshape(-1,3)

    # Generate Perlin noise
    perlin_noise = np.zeros((size, size, size))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                perlin_noise[i][j][k] = noise.pnoise3(i*scale + seed, j*scale + seed, k*scale + seed, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=size, repeaty=size, repeatz=size)

    # Generate environment
    environment = []
    for i in range(size):
        for j in range(size):
            for k in range(size):
                # Only include points that are above the height threshold
                if perlin_noise[i][j][k] > height_threshold:
                    environment.append([i, j, k])

    return environment