import biocypher
from monarch_gene_phenotype.adapter import (
    NamedThingType,
    NamedThingFieldMerged,
    AssociationType,
    AssociationFieldMerged,
    MonarchGenePhenotypeAdapter
)

# Configure node types and fields
# Can be used to remove some of them programmatically if required
node_types = NamedThingType.valueList
node_fields = NamedThingFieldMerged.valueList
edge_types = AssociationType.valueList
edge_fields = AssociationFieldMerged.valueList

def main():
    """
    Connect BioCypher to Monarch adapter to import data into Neo4j.
    """

    # start biocypher
    driver = biocypher.Driver()

    # check schema
    driver.show_ontology_structure()

    # create adapter

    # here default settings and full data
    adapter = MonarchGenePhenotypeAdapter()

    # example for testing only one node type:
    # adapter = MonarchGenePhenotypeAdapter(node_types=[NamedThingType.PHENOTYPE],edge_types=[],test_mode=True)

    # write nodes and edges to csv
    driver.write_nodes(adapter.get_nodes())
    driver.write_edges(adapter.get_edges())

    # convenience and stats
    driver.write_import_call()
    driver.log_missing_bl_types()
    driver.log_duplicates()

if __name__ == "__main__":
    main()
