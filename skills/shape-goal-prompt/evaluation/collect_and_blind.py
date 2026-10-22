"""Copy raw replies and randomize condition labels independently for each grader."""
import argparse, hashlib, json, pathlib, random, shutil

p=argparse.ArgumentParser();p.add_argument('stage');p.add_argument('conditions',nargs='+');a=p.parse_args()
E=pathlib.Path(__file__).resolve().parent
cases=json.loads((E/a.stage/'cases-private.json').read_text())
by={}
for condition in a.conditions:
 dispatch=json.loads((E/'dispatch'/f'{a.stage}-{condition}.json').read_text())
 responses={}
 for m in dispatch['messages']:
  f=pathlib.Path(m['response_path']); data=json.loads(f.read_text())
  dest=E/a.stage/f'responses-{condition}-{m["turn"]}.json';shutil.copyfile(f,dest)
  expected={r['case_id'] for r in json.loads((E/a.stage/f'turn-{m["turn"]}.json').read_text())}
  assert {r['case_id'] for r in data['responses']}==expected
  for r in data['responses']:
   assert isinstance(r['reply'],str) and r['reply'].strip()
   responses[(r['case_id'],m['turn'])]=r['reply']
 by[condition]=responses
G=E/'grading';G.mkdir(exist_ok=True)
for judge in [1,2]:
 rng=random.Random(f'goal-prompt-{a.stage}-{judge}-20261021')
 records=[];key={}
 for c in cases:
  shuffled=a.conditions[:];rng.shuffle(shuffled)
  for n,condition in enumerate(shuffled):
   label=f'{c["id"]}-{chr(65+n)}'
   transcript=[]
   for t,user in enumerate(c['turns'],1):
    transcript.extend([{'role':'user','content':user},{'role':'assistant','content':by[condition][(c['id'],t)]}])
   records.append({'case_id':c['id'],'label':label,'transcript':transcript,'checks':c['checks']})
   key[label]=condition
 rng.shuffle(records)
 (G/f'{a.stage}-judge-{judge}-input.json').write_text(json.dumps(records,indent=2)+'\n')
 (G/f'{a.stage}-judge-{judge}-key.json').write_text(json.dumps(key,indent=2)+'\n')
stats={k:{'replies':len(v),'words':sum(len(x.split()) for x in v.values()),'per_reply':{f'{c}-{t}':len(x.split()) for (c,t),x in v.items()}} for k,v in by.items()}
(E/a.stage/'word-counts.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps({'stage':a.stage,'conditions':a.conditions,'cases':len(cases),'stats':stats},indent=2))
