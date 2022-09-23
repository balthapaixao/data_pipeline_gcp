
{{ config(materialized='table') }}

with source_data as (

SELECT
  CAST(FORMAT_DATETIME('%Y%m%d', CreationDate) AS STRING) AS dky_day,
  CAST(OrderStatus AS INTEGER) AS dky_status,
  CAST(ProductId AS INTEGER) AS dky_product,
  COUNT(OrderStatus) AS qty_orders,
  SUM(ProductPrice) AS num_price,
  COUNT(DISTINCT CustomerId) AS qty_distinct_customers,
  COUNT(CustomerId) AS qty_customers,
  COUNT(CASE
      WHEN OrderId=4 THEN 1
    ELSE
    0
  END
    ) AS qty_closed_orders,
FROM
  `cloud-portfolio-dev.Business.Orders`
GROUP BY
  dky_day,
  dky_status,
  dky_product
ORDER BY
  dky_day,
  dky_status,
  dky_product
)
select * from source_data