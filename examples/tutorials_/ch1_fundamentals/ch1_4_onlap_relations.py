"""
1.4: Unconformity relationships
===============================

"""

# %%
# Importing gempy
import gempy as gp
import gempy_viewer as gpv

# Aux imports
import numpy as np
import os

np.random.seed(1515)

# %%
# We import a model from an existing folder, representing a subduction
# zone with onlap relationships. The aesara function is automatically
# recombined to allow changes.
# 

# %%
# cwd = os.getcwd()
# if not 'examples' in cwd:
#     data_path = os.getcwd() + '/examples/'
# else:
#     data_path = cwd + '/../../'
# 
# geo_model = gp.load_model(r'Tutorial_ch1-8_Onlap_relations',
#                           path=data_path + 'data/gempy_models/Tutorial_ch1-8_Onlap_relations',
#                           recompile=True)
# 
# geo_model.meta.project_name = "Onlap_relations"

data_path = os.path.abspath('../../')

geo_model: gp.data.GeoModel = gp.create_geomodel(
    project_name='Onlap_relations',
    extent=[-200, 1000, -500, 500, -1000, 0],
    resolution=[50, 50, 50],
    number_octree_levels=4,
    importer_helper=gp.data.ImporterHelper(
        path_to_orientations=data_path + "/data/input_data/tut-ch1-4/tut_ch1-4_orientations.csv",
        path_to_surface_points=data_path + "/data/input_data/tut-ch1-4/tut_ch1-4_points.csv",
    )
)

# %% 
gpv.plot_2d(geo_model)

# %%
gp.set_topography_from_random(grid=geo_model.grid, d_z=np.array([-600, -100]))

# %% 
print(geo_model.structural_frame)
geo_model.transform.apply_anisotropy(gp.data.GlobalAnisotropy.NONE)
s = gp.compute_model(geo_model)

# %% 
gpv.plot_2d(geo_model, show_data=True)
gpv.plot_3d(
    model=geo_model,
    show_surfaces=True,
    show_data=True,
    image=False,
    show_topography=True,
    kwargs_plot_structured_grid={'opacity': .2}
)

foo

# %%
gpv.plot_2d(
    model=geo_model,
    cell_number=2,
    regular_grid=geo_model.solutions.mask_matrix_pad[0],
    show_data=True, kwargs_regular_grid={'cmap': 'gray', 'norm': None}
)

gpv.plot_2d(
    model=geo_model,
    cell_number=2,
    regular_grid=geo_model.solutions.mask_matrix_pad[1],
    show_data=True, kwargs_regular_grid={'cmap': 'gray', 'norm': None}
)

gpv.plot_2d(
    model=geo_model,
    cell_number=2,
    regular_grid=geo_model.solutions.mask_matrix_pad[2],
    show_data=True, kwargs_regular_grid={'cmap': 'gray', 'norm': None}
)

gpv.plot_2d(
    model=geo_model,
    cell_number=2,
    regular_grid=geo_model.solutions.mask_matrix_pad[3],
    show_data=True, kwargs_regular_grid={'cmap': 'gray', 'norm': None}
)

# sphinx_gallery_thumbnail_number = 7
