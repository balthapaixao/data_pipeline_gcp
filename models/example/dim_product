{{ config(materialized='table') }}

with source_data as (
    SELECT
  CAST(ProductId AS INTEGER) AS dky_product,
  CASE
    WHEN ProductId=1 THEN "BOOK"
    WHEN ProductId=2 THEN 'PENCIL'
    WHEN ProductId=3 THEN "PEN"
    WHEN ProductId=4 THEN "NOTEBOOK"
    WHEN ProductId=5 THEN 'ERASER'
    WHEN ProductId=6 THEN "CASE"
    WHEN ProductId=7 THEN "BACKPACK"
  ELSE
  "N/A"
END
  AS des_product
FROM
  `cloud-portfolio-dev.Business.Orders`
GROUP BY
  ProductId
ORDER BY
  ProductId
)
select * from source_data