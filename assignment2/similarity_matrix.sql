select cnt from
(select f1.docid, f2.docid, sum(f1.count * f2.count) as cnt
from frequency f1 join frequency f2
on f1.term = f2.term
where f1.docid = "10080_txt_crude" and f2.docid = "17035_txt_earn" and f1.docid < f2.docid
group by f1.docid, f2.docid);
