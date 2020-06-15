#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.pardir)
sys.path.insert(0, os.path.join(os.pardir, 'openmoc'))
from testing_harness import PlottingTestHarness
from input_set import NonUniformLatticeInput
from openmoc.plotter import plot_cells
import openmoc


class PlotCellsTestHarness(PlottingTestHarness):
    """Test cell plotting with a 4x4 lattice."""

    def __init__(self):
        super(PlotCellsTestHarness, self).__init__()
        self.input_set = NonUniformLatticeInput()
        self.num_polar = 4
        self.azim_spacing = 0.25
        self.z_spacing = 0.5
        self.max_iters = 10

    def _create_trackgenerator(self):
        """Instantiate a TrackGenerator."""
        geometry = self.input_set.geometry
        geometry.initializeFlatSourceRegions()
        self.track_generator = \
            openmoc.TrackGenerator3D(geometry, self.num_azim, self.num_polar,
                                     self.azim_spacing, self.z_spacing)
        self.track_generator.setSegmentFormation(openmoc.OTF_STACKS)


    def _run_openmoc(self):
        """Plot the cells in the geometry."""

        # Create a series of Matplotlib Figures / PIL Images for different
        # plotting parameters and append to figures list
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, offset=0.1,
                       get_figure=True))
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, offset=0.1,
                       get_figure=True))
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, offset=0.1,
                       get_figure=True, xlim=(0., 2.), ylim=(0., 2.)))
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, offset=0.1,
                       get_figure=True, library='pil'))
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, plane="yz",
                       offset=0.6, get_figure=True))
        self.figures.append(
            plot_cells(self.input_set.geometry, gridsize=100, plane="xz",
                       offset=0.6, get_figure=True))


if __name__ == '__main__':
    harness = PlotCellsTestHarness()
    harness.main()
