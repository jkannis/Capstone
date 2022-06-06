-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Species" (
    "speciesName" varchar   NOT NULL,
    "speciesCode" int   NOT NULL,
    CONSTRAINT "pk_Species" PRIMARY KEY (
        "speciesCode"
     )
);

CREATE TABLE "coffeeQualities" (
    "index" int   NOT NULL,
    "Species" int   NOT NULL,
    "Aroma" int   NOT NULL,
    "Flavor" int   NOT NULL,
    "Aftertaste" int   NOT NULL,
    "Acidity" int   NOT NULL,
    "Body" int   NOT NULL,
    "Balance" int   NOT NULL,
    "Uniformity" int   NOT NULL,
    "Clean.Cup" int   NOT NULL,
    "Sweetness" int   NOT NULL,
    "Cupper.Points" int   NOT NULL,
    "Total.Cup.Points" int   NOT NULL,
    "Moisture" int   NOT NULL,
    "altitude_low_meters" int   NOT NULL,
    "altitude_high_meters" int   NOT NULL,
    "altitude_mean_meters" int   NOT NULL,
    CONSTRAINT "pk_coffeeQualities" PRIMARY KEY (
        "index"
     )
);

ALTER TABLE "Species" ADD CONSTRAINT "fk_Species_speciesCode" FOREIGN KEY("speciesCode")
REFERENCES "coffeeQualities" ("Species");

