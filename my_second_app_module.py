
from handcalcs.decorator import handcalc

@handcalc()
def seismic_design_force( a_p: float, S_ds: float, z: float, h: float, R_p: float, I_p: float ):
    """
    returns Seismic Design force factor F_p per ASCE 7-16 EQN 13.3-1 to 13.3-3
    """
    F_p_nom = 0.4 * a_p * S_ds * (1 + 2 * (z / h)) / (R_p/I_p)
    F_p_min = 0.3 * S_ds * I_p
    F_p_max = 1.6 * S_ds * I_p
    
    if F_p_min < F_p_nom < F_p_max:
        F_p = F_p_nom
    elif F_p_min >= F_p_nom:
        F_p = F_p_min
    elif F_p_max <= F_p_nom:
        F_p = F_p_max
    return F_p

@handcalc()
def lateral_seismic_force(omega, Fp, W_p):
    """ 
    returns omega level lateral Fp
    """
    F_ph = omega * Fp * W_p
    return F_ph

@handcalc()
def vertical_seismic_force(S_ds, W_p):
    """ 
    returns Horizontal Wp
    """
    F_spv = 0.2 * S_ds * W_p
    return F_spv

@handcalc()
def resisting_load(F_spv, W_p):
    """ 
    returns Horizontal Wp
    """
    F_sres = F_spv - (0.9 * W_p)
    return F_sres

@handcalc()
def tension_across_length(H_cg, F_ph, L1, Q):
    """ 
    returns tension on anchor across length
    """
    T_1 = (H_cg * F_ph) / (L1 * Q)
    return T_1

@handcalc()
def tension_across_width(H_cg, F_ph, B1, R):
    """ 
    returns tension on anchor across width
    """
    T_2 = (H_cg * F_ph) / (B1 * R)
    return T_2

@handcalc()
def vertical_reaction_uplift(F_sres, N):
    """ 
    returns vertical reaction at anchor due to uplift - DL
    """
    T_3 = F_sres / N
    return T_3

@handcalc()
def tension_per_anchor(T_1, T_2, T_3):
    """ 
    returns total tension per anchor
    """
    T_net = max(T_1, T_2) + T_3
    return T_net

@handcalc()
def shear_per_anchor(F_ph, N):
    """ 
    returns total shear per anchor
    """
    V_anchor = F_ph / N
    return V_anchor
