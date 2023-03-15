#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BioCypher - Monarch Gene/Phenotype adapter prototype
"""

import csv
from itertools import islice
from .adapter_enums import *
from ._adapter_enums_merged import NamedThingFieldMerged, AssociationFieldMerged

from biocypher._logger import logger

logger.debug(f"Loading module {__name__}.")

class MonarchGenePhenotypeAdapter:
    def __init__(
        self,
        id_batch_size: int = int(1e6),
        node_types: list = NamedThingType.valueList(),
        node_fields: list = NamedThingFieldMerged.valueList(),
        edge_types:list = AssociationType.valueList(),
        edge_fields: list = AssociationFieldMerged.valueList(),
        test_mode: bool = False,
    ):

        self.id_batch_size = id_batch_size

        self.node_types = node_types
        self.node_fields = node_fields
        self.edge_types = edge_types
        self.edge_fields = edge_fields

        self.test_mode = test_mode

        self.data_source = "Monarch"
        self.data_version = "v0.1"
        self.data_licence = "None"

        self.nodes_location = "data/gene_phenotype.all.tsv"
        self.edges_location = "data/gene_phenotype.all.tsv"

    def get_nodes(self):
        """
        Get nodes from csv and yield them to the batch writer.

        Args:
            label: input label of nodes to be read

        Returns:
            generator of tuples representing nodes
        """

        with (open(self.nodes_location, "r")) as f:

            reader = csv.DictReader(f, delimiter='\t')
            _ = next(reader)

            if self.test_mode:
                reader = islice(reader, 0, 100)

            for row in reader:

                if self._skip_node_row(row):
                    continue

                for node_type in self.node_types:
                    fields_enum = NamedThingType.__FIELD_ENUM_MAPPING__[node_type]

                    _id = self._process_node_id(row[fields_enum._PRIMARY_ID], node_type)
                    _label = node_type
                    _props, _edges = self._process_node_fields(
                        row,
                        fields_enum.valueList(),
                        fields_enum.__PROPERTY_MAPPING__, 
                        fields_enum.__EDGE_MAPPING__,                        
                    )

                    yield _id, _label, _props, _edges

    def get_edges(self):
        """
        Get edges from csv and yield them to the batch writer.

        Args:
            label: input label of edges to be read

        Returns:
            generator of tuples representing edges
        """

        with (open(self.edges_location, "r")) as f:

            reader = csv.DictReader(f, delimiter='\t')
            _ = next(reader)

            if self.test_mode:
                reader = islice(reader, 0, 100)

            for row in reader:

                if self._skip_edge_row(row):
                    continue

                for edge_type in self.edge_types:
                    fields_enum = AssociationType.__FIELD_ENUM_MAPPING__[edge_type]

                    _src = self._process_source_id(row[fields_enum._PRIMARY_SOURCE_ID], edge_type)
                    _tar = self._process_target_id(row[fields_enum._PRIMARY_TARGET_ID], edge_type)
                    _label = edge_type
                    _props = self._process_edge_fields(
                        row, 
                        fields_enum.valueList(),
                        fields_enum.__PROPERTY_MAPPING__,
                        )

                    if not _src or not _tar:
                        continue

                    yield _src, _tar, _label, _props

    def _skip_node_row(self, _props):
        """
        Returns true if the node row must be skipped
        """

        return self._skip_row(_props)

    def _skip_edge_row(self, _props):
        """
        Returns true if the edge row must be skipped
        """

        return self._skip_row(_props)

    def _skip_row(self, _props):
        """
        Returns true if the row must be skipped
        """

        if _props.get(GeneField.GENE_TAXON_CURIE) == "NCBITaxon:10090" or _props.get(GeneField.GENE_TAXON_CURIE) == "NCBITaxon:9606":
            return False

        return True

    def _process_node_fields(self, _props, fields, property_mapping, edge_mapping):
        """
        Process node fields.
        """
        
        return self._process_fields(_props, fields, self.node_fields, property_mapping, edge_mapping)

    def _process_edge_fields(self, _props, fields, property_mapping):
        """
        Process edge fields.
        """

        props, _ = self._process_fields(_props, fields, self.edge_fields, property_mapping)
        return props

    def _process_fields(self, _props, fields, global_fields, property_mapping, edge_mapping = {}):
        """
        Process general fields.
        """

        _processed_props = {}
        _processed_edges = {}

        for key, value in _props.items():

            if key not in fields or key not in global_fields:
                continue

            #if key == GeneField.GENE_SYMBOL:
            #    ...

            # workaround for (single and double) quote escape problems
            # TODO identify problem and create issue
            value = value.replace("'", "''").replace('"', '""')

            # TODO split values to obtain list if necessary

            _prop_key = property_mapping.get(key) or key
            _processed_props[_prop_key] = value

            _edge_key = edge_mapping.get(key)
            if _edge_key:
                _processed_edges[_edge_key] = value 

        #  generic source, version and licence
        #_processed_props["source"] = self.data_source
        #_processed_props["version"] = self.data_version
        #_processed_props["licence"] = self.data_licence

        return _processed_props, _processed_edges

    def _process_source_id(self, _id, _type):
        """
        Nothing to do currently
        """

        return _id

    def _process_target_id(self, _id, _type):
        """
        Nothing to do currently
        """

        return _id

    def _process_node_id(self, _id, _type):
        """
        Nothing to do currently
        """

        return _id

    def _process_edge_id(self, _id, _type):
        """
        Nothing to do currently
        """

        return _id
