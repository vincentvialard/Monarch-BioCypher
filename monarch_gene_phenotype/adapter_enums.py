#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BioCypher - Monarch Gene/Phenotype adapter prototype
"""

from ._adapter_enum_utils import EnumForFields, EnumWithValuesList

#
# Named Things
#

class GeneField(EnumForFields):
    """
    Fields available in input for the genes with 
    - mapping to the output properties
    - mapping to the output edges
    - identification of the ID field

    Mapping based on:
    - input: https://data.monarchinitiative.org/README.txt
    - output: https://biolink.github.io/biolink-model/docs/Gene.html
    """
    GENE_CURIE = "subject"
    GENE_SYMBOL = "subject_label"
    GENE_TAXON_CURIE = "subject_taxon"
    __PROPERTY_MAPPING__ = {
        GENE_CURIE: "id",
        GENE_SYMBOL: "name",
        GENE_TAXON_CURIE: "in_taxon", # here both as property and edge to demonstrate it is possible
    }
    __EDGE_MAPPING__ = {
        GENE_TAXON_CURIE: "in_taxon", # here both as property and edge to demonstrate it is possible
    }
    _PRIMARY_ID = GENE_CURIE

class PhenotypeField(EnumForFields):
    """
    Fields available in input for the taxons with 
    - mapping to the output properties
    - mapping to the output edges (currently empty)
    - identification of the ID field

    Mapping based on:
    - input: https://data.monarchinitiative.org/README.txt
    - output: https://biolink.github.io/biolink-model/docs/PhenotypicFeature.html
    """
    PHENOTYPE_CURIE = "object"
    PHENOTYPE_LABEL = "object_label"
    __PROPERTY_MAPPING__ = {
        PHENOTYPE_CURIE: "id",
        PHENOTYPE_LABEL: "name",
    }
    _PRIMARY_ID = PHENOTYPE_CURIE

class TaxonField(EnumForFields):
    """
    Fields available in input for the taxons with 
    - mapping to the output properties
    - mapping to the output edges (currently empty)
    - identification of the ID field

    Mapping based on:
    - input: https://data.monarchinitiative.org/README.txt
    - output: https://biolink.github.io/biolink-model/docs/OrganismTaxon.html
    """
    TAXON_CURIE = "subject_taxon"
    TAXON_LABEL = "subject_taxon_label"
    __PROPERTY_MAPPING__ = {
        TAXON_CURIE: "id",
        TAXON_LABEL: "name",
    }
    _PRIMARY_ID = TAXON_CURIE        

class NamedThingType(EnumWithValuesList):
    """
    All NamedThings with mapping to their associated field enums.
    """
    GENE = "gene"
    PHENOTYPE = "phenotype"
    TAXON = "taxon"
    __FIELD_ENUM_MAPPING__ = {
        GENE: GeneField,
        PHENOTYPE: PhenotypeField,
        TAXON: TaxonField,
    }

#
# Associations
#

class GeneToPhenotypeField(EnumForFields):
    """
    Fields available in input for the gene to phenotype associations with 
    - mapping to the output properties
    - mapping to the output edges (currently empty)
    - identification of the source and target ID fields

    Mapping based on:
    - input: https://data.monarchinitiative.org/README.txt
    - output: https://biolink.github.io/biolink-model/docs/GeneToPhenotypicFeatureAssociation.html
    """
    EVIDENCE_CURIE = "evidence"
    EVIDENCE_LABEL = "evidence_label"
    SOURCE_CURIE = "source"
    DEFINED_BY = "is_defined_by"
    QUALIFIER = "qualifier"
    __PROPERTY_MAPPING__ = {
        EVIDENCE_CURIE: "has evidence",    # here only as property, TODO should be an array
        EVIDENCE_LABEL: "_evidence_label", # more human friendly (not in biolink)
        SOURCE_CURIE: "publications",      # here only as property, TODO should be an array
        DEFINED_BY: "knowledge source",    # here only as property
        QUALIFIER: "_qualifier",           # biolink qualifiers require a class, we have just a text
    }
    _PRIMARY_SOURCE_ID = GeneField._PRIMARY_ID
    _PRIMARY_TARGET_ID = PhenotypeField._PRIMARY_ID

class AssociationType(EnumWithValuesList):
    """
    All Associations with mapping to their associated field enums.
    """
    GENE_TO_PHENOTYPE = "gene to phenotype"
    __FIELD_ENUM_MAPPING__ = {
        GENE_TO_PHENOTYPE: GeneToPhenotypeField,
    }

