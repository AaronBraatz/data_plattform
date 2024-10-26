-- models/example_model.sql

with source_data as (
    select *
    from {{ ref('source_table') }}
)

select *
from source_data
