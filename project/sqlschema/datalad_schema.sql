

CREATE TABLE "Dataset" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	homepage TEXT, 
	last_updated TEXT, 
	license TEXT, 
	title TEXT, 
	version TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "DatasetCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "File" (
	checksum_md5 TEXT, 
	path_posix TEXT, 
	size_in_bytes INTEGER, 
	url TEXT, 
	"Dataset_identifier" TEXT, 
	PRIMARY KEY (checksum_md5, path_posix, size_in_bytes, url, "Dataset_identifier"), 
	FOREIGN KEY("Dataset_identifier") REFERENCES "Dataset" (identifier)
);

CREATE TABLE "Person" (
	email TEXT, 
	name TEXT, 
	"Dataset_identifier" TEXT, 
	PRIMARY KEY (email, name, "Dataset_identifier"), 
	FOREIGN KEY("Dataset_identifier") REFERENCES "Dataset" (identifier)
);

CREATE TABLE "Dataset_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (identifier)
);
