#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BioCypher - Monarch Gene/Phenotype adapter prototype
"""

from enum import StrEnum

class EnumWithValuesList(StrEnum):
    """
    Enum with method returning a list of the values
    """
    @classmethod
    def valueList(cls):
        return list(map(lambda c: c.value, cls))

class EnumForFields(EnumWithValuesList):
    """
    EnumWithValuesList with default empty mappings
    """
    __PROPERTY_MAPPING__ = {}
    __EDGE_MAPPING__ = {}
