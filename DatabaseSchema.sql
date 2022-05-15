-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Species" (
    "speciesName" varchar   NOT NULL,
    CONSTRAINT "pk_Species" PRIMARY KEY (
        "speciesName"
     )
);

CREATE TABLE "Countries" (
    "countryName" varchar   NOT NULL,
    CONSTRAINT "pk_Countries" PRIMARY KEY (
        "countryName"
     )
);

CREATE TABLE "Regions" (
    "regionName" varchar   NOT NULL,
    "country" varchar   NOT NULL,
    CONSTRAINT "pk_Regions" PRIMARY KEY (
        "regionName"
     )
);

CREATE TABLE "Partners" (
    "partnerName" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    CONSTRAINT "pk_Partners" PRIMARY KEY (
        "partnerName"
     )
);

CREATE TABLE "ArabicaRatings" (
    "recID" int   NOT NULL,
    "species" varchar   NOT NULL,
    "qualityScore" int   NOT NULL,
    "owner" varchar   NOT NULL,
    "countryOfOrigin" varchar   NOT NULL,
    "farmName" varchar   NOT NULL,
    "company" varchar   NOT NULL,
    "altitude" int   NOT NULL,
    "producer" varchar   NOT NULL,
    "inCountryPartner" varchar   NOT NULL,
    "harvestYear" int   NOT NULL,
    "variety" varchar   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "balance" int   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_ArabicaRatings" PRIMARY KEY (
        "recID"
     )
);

CREATE TABLE "RobustaRatings" (
    "recID" int   NOT NULL,
    "species" varchar   NOT NULL,
    "qualityScore" int   NOT NULL,
    "owner" varchar   NOT NULL,
    "countryOfOrigin" varchar   NOT NULL,
    "farmName" varchar   NOT NULL,
    "company" varchar   NOT NULL,
    "altitude" int   NOT NULL,
    "producer" varchar   NOT NULL,
    "inCountryPartner" varchar   NOT NULL,
    "harvestYear" int   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "balance" int   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_RobustaRatings" PRIMARY KEY (
        "recID"
     )
);

ALTER TABLE "Species" ADD CONSTRAINT "fk_Species_speciesName" FOREIGN KEY("speciesName")
REFERENCES "ArabicaRatings" ("species");

ALTER TABLE "Countries" ADD CONSTRAINT "fk_Countries_countryName" FOREIGN KEY("countryName")
REFERENCES "Regions" ("country");

ALTER TABLE "Regions" ADD CONSTRAINT "fk_Regions_regionName" FOREIGN KEY("regionName")
REFERENCES "Partners" ("region");

ALTER TABLE "Partners" ADD CONSTRAINT "fk_Partners_partnerName" FOREIGN KEY("partnerName")
REFERENCES "RobustaRatings" ("inCountryPartner");

