from __future__ import annotations

from typing import Callable, Iterator

from ms2ml.annotation_classes import RetentionTime
from ms2ml.config import Config
from ms2ml.data.adapters.base import BaseAdapter
from ms2ml.data.parsing import EncyclopeDIAParser
from ms2ml.peptide import Peptide
from ms2ml.spectrum import AnnotatedPeptideSpectrum


class EncyclopeDIAAdapter(BaseAdapter):
    """Implements an adapter that reads bibliospec files

    Args:
        file (str): Path to the .elib or .dlib file
        config (Config): The config object
        in_hook (Callable, optional):
            A function to apply to each element before processing. Defaults to None.
        out_hook (Callable, optional):
            A function to apply to each element after processing. Defaults to None.
        collate_fn (Callable, optional):
            A function to collate the elements. Defaults to list.

    """

    def __init__(
        self,
        file: str,
        config: Config,
        in_hook: Callable | None = None,
        out_hook: Callable | None = None,
        collate_fn: Callable = list,
    ):
        BaseAdapter.__init__(
            self,
            config=config,
            in_hook=in_hook,
            out_hook=out_hook,
            collate_fn=collate_fn,
        )
        self.parser = EncyclopeDIAParser(file)

    def _to_elem(self, spec_dict) -> AnnotatedPeptideSpectrum:
        """
        Converts a dictionary to an AnnotatedPeptideSpectrum object.
        It is implicitly called by the _process_elem method.

        Args:
            spec_dict (dict): A dictionary containing the information for a spectrum.
                usually the result of parsing an msp file using their MSP parser.
        """
        mz = spec_dict.pop("MassArray")
        intensity = spec_dict.pop("IntensityArray")
        rt = RetentionTime(spec_dict.pop("RTInSeconds"), "s")

        precursor_mz = spec_dict.pop("PrecursorMz")

        peptide_mod_seq = (
            f'{spec_dict.pop("PeptideModSeq")}/{spec_dict.pop("PrecursorCharge")}'
        )

        pep = Peptide.from_proforma_seq(peptide_mod_seq, config=self.config)
        spec = AnnotatedPeptideSpectrum(
            mz=mz,
            intensity=intensity,
            ms_level=2,  # Is this a valid assumption?
            precursor_mz=precursor_mz,
            precursor_peptide=pep,
            extras=spec_dict,
            retention_time=rt,
            config=self.config,
        )

        return spec

    def parse(self) -> Iterator[AnnotatedPeptideSpectrum]:
        for spec in self.parser.parse():
            out = self._process_elem(spec)
            yield out

    def parse_file(self, file) -> Iterator[AnnotatedPeptideSpectrum]:
        for spec in self.parser.parse_file(file):
            yield self._process_elem(spec)
