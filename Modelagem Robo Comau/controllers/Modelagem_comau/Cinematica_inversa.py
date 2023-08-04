import numpy as np

def getAngles(pose):
# Desacoplamento cinemático:
    xc = (pose[0][3] - (95*pose[0][2]))
    yc = (pose[1][3] - (95*pose[1][2]))
    zc = (pose[2][3] - (95*pose[2][2]))

    # Auxiliares:
    r = np.sqrt((xc**2) + (yc**2))
    s = (zc-450)
    h = np.sqrt(((r-150)**2)+(s**2))
    l = np.sqrt((130**2) + (647.07**2))  

    thetas = (np.ones(6)*np.nan)

    # Theta 1:
    thetas[0] = np.arctan2(yc, xc)   #+/- theta1

    # Theta 3:
    alpha = np.arctan2(647.07, 130)
    sb = (((590**2) + (l**2) - (h**2))/(2*590*l))
    beta = np.arctan2(-sb, np.sqrt(1-(sb**2)))    #+/- beta | +/- cb
    thetas[2] = (beta - alpha)  

    # Theta 2:
    sg = -((l*np.cos(beta))/h)
    gamma = np.arctan2(-sg, np.sqrt(1-(sg**2)))   #+/- gamma | +/- cg | +/- sg
    psi = np.arctan2((r-150), s)
    thetas[1] = (gamma + psi)

    # Theta 5:
    c5 = -(-(np.cos(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[0][2]) + (np.sin(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[1][2]) - (np.cos(thetas[1]-thetas[2])*pose[2][2]))
    thetas[4] = np.arctan2(np.sqrt(1-(c5**2)+1e-20), c5)

    # Theta 6:
    s6 = ((-(np.cos(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[0][1]) + (np.sin(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[1][1]) - (np.cos(thetas[1]-thetas[2])*pose[2][1]))/np.sin(thetas[4]))
    thetas[5] = np.arctan2(s6, np.sqrt(1-(s6**2)))

    # Theta 4:
    s4 = (((np.sin(thetas[0])*pose[0][2]) + (np.cos(thetas[0])*pose[1][2]))/np.sin(thetas[4]))
    thetas[3] = -np.arctan2(s4, np.sqrt(1-(s4**2)))

    return thetas