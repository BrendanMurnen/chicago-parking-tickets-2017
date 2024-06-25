with ticket_measures_by_ward as (
  select
    ward
    , count(*) as issued_tickets_count
    , sum(case when ticket_queue = 'Paid'then 1 end) as paid_tickets_count
    , sum(total_payments) as net_payments_usd

  from `bmurnen-maps.chicago_data.chicago_parking_tickets`
  where 
    issue_date between '2017-01-01' and '2017-12-31'
    and ward is not null
  group by 1
)

select
  ward
  , issued_tickets_count
  , paid_tickets_count
  , round(paid_tickets_count / issued_tickets_count, 4) as collected_tickets_pct
  , net_payments_usd
from ticket_measures_by_ward
order by net_payments_usd desc