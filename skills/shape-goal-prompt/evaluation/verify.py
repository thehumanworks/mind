"""Verify an extracted evaluation bundle using only Python's standard library."""
import hashlib, io, json, pathlib, re, sys, zipfile

E=pathlib.Path(__file__).resolve().parent
dimensions={'fidelity','outcome','acceptance','clarification','feedback','handoff','proportionality','optimization'}

def digest(data):return hashlib.sha256(data).hexdigest()
def readj(path):return json.loads(path.read_text())

def main():
 manifest=readj(E/'SHA256SUMS.json')
 for rel,expected in manifest.items():
  p=E.parent/rel
  assert p.is_file(),f'Missing {rel}'
  assert digest(p.read_bytes())==expected,f'Hash mismatch: {rel}'
 for rel,expected in readj(E/'protocol-freeze.json').items():
  assert digest((E/rel).read_bytes())==expected,f'Changed protocol input: {rel}'
 for rel,expected in readj(E/'variant-freeze.json').items():
  assert digest((E/rel).read_bytes())==expected,f'Changed candidate: {rel}'
 for rel,expected in readj(E/'revision-freeze.json').items():
  assert digest((E/rel).read_bytes())==expected,f'Changed revision: {rel}'
 for rel,expected in readj(E/'regression-freeze.json').items():
  assert digest((E/rel).read_bytes())==expected,f'Changed regression input: {rel}'
 for f in (E/'dispatch').glob('*.json'):
  dispatch=readj(f)
  if isinstance(dispatch,dict) and dispatch.get('skill_original'):
   relative=dispatch['skill_original'].split('/variants/',1)[1]
   root=E/'variants'/relative
   hashes={str(p.relative_to(root)):digest(p.read_bytes()) for p in root.rglob('*') if p.is_file()}
   assert hashes==dispatch['skill_hashes'],f'Dispatched candidate mismatch: {f.name}'
 skillzip=E.parent/'shape-goal-prompt.zip'
 with zipfile.ZipFile(skillzip) as z:
  assert z.testzip() is None
  names=set(z.namelist());prefix='shape-goal-prompt/'
  assert all(n.startswith(prefix) and '..' not in pathlib.PurePosixPath(n).parts for n in names)
  md=z.read(prefix+'SKILL.md').decode()
  assert md.startswith('---\nname: shape-goal-prompt\ndescription:')
  assert '\n---\n' in md and len(md.splitlines())<500
  assert 'TODO' not in md and 'TODO' not in z.read(prefix+'agents/openai.yaml').decode()
  for rel,expected in readj(E/'delivered-skill-hashes.json').items():
   assert digest(z.read(prefix+rel))==expected,f'Delivered skill mismatch: {rel}'
  frozen=E/'variants'/'revised'/'shape-goal-prompt'
  assert names=={prefix+str(f.relative_to(frozen)) for f in frozen.rglob('*') if f.is_file()},'Unexpected or missing runtime file'
  for f in frozen.rglob('*'):
   if f.is_file():assert f.read_bytes()==z.read(prefix+str(f.relative_to(frozen)))
  for name in names:
   if name.endswith('.md'):
    s=z.read(name).decode()
    for target in re.findall(r'\]\(([^)]+)\)',s):
     if not re.match(r'https?://|#',target):
      p=str(pathlib.PurePosixPath(name).parent/target.split('#')[0]);assert p in names,(name,target)
 print('PASS: package, hashes, frozen inputs, runtime identity, metadata and local links')
 for stage in ('development','holdout','regression'):
  summary=readj(E/f'{stage}-summary.json');totals={k:0 for k in summary}
  for judge in (1,2):
   inputs=readj(E/'grading'/f'{stage}-judge-{judge}-input.json')
   key=readj(E/'grading'/f'{stage}-judge-{judge}-key.json')
   raw=readj(E/'grading'/f'{stage}-judge-{judge}-scores.json');records=raw if isinstance(raw,list) else raw['records']
   assert {r['label'] for r in inputs}==set(key)=={r['label'] for r in records}
   assert len(records)==len(key)
   for r in records:
    assert set(r['scores'])==dimensions
    assert all(type(v)is int and 0<=v<=2 for v in r['scores'].values())
    totals[key[r['label']]]+=sum(r['scores'].values())
   cases={c['id']:c for c in readj(E/stage/'cases-private.json')}
   for record in inputs:
    c=cases[record['case_id']];condition=key[record['label']]
    assert len(record['transcript'])==2*len(c['turns'])
    for t,user in enumerate(c['turns'],1):
     reply=next(r['reply'] for r in readj(E/stage/f'responses-{condition}-{t}.json')['responses'] if r['case_id']==c['id'])
     assert record['transcript'][2*t-2]=={'role':'user','content':user}
     assert record['transcript'][2*t-1]=={'role':'assistant','content':reply}
  assert totals=={k:v['total'] for k,v in summary.items()}
  print(f'PASS: {stage} anonymization and rubric totals {totals}')
 for r in readj(E/'format-checks.json')['checks']:
  stage='development' if r['case_id']=='D2' else 'holdout'
  reply=next(x['reply'] for x in readj(E/stage/f'responses-{r["condition"]}-1.json')['responses'] if x['case_id']==r['case_id'])
  if r['case_id']=='D2':assert r['word_count']==len(reply.split()) and r['passed']==(len(reply.split())<=120)
  else:assert r['reply']==reply and r['terminal_punctuation_count']==len(re.findall(r'[.!?](?=\s|$)',reply))==2 and r['passed']
 print('PASS: explicit user word and sentence limits on the saved outputs')
 from check_transfer import evaluate
 transfer=readj(E/'transfer-results.json')
 cases={c['case_id']:c for c in readj(E/'transfer-cases.json')}
 for r in transfer['results']:
  assert r['checked']
  actual=evaluate(cases[r['case_id']],(E/r['output_file']).read_text())
  assert actual==r['checks'],f'Transfer check mismatch: {r}'
  directory=(E/r['output_file']).parent
  source=next(x['reply'] for x in readj(E/'transfer'/f'responses-{r["condition"]}-1.json')['responses'] if x['case_id']==r['case_id'])
  assert (directory/'prompt.md').read_text()==source
  for name,body in cases[r['case_id']]['files'].items():assert (directory/name).read_text()==body
 print('PASS: downstream transfer checks independently recalculated; see REPORT.md for limits')

if __name__=='__main__':
 try:main()
 except (AssertionError,KeyError,FileNotFoundError,ValueError) as e:
  print(f'FAIL: {e}',file=sys.stderr);sys.exit(1)
