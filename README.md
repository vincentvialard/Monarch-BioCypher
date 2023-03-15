# Monarch-BioCypher

This is a work in progress BioCypher adapter for the tsv files of the
[Monarch Initiative](https://monarchinitiative.org/).
It currently serves as an experimental platform for the conception of a
mapping configuration and adapter structure template.

It currently relies on an [experimental feature branch](https://github.com/vincentvialard/BioCypher/tree/nodes-with-edges) of a fork of the [BioCypher project](https://github.com/saezlab/BioCypher). The branch should get merged to the main project in the near future.

At the time being only the gene to phenotype file is mapped and the adapter retains
only the lines for mice and men (taxon ids 10090 and 9606) to match the pipeline of
the german center for diabetes research (see [here](https://www.dzd-ev.de/)).

The script assumes the presence of an uncompressed version of the tsv file in the data
folder (`data/gene_phenotype.all.tsv`). The latest version of the file can be obtained at:

[https://data.monarchinitiative.org/latest/tsv/gene_associations/gene_phenotype.all.tsv.gz](https://data.monarchinitiative.org/latest/tsv/gene_associations/gene_phenotype.all.tsv.gz)

The adapter (`adapter.py`) currently only generates `neo4j-admin import`-ready
files via the batch writer class (to `biocypher-out` or any specified location).

The process can be run using `script.py`. If all
goes well, the output folder will contain a `neo4j-admin-import-call.sh`
file which, when run in the terminal in the database folder, will create
a new database under the name specified in the `db_name` argument of the
`BioCypherAdapter` instantiation in `script.py`. The database does not
need to be running at this point (but it can). However, it is important
that the target database (in the current example the one named "import")
is either completely empty or does not exist yet.

After import, and in case the database in point did not exist yet, the
database can be created and activated in the Neo4j browser with `:use
system`, `create database monarch`, `:use monarch`. At this point,
the DBMS needs to be running.

## Installation

The project can be installed using poetry:

```shell
git clone https://github.com/vincentvialard/Monarch-BioCypher.git
cd Monarch-BioCypher
poetry install
```
