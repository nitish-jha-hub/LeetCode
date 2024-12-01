select name from salesperson 
where sales_id not in (select orders.sales_id from orders where orders.com_id in (select company.com_id from company where company.name='RED'))