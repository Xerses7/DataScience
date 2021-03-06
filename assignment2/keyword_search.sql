select f1.docid, sum(f1.count * q.count) as cnt
from frequency f1 join (
    SELECT 'q' as docid, 'washington' as term, 1 as count 
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION 
    SELECT 'q' as docid, 'treasury' as term, 1 as count
) q
on f1.term = q.term
group by f1.docid, q.docid
order by cnt desc;
