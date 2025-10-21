import numpy as np
import matplotlib.pyplot as plt
from RandomWalk_2D import drip_layer
# --- Pollock 'Blue Poles' inspired simulation (improved vertical poles) ---

# Function to draw solid blue poles with texture
def draw_blue_pole(x_center, tilt, width, color="#01153d"):
    # base vertical line with small edge perturbations
    x_vals = np.linspace(x_center - width/2, x_center + width/2, 20)
    for x in x_vals:
        y = np.linspace(-1, 1, 200)
        jitter = np.zeros(200)
        for i in range(200):
            jitter[i] = 0.05 * ((np.random.rand()+0.015)**100) * np.sin(10*y[i] + 5*np.random.rand()) + 0.005*np.sin(100*y[i] + np.random.rand()*50) + 0.002*np.sin(1000*y[i] + np.random.rand()*500) + 0.0001*np.sin(10000*y[i] + np.random.rand()*5000)
        xj = x + tilt*y + jitter
        plt.plot(xj, y, color=color, linewidth=np.random.uniform(3,6), alpha=0.5)

plt.figure(figsize=(12, 7))
plt.axis('off')
plt.gca().set_facecolor('#f2efe9')  # off-white canvas

xlim = 1.2*1.2
ylim = 1*1.2
# Draw 8 main blue poles with varying tilt and width
drip_layer(num_particles=100, steps=4000, spread=0.03, xlim=xlim, ylim=ylim, color_map=plt.cm.Greys, lw_range=(0.5, 5), alpha=0.6)
drip_layer(num_particles=100, steps=4000, spread=0.03, xlim=xlim, ylim=ylim, color_map=plt.cm.copper, lw_range=(0.5, 1), alpha=0.6)
drip_layer(num_particles=20, steps=30, spread=0.1, xlim=xlim, ylim=ylim, color_map=plt.cm.Oranges, lw_range=(5, 5), alpha=1)
draw_blue_pole(-0.8, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.0, 0.05))
drip_layer(num_particles=20, steps=30, spread=0.1, xlim=xlim, ylim=ylim, color_map=plt.cm.Wistia, lw_range=(5, 5), alpha=1)

draw_blue_pole(-0.4, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))
draw_blue_pole(-0.2, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))
draw_blue_pole(0.4, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))

drip_layer(num_particles=25, steps=4000, spread=0.03, xlim=xlim, ylim=ylim, color_map=plt.cm.pink, lw_range=(1, 2), alpha=0.5)
draw_blue_pole(-0.1, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))
draw_blue_pole(0.8, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))

drip_layer(num_particles=5, steps=4000, spread=0.03, xlim=xlim, ylim=ylim, color_map=plt.cm.Blues, lw_range=(0.0, 1), alpha=0.5)
draw_blue_pole(0.1, tilt=np.random.uniform(-0.1, 0.1), width=np.random.uniform(0.02, 0.05))

# Add white and black splatter bursts to simulate paint impacts
for _ in range(240):
    cx, cy = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    n_drops = np.random.randint(10, 30)
    for _ in range(n_drops):
        angle = np.random.uniform(0, 2*np.pi)
        r = np.random.uniform(0, 0.05)
        x = cx + r*np.cos(angle)
        y = cy + r*np.sin(angle)
        plt.plot(x, y, marker='o', markersize=np.random.uniform(1, 4), color=np.random.choice(['#ffffff','#000000','#002b7f']), alpha=np.random.uniform(0.3,0.8))

plt.xlim(-1.2, 1.2)
plt.ylim(-1, 1)
plt.tight_layout()
plt.show()