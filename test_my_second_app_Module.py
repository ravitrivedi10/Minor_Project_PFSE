from pytest import approx

from my_second_app_module import seismic_design_force

def test_seismic_design_force():
    latex_out, result = seismic_design_force(2.5, 0.59, 0, 30, 2.5, 1.0) 
    assert result == 0.234


from my_second_app_module import lateral_seismic_force

def test_lateral_seismic_force():
    latex_out, result = lateral_seismic_force(2.0, 0.234, 17000)
    assert result == approx(7969.608)