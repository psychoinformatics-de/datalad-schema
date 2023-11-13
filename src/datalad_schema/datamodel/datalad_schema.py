# Auto generated from datalad_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-11-13T11:44:11
# Schema: datalad-schema
#
# id: https://w3id.org/psychoinformatics-de/datalad-schema
# description: DataLad dataset schema
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
AFO = CurieNamespace('afo', 'http://purl.allotrope.org/ontologies/result#')
DATALAD_SCHEMA = CurieNamespace('datalad_schema', 'https://w3id.org/psychoinformatics-de/datalad-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'https://purl.obolibrary.org/obo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX = CurieNamespace('spdx', 'https://spdx.org/licenses/')
DEFAULT_ = DATALAD_SCHEMA


# Types

# Class references
class NamedThingIdentifier(extended_str):
    pass


class DatasetIdentifier(NamedThingIdentifier):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = DATALAD_SCHEMA.NamedThing

    identifier: Union[str, NamedThingIdentifier] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, NamedThingIdentifier):
            self.identifier = NamedThingIdentifier(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DATALAD_SCHEMA.Dataset

    identifier: Union[str, DatasetIdentifier] = None
    authors: Optional[Union[Union[dict, "Person"], List[Union[dict, "Person"]]]] = empty_list()
    hasPart: Optional[Union[Union[dict, "File"], List[Union[dict, "File"]]]] = empty_list()
    homepage: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    last_updated: Optional[str] = None
    license: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, DatasetIdentifier):
            self.identifier = DatasetIdentifier(self.identifier)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.authors]

        if not isinstance(self.hasPart, list):
            self.hasPart = [self.hasPart] if self.hasPart is not None else []
        self.hasPart = [v if isinstance(v, File) else File(**as_dict(v)) for v in self.hasPart]

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class File(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DigitalDocument"]
    class_class_curie: ClassVar[str] = "schema:DigitalDocument"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = DATALAD_SCHEMA.File

    checksum_md5: Optional[str] = None
    path_posix: Optional[str] = None
    size_in_bytes: Optional[int] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.checksum_md5 is not None and not isinstance(self.checksum_md5, str):
            self.checksum_md5 = str(self.checksum_md5)

        if self.path_posix is not None and not isinstance(self.path_posix, str):
            self.path_posix = str(self.path_posix)

        if self.size_in_bytes is not None and not isinstance(self.size_in_bytes, int):
            self.size_in_bytes = int(self.size_in_bytes)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = DATALAD_SCHEMA.Person

    email: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class DatasetCollection(YAMLRoot):
    """
    A holder for Dataset objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATALAD_SCHEMA["DatasetCollection"]
    class_class_curie: ClassVar[str] = "datalad_schema:DatasetCollection"
    class_name: ClassVar[str] = "DatasetCollection"
    class_model_uri: ClassVar[URIRef] = DATALAD_SCHEMA.DatasetCollection

    entries: Optional[Union[Dict[Union[str, DatasetIdentifier], Union[dict, Dataset]], List[Union[dict, Dataset]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Dataset, key_name="identifier", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.authors = Slot(uri=SCHEMA.author, name="authors", curie=SCHEMA.curie('author'),
                   model_uri=DATALAD_SCHEMA.authors, domain=None, range=Optional[Union[Union[dict, Person], List[Union[dict, Person]]]])

slots.checksum_md5 = Slot(uri=OBO.NCIT_C171276, name="checksum_md5", curie=OBO.curie('NCIT_C171276'),
                   model_uri=DATALAD_SCHEMA.checksum_md5, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DATALAD_SCHEMA.description, domain=None, range=Optional[str])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=DATALAD_SCHEMA.email, domain=None, range=Optional[str])

slots.hasPart = Slot(uri=SCHEMA.hasPart, name="hasPart", curie=SCHEMA.curie('hasPart'),
                   model_uri=DATALAD_SCHEMA.hasPart, domain=None, range=Optional[Union[Union[dict, File], List[Union[dict, File]]]])

slots.homepage = Slot(uri=SCHEMA.version, name="homepage", curie=SCHEMA.curie('version'),
                   model_uri=DATALAD_SCHEMA.homepage, domain=None, range=Optional[str])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=DATALAD_SCHEMA.identifier, domain=None, range=URIRef)

slots.keywords = Slot(uri=SCHEMA.keywords, name="keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=DATALAD_SCHEMA.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.last_updated = Slot(uri=SCHEMA.dateModified, name="last-updated", curie=SCHEMA.curie('dateModified'),
                   model_uri=DATALAD_SCHEMA.last_updated, domain=None, range=Optional[str])

slots.license = Slot(uri=SCHEMA.license, name="license", curie=SCHEMA.curie('license'),
                   model_uri=DATALAD_SCHEMA.license, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DATALAD_SCHEMA.name, domain=None, range=Optional[str])

slots.path_posix = Slot(uri=AFO.AFR_0001928, name="path_posix", curie=AFO.curie('AFR_0001928'),
                   model_uri=DATALAD_SCHEMA.path_posix, domain=None, range=Optional[str])

slots.size_in_bytes = Slot(uri=SCHEMA.contentSize, name="size_in_bytes", curie=SCHEMA.curie('contentSize'),
                   model_uri=DATALAD_SCHEMA.size_in_bytes, domain=None, range=Optional[int])

slots.title = Slot(uri=SCHEMA.title, name="title", curie=SCHEMA.curie('title'),
                   model_uri=DATALAD_SCHEMA.title, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.contentUrl, name="url", curie=SCHEMA.curie('contentUrl'),
                   model_uri=DATALAD_SCHEMA.url, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=DATALAD_SCHEMA.version, domain=None, range=Optional[str])

slots.datasetCollection__entries = Slot(uri=DATALAD_SCHEMA.entries, name="datasetCollection__entries", curie=DATALAD_SCHEMA.curie('entries'),
                   model_uri=DATALAD_SCHEMA.datasetCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, DatasetIdentifier], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.Person_email = Slot(uri=SCHEMA.email, name="Person_email", curie=SCHEMA.curie('email'),
                   model_uri=DATALAD_SCHEMA.Person_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))