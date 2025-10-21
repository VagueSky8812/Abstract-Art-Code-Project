import numpy as np
import matplotlib.pyplot as plt

# --- Pollock 'Blue Poles' inspired simulation (improved vertical poles) ---

# Function to create drip layer
def drip_layer(num_particles, steps, spread, xlim, ylim, color_map, lw_range=(0.5, 5.0), alpha=0.6):
    colors = color_map(np.linspace(0.1, 1, num_particles))
    for i in range(num_particles):
        x, y = np.zeros(steps), np.zeros(steps)
        x[0], y[0] = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        angle = np.random.uniform(np.pi, np.pi)
        angle_prev = angle
        for s in range(1, steps):
            #angle = angle_prev + np.random.uniform(-0.5*np.pi, 0.5*np.pi)
            #angle = angle_prev + np.random.normal(0, 2*np.pi)
            angle = angle_prev + np.random.normal(0, np.pi)
            #limiter
            '''
            # for multiple cycles
            n = np.floor(angle/np.pi)
            if n%2 == 0:
                angle = angle - np.sign(angle)*n*np.pi
            else:
                angle = angle - np.sign(angle)*(n+1)*np.pi
            '''
            if angle>np.pi:
                angle = angle - 2*np.pi
            if angle<-np.pi:
                angle = angle + 2*np.pi
            
            x[s] = x[s-1] + spread * np.cos(angle)
            y[s] = y[s-1] + spread * np.sin(angle)
            
            #bounce back
            if x[s]>xlim:
                x[s] = 2*xlim - x[s]
                print(f"Step no. {s}; angle = {180*angle/np.pi}; bounced on the right bound")
                angle = np.sign(angle)*np.pi - angle
                print(f"reflected angle = {180*angle/np.pi}; bounced on the right bound")
            elif x[s]<-xlim:
                x[s] = -2*xlim - x[s]
                print(f"Step no. {s}; angle = {180*angle/np.pi};bounced on the left bound")
                angle = np.sign(angle)*np.pi - angle
                print(f"reflected angle = {180*angle/np.pi}; bounced on the left bound")
            elif y[s]>ylim:
                y[s] = 2*ylim - y[s]
                print(f"Step no. {s}; angle = {180*angle/np.pi};bounced on the top bound")
                angle = -angle
                print(f"reflected angle = {180*angle/np.pi}; bounced on the top bound")
            elif y[s]<-ylim:
                y[s] = -2*ylim - y[s]
                print(f"Step no. {s}; angle = {180*angle/np.pi};bounced on the bottom bound")
                angle = -angle
                print(f"reflected angle = {180*angle/np.pi}; bounced on the bottom bound")

            angle_prev = angle
        plt.plot(x, y, color=colors[i], linewidth=np.random.uniform(*lw_range), alpha=alpha)

# Draw 8 main blue poles with varying tilt and width
'''
plt.figure(figsize=(12, 7))
plt.axis('off')
plt.gca().set_facecolor('#f2efe9')  # off-white canvas

drip_layer(num_particles=1, steps=4000, spread=0.05, xlim=1.2, ylim=1, color_map=plt.cm.copper, lw_range=(1, 1), alpha=1)

plt.xlim(-1.2, 1.2)
plt.ylim(-1, 1)
plt.tight_layout()
plt.show()
'''