 
 CREATE EXTENSION postgis
  SCHEMA public;
/*
CREATE TABLE inwater_021215 (
    gid integer,
    agency_type character varying(200),
    agency_organization character varying(200),
    name character varying(200),
    site_no character varying(200),
    description character varying(1000),
    parameter_type character varying(1000),
    parameter character varying(10000),
    frequency character varying(100),
    publicly_available character varying(10),
    start_date character varying(10),
    end_date character varying(10),
    contact_url character varying(1000),
    id double precision,
    quality character varying(10),
    user_email character varying(200),
    huc_8 character varying(8),
    huc_10 character varying(10),
    huc_12 character varying(12),
    clipped_geom geometry
);

insert into inwater_monitoring(gid,agency_type,agency_organization,name,site_no,description,parameter_type,parameter,frequency,publicly_available,start_date,end_date,contact_url,quality,user_email,huc_8,huc_10,huc_12,clipped_geom) select gid,agency_type,agency_organization,name,site_no,description,parameter_type,parameter,frequency,publicly_available,start_date,end_date,contact_url,quality,user_email,huc_8,huc_10,huc_12,clipped_geom from inwater_021215;
*/
ALTER table inwater_monitoring ALTER COLUMN clipped_geom TYPE geometry;

CREATE INDEX geoindex
  ON inwater_monitoring
  USING gist
  (clipped_geom);
