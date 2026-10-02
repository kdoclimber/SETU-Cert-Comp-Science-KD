GRAVITY   = 9.81     # m/s²
SPEED_OF_LIGHT = 299_792_458   # m/s
AIR_DENSITY = 1.225  # kg/m³


def free_fall_velocity(time_s):
    v = GRAVITY * time_s
    return v

print(free_fall_velocity(10))

def kinetic_energy(mass_kg, velocity_ms):
    m = mass_kg
    v_squared = velocity_ms ** 2
    return 0.5 * m * v_squared
print(kinetic_energy(10, 30))

def drag_force(area_m2, velocity_ms, drag_coefficient=.07):
    Cd = drag_coefficient
    print(f'Cd = {drag_coefficient}')
    v_squared = velocity_ms ** 2
    area = area_m2
    return 0.5 * AIR_DENSITY * v_squared * area * Cd


print(drag_force(10,12,))
""" don't need to add drag_coefficient 
if it is defined in the function...
but I can if I want add it here which will ovder ride the original"""