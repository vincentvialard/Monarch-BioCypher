The script assumes the presence of an uncompressed version of the tsv file in the data
folder. The latest version of the file can be obtained at:

https://data.monarchinitiative.org/latest/tsv/gene_associations/gene_phenotype.all.tsv.gz

# Header of TSV file:

subject	subject_label	subject_taxon	subject_taxon_label	object	object_label	relation	relation_label	evidence	evidence_label	source	is_defined_by	qualifier

# TSV Glossary of Terms:

subject: The curie formatted identifier for the subject of the association (gene, disease, variant).
subject_label: Label of the subject of the association.
subject_taxon: Taxonomic class of the subject. This is typically a CURIE of the form NCBITaxon:nnnn.
subject_taxon_label: Label of subject taxon.
object: The curie formatted identifier for the object of the association (disease, phenotype).
object_label: Label of the object of the association.
object_taxon: Taxonomic class of the object. This is typically a CURIE of the form NCBITaxon:nnnn.
object_taxon_label: Label of object taxon.
relation: A relationship type that connects the subject with object.
relation_label: Label for relation.
evidence: Evidence type. In Monarch we may have a chain of assertions that link two entites/terms. This is a list of all evidence types used in that chain.
evidence_label: Labels for each evidence code.
source: The RDF sources used to create the association.
is_defined_by: Associations are obtained from the source(s) listed. More than one source indicates the
               association may be derived from connecting data from multiple sources, or multiple sources
               have corroborated the same assertion.
qualifier: Qualifies if the underlying query makes a direct connection or is inferred across multiple
           associations, eg gene to phenotype inferred across gene to disease and disease to phenotype.
