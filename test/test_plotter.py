import numpy as np
from WDPhotTools import plotter
from WDPhotTools.cooling_model_reader import model_list
import os


def test_list_everything():
    plotter.list_atmosphere_parameters()
    plotter.list_cooling_model()
    for i in model_list.keys():
        plotter.list_cooling_parameters(i)


def test_plot_atmosphere_model_with_ext_as_str():
    plotter.plot_atmosphere_model(display=False,
                                  savefig=True,
                                  folder='test' + os.sep + 'test_output',
                                  filename='test_plot_atmosphere_model',
                                  ext='png')


def test_plot_atmosphere_model():
    plotter.plot_atmosphere_model(display=False,
                                  savefig=True,
                                  folder='test' + os.sep + 'test_output',
                                  filename='test_plot_atmosphere_model',
                                  ext=['png', 'pdf'])


def test_plot_atmosphere_model_different_filters():
    plotter.plot_atmosphere_model(x='B-V',
                                  y='U',
                                  invert_yaxis=True,
                                  display=False)


def test_plot_atmosphere_model_color_color_diagram():
    plotter.plot_atmosphere_model(x='U-V', y='B-V', display=False)


def test_plot_atmosphere_model_with_differnt_independent_variables():
    plotter.plot_atmosphere_model(independent=['logg', 'Mbol'],
                                  independent_values=[
                                      np.linspace(7.0, 9.0, 5),
                                      np.linspace(2.0, 18.0, 101)
                                  ],
                                  invert_xaxis=True,
                                  invert_yaxis=True,
                                  display=False)


def test_plot_2_atmosphere_models():
    fig = plotter.plot_atmosphere_model(display=False, title=' ')
    plotter.plot_atmosphere_model(atmosphere='He',
                                  invert_yaxis=True,
                                  contour=False,
                                  display=False,
                                  title='DA + DB (Montreal)',
                                  fig=fig)


def test_plot_cooling_model():
    plotter.plot_cooling_model(display=False,
                               savefig=True,
                               folder='test' + os.sep + 'test_output',
                               filename='cooling_model',
                               ext='png')


def test_plot_cooling_model():
    plotter.plot_cooling_model(x='r',
                               y='logg',
                               mass=np.arange(0.5, 1.0, 0.1),
                               invert_xaxis=True,
                               invert_yaxis=True,
                               display=False,
                               savefig=True,
                               folder='test' + os.sep + 'test_output',
                               filename='cooling_model_r_logg',
                               ext=['png', 'pdf'])