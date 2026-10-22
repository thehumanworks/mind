"""Prepare executor inputs from unedited authored prompts; no model calls."""
import argparse, hashlib, json, pathlib

p=argparse.ArgumentParser();p.add_argument('condition');a=p.parse_args()
E=pathlib.Path(__file__).resolve().parent
cases={c['case_id']:c for c in json.loads((E/'transfer-cases.json').read_text())}
source=E/'transfer'/f'responses-{a.condition}-1.json'
replies=json.loads(source.read_text())['responses']
assert {r['case_id'] for r in replies}==set(cases)
dispatch=[]
for reply in replies:
 c=cases[reply['case_id']]
 run=pathlib.Path('/tmp')/f'goal-transfer-execution-{a.condition}-{c["case_id"]}'
 run.mkdir(exist_ok=False)
 (run/'prompt.md').write_text(reply['reply'])
 for name,body in c['files'].items():(run/name).write_text(body)
 ext='csv' if c['case_id']=='T1' else 'json'
 output=run/f'result.{ext}'
 message=f'''Execute the assignment in {run}/prompt.md using only the input files in {run}. The assignment is authorized for this local task. You have been given all available task context; do not inspect other workspace material or browse, and do not delegate to subagents.
Write the complete requested output, without commentary or Markdown fences, to {output}. This output file is an administrative destination for the requested artifact. Do not modify the source inputs. Return a short completion notice after saving.'''
 dispatch.append({'condition':a.condition,'case_id':c['case_id'],'run_directory':str(run),'message':message,'output_file':str(output),'input_hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in run.iterdir() if f.is_file()}})
(E/'dispatch'/f'transfer-execution-{a.condition}.json').write_text(json.dumps(dispatch,indent=2)+'\n')
print(json.dumps(dispatch,indent=2))
