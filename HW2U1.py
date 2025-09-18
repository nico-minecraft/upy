import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Parameters (example values for a small DC motor) ---
Ra = 1.0      # Armature resistance [ohm]
La = 0.5      # Armature inductance [H]
Ke = 0.01     # Back EMF constant [V·s/rad]
Kt = 0.01     # Torque constant [N·m/A]
J  = 0.01     # Inertia [kg·m^2]
B  = 0.1      # Viscous friction [N·m·s/rad]

# Load torque (disturbance) = 0 for now
def dc_motor_dynamics(t, x, u_func):
    i_a, omega, theta = x
    Va = u_func(t)
    di_dt = (-Ra/La) * i_a - (Ke/La) * omega + (1/La) * Va
    domega_dt = (Kt/J) * i_a - (B/J) * omega  # no load torque
    dtheta_dt = omega
    return [di_dt, domega_dt, dtheta_dt]

# --- Input: Step voltage (e.g., 24 V after t=0) ---
def step_voltage(t):
    return 24.0 if t >= 0 else 0.0

# Time span for simulation
t_span = (0, 2)  # simulate for 2 seconds
t_eval = np.linspace(t_span[0], t_span[1], 2000)

# Initial conditions: i(0)=0, omega(0)=0, theta(0)=0
x0 = [0.0, 0.0, 0.0]

# Solve ODE system
sol = solve_ivp(dc_motor_dynamics, t_span, x0, t_eval=t_eval, args=(step_voltage,))

# Extract results
t = sol.t
i_a = sol.y[0]
omega = sol.y[1]
theta = sol.y[2]

# --- Plot results ---
plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(t, i_a, label="Armature Current $i_a(t)$")
plt.ylabel("Current [A]")
plt.grid(True)
plt.legend()

plt.subplot(3,1,2)
plt.plot(t, omega, label="Angular Velocity $\\omega(t)$", color='orange')
plt.ylabel("Velocity [rad/s]")
plt.grid(True)
plt.legend()

plt.subplot(3,1,3)
plt.plot(t, theta, label="Angular Position $\\theta(t)$", color='green')
plt.xlabel("Time [s]")
plt.ylabel("Position [rad]")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
