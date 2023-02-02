"""
Dependencies
"""

import json
import networkx


class DependencyAnalyzer:
    """
    DependencyAnalyzer
    """

    def __init__(self, data):
        self.data = data

    def deps_satisfied(self, pkg, available):
        """
        Can the package be built given the set of available
        previously missing packages
        """
        return len(self.get_deps(pkg) - available) == 0

    @staticmethod
    def from_file(deps_filename: str):
        """
        Load dependency data from a JSON file
        """
        with open(deps_filename, "r", encoding="utf-8") as deps_file:
            return DependencyAnalyzer(json.load(deps_file))

    def get_deps(self, pkg):
        """
        Get the missing dependencies of a package
        """
        return set(self.data[pkg]["build"].keys())

    def next_phase(self, available, pending):
        """
        Calculate the next set of packages that can be built
        """
        return set(p for p in pending if self.deps_satisfied(p, available))

    def calculate_build_phases(self):
        """
        Calculates the list of phases, each containing a set of packages
        that can be built together
        """
        return self.calculate_build_phases_helper(set(), set(self.data.keys()), [])

    def calculate_build_phases_helper(self, available, pending, phases):
        """
        Helper for iterating over build phase calculations
        """
        new_phase = self.next_phase(available, pending)
        if not new_phase:
            return (phases, available, pending)
        next_phases = phases + [new_phase]
        next_pending = pending - new_phase
        if not next_pending:
            return (next_phases, available.union(new_phase), next_pending)
        return self.calculate_build_phases_helper(
            available.union(new_phase), next_pending, next_phases
        )

    def calculate_chain_build(self):
        """
        Calculate the chain build invocation
        """
        phases, _, _ = self.calculate_build_phases()
        return " : ".join([" ".join(sorted(phase)) for phase in phases])

    def del_pkg(self, pkg):
        """
        Delete a package from the dependency graph
        This is needed if e.g. the package is built previously
        (since the analysis only considers what's already in stable updates)
        """
        # remove that package's entry
        if pkg in self.data:
            del self.data[pkg]
        # also remove it as a dependency
        for p in self.data:
            for stage in ['build']:
                if pkg in self.data[p][stage]:
                    del self.data[p][stage][pkg]

    def output_missing_graph(self, pending):
        """
        Outputs the graph of missing dependencies
        """
        return {
            k: set(self.data[k]["build"].keys()).intersection(pending)
            for k in sorted(pending)
        }

    def what_requires(self, pkg):
        """
        What requires a package
        """
        return set(
            k for k in self.data.keys() if pkg in set(self.data[k]["build"].keys())
        )

    def find_cycles(self):
        edges = [(k, v) for k in self.data.keys() for v in self.data[k]["build"].keys()]
        G = networkx.DiGraph(edges)
        return sorted(networkx.simple_cycles(G))
