#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BioCypher - Monarch Gene/Phenotype adapter prototype
"""

from ._adapter_enum_utils import EnumWithValuesList
from .adapter_enums import NamedThingType, AssociationType

class NamedThingFieldMerged(EnumWithValuesList): 
    """ 
    All fields available for nodes (all node types merged) 
    """
    _ignore_ = 'member cls'
    cls = vars()
    for member in [item 
            for enum in NamedThingType.__FIELD_ENUM_MAPPING__.values() 
            for item in list(enum)]:
        if not member.name.startswith('_PRIMARY_'):
            cls[member.name] = member.value 

class AssociationFieldMerged(EnumWithValuesList): 
    """ 
    All fields available for edges (all edge types merged) 
    """
    _ignore_ = 'member cls'
    cls = vars()
    for member in [item 
            for enum in AssociationType.__FIELD_ENUM_MAPPING__.values() 
            for item in list(enum)]:
        if not member.name.startswith('_PRIMARY_'):
            cls[member.name] = member.value 
