BEGIN;
CREATE TABLE "stepl_countydata" ("id" serial NOT NULL PRIMARY KEY, "state_name" varchar(30) NOT NULL, "name" varchar(30) NOT NULL, "rmean" double precision NULL, "kmean" double precision NULL, "lsavg" double precision NULL, "cavg" double precision NULL, "pavg" double precision NULL, "state_name_name" varchar(30) NOT NULL, "rainfall_inches" double precision NOT NULL, "raindays" double precision NOT NULL, "runoff" double precision NOT NULL, "station_name" varchar(30) NULL, "ptrecipitation_correction_factor" double precision NULL, "no_of_rain_days_correction_factor" double precision NULL);
CREATE TABLE "stepl_countydatainput" ("id" serial NOT NULL PRIMARY KEY, "state_name" varchar(30) NOT NULL, "name" varchar(30) NOT NULL, "rmean" double precision NULL, "kmean" double precision NULL, "lsavg" double precision NULL, "cavg" double precision NULL, "pavg" double precision NULL, "index_id" varchar(30) NOT NULL);
CREATE TABLE "stepl_indexinput" ("id" serial NOT NULL PRIMARY KEY, "num_watershd" integer NOT NULL, "num_gully" integer NOT NULL, "num_steambank" integer NOT NULL);
ALTER TABLE "stepl_countydatainput" ADD CONSTRAINT "stepl_countydatainput_state_name_300640b7fbf2b38e_uniq" UNIQUE ("state_name", "name");
ALTER TABLE "stepl_countydata" ADD CONSTRAINT "stepl_countydata_state_name_6d046ab3e35504eb_uniq" UNIQUE ("state_name", "name");

COMMIT;
