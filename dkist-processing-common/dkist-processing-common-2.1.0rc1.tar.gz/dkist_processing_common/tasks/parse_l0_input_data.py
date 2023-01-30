"""
Common task to populate pipeline Constants and group files with tags by scanning headers.

The problems that parsing solves are:
* We need to sort and group data
* We need to ask questions of the set of data as a whole

In the Parse task, the pipeline has access to every single input file.

In the task we can ask two types of questions of the data:
* Something about a specific frame - becomes a flower and results in a tag on a frame
* Something about the data as a whole - becomes a bud and results in a pipeline constant

Either type of question can involve getting information about any number of frames, and to ask a new
question of the data we just add a new Flower or Bud to the parsing task. The goal is that at the
end of the Parse task the file tags are applied and the constants are populated so that we know
everything we need to know about the dataset as a whole and our data are organized in such a way
that makes the rest of the pipeline easy to write.

In other words, we can find exactly the frame we need (tags) and, once we have it, we never need to look
at a different frame to get information (constants).
"""
import json
import logging
from typing import TypeVar

from dkist_processing_common.models.constants import BudName
from dkist_processing_common.models.flower_pot import FlowerPot
from dkist_processing_common.models.flower_pot import Stem
from dkist_processing_common.models.flower_pot import Thorn
from dkist_processing_common.models.tags import Tag
from dkist_processing_common.parsers.l0_fits_access import L0FitsAccess
from dkist_processing_common.parsers.proposal_id_bud import ProposalIdBud
from dkist_processing_common.parsers.time import AverageCadenceBud
from dkist_processing_common.parsers.time import MaximumCadenceBud
from dkist_processing_common.parsers.time import MinimumCadenceBud
from dkist_processing_common.parsers.time import TaskExposureTimesBud
from dkist_processing_common.parsers.time import VarianceCadenceBud
from dkist_processing_common.parsers.unique_bud import UniqueBud
from dkist_processing_common.tasks.base import WorkflowTaskBase
from dkist_processing_common.tasks.mixin.fits import FitsDataMixin
from dkist_processing_common.tasks.mixin.input_dataset import InputDatasetMixin


__all__ = ["ParseL0InputData"]


logger = logging.getLogger(__name__)
S = TypeVar("S", bound=Stem)


class ParseL0InputData(WorkflowTaskBase, InputDatasetMixin, FitsDataMixin):
    """Common task to populate pipeline Constants and group files with tags by scanning headers."""

    @property
    def constant_flowers(self) -> list[S]:
        """Define the constants used."""
        return [
            UniqueBud(constant_name=BudName.instrument.value, metadata_key="instrument"),
            ProposalIdBud(),
            AverageCadenceBud(),
            MaximumCadenceBud(),
            MinimumCadenceBud(),
            VarianceCadenceBud(),
            TaskExposureTimesBud(stem_name=BudName.dark_exposure_times.value, ip_task_type="dark"),
        ]

    @property
    def tag_flowers(self) -> list[S]:
        """Define the Tags to apply."""
        return []

    @property
    def fits_parsing_class(self):
        """Class used to parse the input data."""
        return L0FitsAccess

    def run(self) -> None:
        """Run method for this task."""
        with self.apm_task_step("Check that input frames exist"):
            self.check_input_frames()

        with self.apm_task_step("Ingest all input files"):
            tag_pot, constant_pot = self.make_flower_pots()

        with self.apm_task_step("Update constants"):
            self.update_constants(constant_pot)

        with self.apm_task_step("Tag files"):
            self.tag_petals(tag_pot)

    def make_flower_pots(self) -> tuple[FlowerPot, FlowerPot]:
        """Ingest all headers."""
        tag_pot = FlowerPot()
        constant_pot = FlowerPot()
        tag_pot.flowers += self.tag_flowers
        constant_pot.flowers += self.constant_flowers

        for fits_obj in self.input_frames:
            filepath = fits_obj.name
            tag_pot.add_dirt(filepath, fits_obj)
            constant_pot.add_dirt(filepath, fits_obj)

        return tag_pot, constant_pot

    @property
    def input_frames(self):
        """Return a fits access generator containing the input fits objects."""
        return self.fits_data_read_fits_access(
            tags=[Tag.input(), Tag.frame()], cls=self.fits_parsing_class
        )

    def check_input_frames(self):
        """Make sure that at least one tagged frame exists before doing anything else."""
        if self.scratch.count_all(tags=[Tag.input(), Tag.frame()]) == 0:
            raise ValueError("No frames were tagged with INPUT and FRAME")

    def update_constants(self, constant_pot: FlowerPot):
        """
        Update pipeline Constants.

        Parameters
        ----------
        constant_pot
            The flower pot to be updated
        Returns
        -------
        None
        """
        for flower in constant_pot:
            with self.apm_processing_step(f"Setting value of constant {flower.stem_name}"):
                logging.info(f"Setting value of constant {flower.stem_name}")
                try:
                    if flower.bud.value is Thorn:
                        # Must've been a picky bud that passed. We don't want to pick it because it has no value
                        continue
                    # If the value is a set, sort it before storing in redis
                    if isinstance(flower.bud.value, set):
                        sorted_value = json.dumps(sorted(flower.bud.value))
                        self.constants._update({flower.stem_name: sorted_value})
                        logging.info(f"Value of {flower.stem_name} set to {sorted_value}")
                    else:
                        self.constants._update({flower.stem_name: flower.bud.value})
                        logging.info(f"Value of {flower.stem_name} set to {flower.bud.value}")
                except StopIteration:
                    # There are no petals
                    pass

    def tag_petals(self, tag_pot: FlowerPot):
        """
        Apply tags to file paths.

        Parameters
        ----------
        tag_pot
            The flower pot to be tagged
        Returns
        -------
        None
        """
        for flower in tag_pot:
            with self.apm_processing_step(f"Applying {flower.stem_name} tag to files"):
                logging.info(f"Applying {flower.stem_name} tag to files")
                for petal in flower.petals:
                    tag = Tag.format_tag(flower.stem_name, petal.value)
                    for path in petal.keys:
                        self.tag(path, tag)
