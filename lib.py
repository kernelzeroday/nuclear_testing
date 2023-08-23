import numpy as np

def binding_energy(A, Z):
    """Calculate binding energy using the semi-empirical mass formula.
    A: Atomic Mass Number
    Z: Atomic Number
    """
    a1, a2, a3, a4, a5 = 15.67, 17.23, 0.75, 93.2, 0  # Constants
    if A % 2 == 1: a5 = 0
    elif Z % 2 == 0: a5 = 12.0
    else: a5 = -12.0
    
    B = (a1 * A) - (a2 * A**(2/3)) - (a3 * (Z**2 / A**(1/3))) - (a4 * ((A - 2*Z)**2 / A)) - (a5 / A**(1/2))
    return B

def fission_reaction(nucleus_mass):
    """Simulate a fission reaction.
    nucleus_mass: Mass of the nucleus
    """
    fragment_mass = nucleus_mass / 2
    energy_released = binding_energy(nucleus_mass, nucleus_mass/2) * nucleus_mass
    return fragment_mass, energy_released

def fusion_reaction(mass1, mass2):
    """Simulate a fusion reaction.
    mass1, mass2: Masses of the reacting nuclei
    """
    fused_mass = mass1 + mass2
    energy_released = binding_energy(fused_mass, (mass1 + mass2)/2) * fused_mass
    return fused_mass, energy_released

def decay_process(initial_mass, half_life, time_elapsed):
    """Calculate the remaining mass after decay.
    initial_mass: Initial mass of the radioactive substance
    half_life: Half-life of the substance
    time_elapsed: Time elapsed for decay
    """
    remaining_mass = initial_mass * 0.5**(time_elapsed / half_life)
    return remaining_mass
