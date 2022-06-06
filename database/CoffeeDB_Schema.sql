-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "species" (
    "species_name" varchar   NOT NULL,
    "species_code" int   NOT NULL,
    CONSTRAINT "pk_species" PRIMARY KEY (
        "species_name"
     )
);

CREATE TABLE "robusta_ratings" (
    "rec_id" int   NOT NULL,
    "species" varchar   NOT NULL,
    "owner" varchar   NOT NULL,
    "country_of_origin" varchar   NOT NULL,
    "altitude" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "harvest_year" date   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "body" int   NOT NULL,
    "balance" int   NOT NULL,
    "uniformity" int   NOT NULL,
    "clean_cup" int   NOT NULL,
    "sweetness" int   NOT NULL,
    "cupper_points" int   NOT NULL,
    "total_cup_points" varchar   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_robusta_ratings" PRIMARY KEY (
        "rec_id"
     )
);

CREATE TABLE "arabica_ratings" (
    "rec_id" int   NOT NULL,
    "species" varchar   NOT NULL,
    "owner" varchar   NOT NULL,
    "country_of_origin" varchar   NOT NULL,
    "altitude" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "harvest_year" date   NOT NULL,
    "aroma" int   NOT NULL,
    "flavor" int   NOT NULL,
    "aftertaste" int   NOT NULL,
    "acidity" int   NOT NULL,
    "body" int   NOT NULL,
    "balance" int   NOT NULL,
    "uniformity" int   NOT NULL,
    "clean_cup" int   NOT NULL,
    "sweetness" int   NOT NULL,
    "cupper_points" int   NOT NULL,
    "total_cup_points" varchar   NOT NULL,
    "moisture" int   NOT NULL,
    CONSTRAINT "pk_arabica_ratings" PRIMARY KEY (
        "rec_id"
     )
);

CREATE TABLE "regions" (
    "index" int   NOT NULL,
    "country" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "altitude" varchar   NOT NULL,
    "latitude" int   NOT NULL,
    "longitude" int   NOT NULL,
    CONSTRAINT "pk_regions" PRIMARY KEY (
        "index"
     )
);

ALTER TABLE "robusta_ratings" ADD CONSTRAINT "fk_robusta_ratings_species" FOREIGN KEY("species")
REFERENCES "species" ("species_name");

ALTER TABLE "robusta_ratings" ADD CONSTRAINT "fk_robusta_ratings_country_of_origin" FOREIGN KEY("country_of_origin")
REFERENCES "regions" ("country");

ALTER TABLE "arabica_ratings" ADD CONSTRAINT "fk_arabica_ratings_species" FOREIGN KEY("species")
REFERENCES "species" ("species_name");

ALTER TABLE "arabica_ratings" ADD CONSTRAINT "fk_arabica_ratings_country_of_origin" FOREIGN KEY("country_of_origin")
REFERENCES "regions" ("country");

