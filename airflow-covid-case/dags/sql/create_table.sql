-- Create Dimension tables
CREATE TABLE IF NOT EXISTS dim_province (
    province_id text,
    province_name text
);

CREATE TABLE IF NOT EXISTS dim_district (
    district_id text,
    province_id text,
    district_name text
);

CREATE TABLE IF NOT EXISTS dim_case (
    Id serial, 
    status_name text,
    status_detail text
);

-- Create Fact tables
CREATE TABLE IF NOT EXISTS fact_province_daily (
    Id serial,
    province_id text,
    case_id int,
    date text,
    total bigint
);

CREATE TABLE IF NOT EXISTS fact_province_monthly (
    Id serial, 
    province_id text,
    case_id int, 
    month text,
    total bigint
);

CREATE TABLE IF NOT EXISTS fact_province_yearly (
    Id serial,
    province_id text,
    case_id int,
    year text,
    total bigint
);

CREATE TABLE IF NOT EXISTS fact_district_monthly (
    Id serial,
    district_id text,
    case_id int,
    month text,
    total bigint
);

CREATE TABLE IF NOT EXISTS fact_district_yearly (
    Id serial,
    district_id text,
    case_id int,
    year text,
    total bigint
);

CREATE TABLE IF NOT EXISTS temp_fact (
    province_id text,
    district_id text, 
    date date,
    "case" text,
    total bigint
);