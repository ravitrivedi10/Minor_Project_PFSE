import streamlit as st
from PIL import Image
# from handcalcs.decorator import handcalc
import forallpeople as us
from math import pi, sqrt
import plotly.graph_objects as go


from my_second_app_module import seismic_design_force
from my_second_app_module import lateral_seismic_force
from my_second_app_module import vertical_seismic_force
from my_second_app_module import resisting_load
from my_second_app_module import tension_across_length
from my_second_app_module import tension_across_width
from my_second_app_module import vertical_reaction_uplift
from my_second_app_module import tension_per_anchor
from my_second_app_module import shear_per_anchor



us.environment("structural")



# @handcalc()
# def seismic_design_force( a_p: float, S_ds: float, z: float, h: float, R_p: float, I_p: float ):
#     """
#     returns Seismic Design force factor F_p per ASCE 7-16 EQN 13.3-1 to 13.3-3
#     """
#     F_p_nom = 0.4 * a_p * S_ds * (1 + 2 * (z / h)) / (R_p/I_p)
#     F_p_min = 0.3 * S_ds * I_p
#     F_p_max = 1.6 * S_ds * I_p
    
#     if F_p_min < F_p_nom < F_p_max:
#         F_p = F_p_nom
#     elif F_p_min >= F_p_nom:
#         F_p = F_p_min
#     elif F_p_max <= F_p_nom:
#         F_p = F_p_max
#     return F_p

# @handcalc()
# def lateral_seismic_force(omega, Fp, W_p):
#     """ 
#     returns omega level lateral Fp
#     """
#     F_ph = omega * Fp * W_p
#     return F_ph

# @handcalc()
# def vertical_seismic_force(S_ds, W_p):
#     """ 
#     returns Horizontal Wp
#     """
#     F_spv = 0.2 * S_ds * W_p
#     return F_spv

# @handcalc()
# def resisting_load(F_spv, W_p):
#     """ 
#     returns Horizontal Wp
#     """
#     F_sres = F_spv - (0.9 * W_p)
#     return F_sres

# @handcalc()
# def tension_across_length(H_cg, F_ph, L1, Q):
#     """ 
#     returns tension on anchor across length
#     """
#     T_1 = (H_cg * F_ph) / (L1 * Q)
#     return T_1

# @handcalc()
# def tension_across_width(H_cg, F_ph, B1, R):
#     """ 
#     returns tension on anchor across width
#     """
#     T_2 = (H_cg * F_ph) / (B1 * R)
#     return T_2

# @handcalc()
# def vertical_reaction_uplift(F_sres, N):
#     """ 
#     returns vertical reaction at anchor due to uplift - DL
#     """
#     T_3 = F_sres / N
#     return T_3

# @handcalc()
# def tension_per_anchor(T_1, T_2, T_3):
#     """ 
#     returns total tension per anchor
#     """
#     T_net = max(T_1, T_2) + T_3
#     return T_net

# @handcalc()
# def shear_per_anchor(F_ph, N):
#     """ 
#     returns total shear per anchor
#     """
#     V_anchor = F_ph / N
#     return V_anchor

h_value = st.sidebar.number_input("building height (ft)", value=30.0)
z_value = st.sidebar.number_input("Equipment elevation (ft)", value=0.0)
S_ds_value = st.sidebar.number_input("Design spectral resp acc.", value=0.586)
I_p_value = st.sidebar.number_input("Comp Imp Factor", value=1.0)
a_p_value = st.sidebar.number_input("Comp Amplification Factor", value=2.5)
R_p_value = st.sidebar.number_input("Comp response Mod Factor", value=2.5)
# Building Inputs
W_p_value = st.sidebar.number_input("Equipment Weight lb", value=17000)
L_value = st.sidebar.number_input("Equipment Length in inch", value=624.0)
B_value = st.sidebar.number_input("Equipment Width in inch", value=276.0)
H_value = st.sidebar.number_input("Equipment Height in inch", value=144.0)
H_cg_value = st.sidebar.number_input("Equipment CG Height in inch", value=72.0)
L1_value = st.sidebar.number_input("anchor locating dimension along L in inch", value=612.0)
B1_value = st.sidebar.number_input("anchor locating dimension along B in inch", value=264.0)
Q_value = st.sidebar.number_input("anchor along width", value=2.0)
R_value = st.sidebar.number_input("anchor along length", value=7.0)


omega = 2.0
h = h_value #* us.inch
z = z_value #* us.inch
S_ds = S_ds_value 
I_p = I_p_value 
a_p = a_p_value
R_p = R_p_value
# Building Inputs
W_p = W_p_value #* us.lb
L = L_value #* us.inch
B = B_value #* us.inch
H = H_value #* us.inch
H_cg = H_cg_value #* us.inch
L1 = L1_value #* us.inch
B1 = B1_value #* us.inch
Q = Q_value 
R = R_value
N = Q * R

st.header("# Calculating the Seismic Design Force for equipment in lb")

Fp_latex, Fp = seismic_design_force(a_p, S_ds, z, h, R_p, I_p)

st.subheader("Calculating the Seismic Design Force factor")
st.latex(Fp_latex)

image1 = Image.open('shape1.png')

st.image(image1, caption='Elevation and plan of equipment')


Fph_latex, Fph = lateral_seismic_force(omega, Fp, W_p)

st.subheader("Calculating the Lateral Seismic Design Force for equipment in lb")
st.latex(Fph_latex)

F_spv_latex, F_spv = vertical_seismic_force(S_ds, W_p)

st.subheader("Calculating the Vertical Seismic Design Force for equipment in lb")
st.latex(F_spv_latex)

F_sres_latex, F_sres = resisting_load(F_spv, W_p)

st.subheader("Calculating the Resisting equipment in lb")
st.latex(F_sres_latex)


image2 = Image.open('shape2.png')

st.image(image2, caption='Elevation view showing FBD forces')


T_1_latex, T_1 = tension_across_length(H_cg, Fph, L1, Q)

st.subheader("returns tension on anchor across length in lb")
st.latex(T_1_latex)

T_2_latex, T_2 = tension_across_width(H_cg, Fph, B1, R)

st.subheader("returns tension on anchor across length in lb")
st.latex(T_2_latex)


T_3_latex, T_3 = vertical_reaction_uplift(F_sres, N)

st.subheader("returns vertical reaction at anchor due to uplift - DL in lb")
st.latex(T_3_latex)

T_net_latex, T_net = tension_per_anchor(T_1, T_2, T_3)

st.subheader("positive -- tension.... negative -- compression..")

st.markdown("### returns total tension per anchor in lb")
st.latex(T_net_latex)


V_anchor_latex, V_anchor = shear_per_anchor(Fph, N)

st.subheader("returns total shear per anchor in lb")
st.latex(V_anchor_latex)




st.subheader("comparision of T_net w/ V_anchor")
# Create a scatter chart
fig = go.Figure(data=go.Scatter(x=[T_net], y=[V_anchor], mode='markers', marker=dict(size=16, color='red')))
fig.update_layout(title='T_net vs V_anchor', xaxis_title='T_net (lb)', yaxis_title='V_anchor (lb)')
st.plotly_chart(fig)



# fig = go.Figure(data=go.Bar(x=[T_net], y=[V_anchor]))
# fig.update_layout(title='T_net vs V_anchor', xaxis_title='T_net (lb)', yaxis_title='V_anchor (lb)')
# st.plotly_chart(fig)


st.subheader("comparision of T_1, T_2 and T_3 w/ V_anchor")
# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt
  
# creating dataframe
df = pd.DataFrame({
    'Tension_Force': (T_1, T_2, T_3),
    'Shear_Force': (V_anchor, V_anchor, V_anchor),
    
})
  
# plotting graph
# df.update_layout(title='T_net vs V_anchor', xaxis_title='T_net (lb)', yaxis_title='V_anchor (lb)')


st.bar_chart(df)