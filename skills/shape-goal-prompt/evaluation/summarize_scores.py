"""Recalculate all reported rubric totals from raw blind grades."""
import argparse, json, pathlib

p=argparse.ArgumentParser();p.add_argument('stage');a=p.parse_args()
E=pathlib.Path(__file__).resolve().parent
dimensions=['fidelity','outcome','acceptance','clarification','feedback','handoff','proportionality','optimization']
summary={}
for judge in [1,2]:
 key=json.loads((E/'grading'/f'{a.stage}-judge-{judge}-key.json').read_text())
 raw=json.loads((E/'grading'/f'{a.stage}-judge-{judge}-scores.json').read_text())
 records=raw if isinstance(raw,list) else raw['records']
 assert len(records)==len(key)
 assert {r['label'] for r in records}==set(key)
 for r in records:
  assert set(r['scores'])==set(dimensions),(r['label'],r['scores'])
  assert all(type(v) is int and 0<=v<=2 for v in r['scores'].values())
  c=key[r['label']]
  s=summary.setdefault(c,{'total':0,'maximum':0,'critical_failures':[],'dimensions':dict.fromkeys(dimensions,0),'judges':{},'cases':{}})
  total=sum(r['scores'].values());s['total']+=total;s['maximum']+=16
  s['judges'][str(judge)]=s['judges'].get(str(judge),0)+total
  s['cases'].setdefault(r['case_id'],[]).append({'judge':judge,'total':total,'evidence':r.get('evidence',r.get('deductions',r.get('overall_notes','')))})
  for d,v in r['scores'].items():s['dimensions'][d]+=v
  for failure in r['critical_failures']:s['critical_failures'].append({'case_id':r['case_id'],'judge':judge,'failure':failure})
for c,s in summary.items():s['percentage']=round(s['total']/s['maximum']*100,2)
(E/f'{a.stage}-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
