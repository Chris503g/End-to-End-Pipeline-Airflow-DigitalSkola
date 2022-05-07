TRUNCATE dim_province;
INSERT INTO dim_province
    SELECT distinct kode_prov, nama_prov from warehouse_table;

TRUNCATE dim_district;
INSERT INTO dim_district
    SELECT distinct kode_kab, kode_prov, nama_kab from warehouse_table
    order by kode_kab asc;
