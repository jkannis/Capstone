-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Species" (
    "speciesName" varchar   NOT NULL,
    "speciesCode" int   NOT NULL,
    CONSTRAINT "pk_Species" PRIMARY KEY (
        "speciesName"
     )
);

CREATE TABLE "RobustaRatings" (
    "recID" int   NOT NULL,
    "species" varchar   NOT NULL,
    "owner" varchar   NOT NULL,
    "countryOfOrigin" varchar   NOT NULL,
    "altitude" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "body" int   NOT NULL,
    "balance" int   NOT NULL,
    "uniformity" int   NOT NULL,
    "cleanCup" int   NOT NULL,
    "sweetness" int   NOT NULL,
    "cupperPoints" int   NOT NULL,
    "totalCupPoints" varchar   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_RobustaRatings" PRIMARY KEY (
        "recID"
     )
);

CREATE TABLE "ArabicaRatings" (
    "recID" int   NOT NULL,
    "species" varchar   NOT NULL,
    "owner" varchar   NOT NULL,
    "countryOfOrigin" varchar   NOT NULL,
    "altitude" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "body" int   NOT NULL,
    "balance" int   NOT NULL,
    "uniformity" int   NOT NULL,
    "cleanCup" int   NOT NULL,
    "sweetness" int   NOT NULL,
    "cupperPoints" int   NOT NULL,
    "totalCupPoints" varchar   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_ArabicaRatings" PRIMARY KEY (
        "recID"
     )
);

ALTER TABLE "RobustaRatings" ADD CONSTRAINT "fk_RobustaRatings_species" FOREIGN KEY("species")
REFERENCES "Species" ("speciesName");

ALTER TABLE "ArabicaRatings" ADD CONSTRAINT "fk_ArabicaRatings_species" FOREIGN KEY("species")
REFERENCES "Species" ("speciesName");

