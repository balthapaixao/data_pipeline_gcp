
{{ config(materialized='table') }}

with source_data as (
  SELECT
  CAST(OrderStatus AS INTEGER) AS dky_status,
  CASE
    WHEN OrderStatus='1' THEN "OPEN"
    WHEN OrderStatus='2' THEN 'WAITING PAYMENT'
    WHEN OrderStatus='3' THEN "PAID"
    WHEN OrderStatus='4' THEN "DELIVERED"
  ELSE
  "N/A"
END
  AS des_status
FROM
  `cloud-portfolio-dev.Business.Orders`
GROUP BY
  OrderStatus
ORDER BY
  OrderStatus
)
select * from source_data