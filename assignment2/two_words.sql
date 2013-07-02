select count(*)
from (
    select distinct f1.docid
    from frequency f1 join frequency f2
    on f1.docid = f2.docid
    where f1.term = "transactions" and f2.term = "world"
);
 
