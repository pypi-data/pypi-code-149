#!/usr/bin/env python3


import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D
from typing import TypeAlias, TextIO, Union, Any
from .odb import Odb


ViewsDict: TypeAlias = dict[str, tuple[int, int, int]]


class MeltpointNotSetError(Exception):
    def __init__(self) -> None:
        self.message = "You must enter the meltpoint and, optionally, the string name of a plt colormap (default \"turbo\") in order to set the colormap"


class OdbVisualizer(Odb):
    """

    """
    def __init__(self, **kwargs) -> None:
        Odb.__init__(self, **kwargs)

        self.results_dir: str = kwargs.get("results_dir", os.getcwd())
        self.interactive: bool = kwargs.get("interactive", True)

        self.views: ViewsDict = self.load_views_dict(os.path.join(os.path.dirname(os.path.abspath(__file__)), "views.json"))

        self.views_list: list[str] = list(self.views.keys())

        self.angle: str = self.views_list[49]
        self.elev: int = self.views[self.angle][0]
        self.azim: int = self.views[self.angle][1]
        self.roll: int = self.views[self.angle][2]

        self.colormap_name: str = kwargs.get("colormap_name", "turbo")
        self.colormap: plt.cm.ScalarMappable


    def select_colormap(self) -> None:
        if not (hasattr(self, "meltpoint") or hasattr(self, "colormap_name")):
            raise MeltpointNotSetError

        norm: mcolors.Normalize = mcolors.Normalize(0, self.meltpoint)
        self.colormap = plt.cm.ScalarMappable(norm=norm, cmap=self.colormap_name)
        self.colormap.set_array([])


    def load_views_dict(self, file) -> ViewsDict:
        o_file: TextIO
        with open(file, "r") as o_file:
            return json.load(o_file)


    def select_views(self, view: Union[int, tuple[int, int, int]]) -> None:
        if isinstance(view, int):
            self.angle = self.views_list[view]
            self.elev = self.views[self.angle][0]
            self.azim = self.views[self.angle][1]
            self.roll = self.views[self.angle][2]

        else:
            self.angle = "custom"
            self.elev = view[0]
            self.azim = view[1]
            self.roll = view[2]


    def plot_time_3d(self, time: float, label: str, title: str)-> Any:
        curr_nodes: Any = self.out_nodes[self.out_nodes["Time"] == time]

        formatted_time: str = format(round(time, 2), ".2f")
        combined_label = f"{label}-{formatted_time}"

        # PLT does not play nice with type hints, we use "any"
        fig: Any = plt.figure(figsize=(19.2, 10.8))
        ax: Any = plt.axes(projection="3d", label=combined_label)

        ax.set_xlabel(self.x.name)
        ax.set_ylabel(self.y.name)
        ax.set_zlabel(self.z.name)

        ax.set_box_aspect((self.x.size, self.y.size, self.z.size))
        ax.view_init(elev=self.elev, azim=self.azim, roll=self.roll)

        ax.set_title(f"{title}, time step: {formatted_time}")
        fig.add_axes(ax, label=ax.title)

        faces: list[str] = ["x_low", "x_high", "y_low", "y_high", "z_low", "z_high"]
        face: str
        for face in faces:
            X: Any
            Y: Any
            Z: Any
            face_shape: tuple[int, int]
            temp_mask: Any
            indices: list[str] = ["X", "Y", "Z"]

            # TODO This whole idea could be parameterized, but it might be less readable
            if "x" in face:
                indices.remove("X")
                y = self.y.vals
                z = self.z.vals
                if "low" in face:
                    X = np.full((self.z.size, self.y.size), self.x.vals[0])
                    temp_mask = curr_nodes["X"] == self.x.vals[0]
                else: # if "high" in face:
                    X = np.full((self.z.size, self.y.size), self.x.vals[-1])
                    temp_mask = curr_nodes["X"] == self.x.vals[-1]

                Y, Z = np.meshgrid(y, z)
                face_shape = X.shape

            elif "y" in face:
                indices.remove("Y")
                x = self.x.vals
                z = self.z.vals
                if "low" in face:
                    Y = np.full((self.z.size, self.x.size), self.y.vals[0])
                    temp_mask = curr_nodes["Y"] == self.y.vals[0]
                else: # if "high" in face:
                    Y = np.full((self.z.size, self.x.size), self.y.vals[-1])
                    temp_mask = curr_nodes["Y"] == self.y.vals[-1]

                X, Z = np.meshgrid(x, z)
                face_shape = Y.shape

            else: # if "z" in face
                indices.remove("Z")
                x = self.x.vals
                y = self.y.vals
                if "low" in face:
                    Z = np.full((self.y.size, self.x.size), self.z.vals[0])
                    temp_mask = curr_nodes["Z"] == self.z.vals[0]
                else: # if "high" in face:
                    Z = np.full((self.y.size, self.x.size), self.z.vals[-1])
                    temp_mask = curr_nodes["Z"] == self.z.vals[-1]

                X, Y = np.meshgrid(x, y)
                face_shape = Z.shape

            temp_nodes: Any = curr_nodes[temp_mask]
            first_dim: Any = temp_nodes[indices[0]]
            first_offset: float = first_dim.min()
            second_dim: Any = temp_nodes[indices[1]]
            second_offset: float = second_dim.min()
            first_color_dim: int
            second_color_dim: int
            first_color_dim, second_color_dim = face_shape

            colors: Any = np.zeros((first_color_dim, second_color_dim, 3))

            node: Any
            for _, node in temp_nodes.iterrows():
                temp = node["Temp"]
                second_index: int = int((node[indices[0]] - first_offset) / self.mesh_seed_size)
                first_index: int = int((node[indices[1]] - second_offset) / self.mesh_seed_size)

                if temp >= self.meltpoint:
                    colors[first_index, second_index] = (0.25, 0.25, 0.25)
                else:
                    colors[first_index, second_index] = self.colormap.to_rgba(temp)[:3]

            ax.plot_surface(X, Y, Z, facecolors=colors)

        return fig


        
