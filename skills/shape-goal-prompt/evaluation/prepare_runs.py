"""Create isolated task inputs and auditable dispatch instructions; no model calls."""
import argparse, hashlib, json, pathlib, shutil

p=argparse.ArgumentParser(); p.add_argument('stage'); p.add_argument('condition'); p.add_argument('--skill'); a=p.parse_args()
E=pathlib.Path(__file__).resolve().parent
R=pathlib.Path('/tmp')/('goal-prompt-'+a.stage+'-'+a.condition)
R.mkdir(parents=True,exist_ok=False)
S=pathlib.Path(a.skill).resolve() if a.skill else None
if S: shutil.copytree(S,R/'shape-goal-prompt')
turns=sorted((E/a.stage).glob('turn-*.json'))
# Reveal later user messages only when that turn is dispatched.
shutil.copyfile(turns[0],R/turns[0].name)
messages=[]
for i,f in enumerate(turns,1):
 intro=(f'Use $shape-goal-prompt at {R}/shape-goal-prompt to respond to the requests.' if S else 'Help the users turn their rough requests into structured goal-driven prompts for an agent, clarifying useful ambiguities and incorporating feedback.') if i==1 else 'Continue the separate conversations from your earlier replies, using the user follow-ups supplied here.'
 msg=f'''{intro}
Read {R}/{f.name}. Each case_id is an independent conversation; keep its context separate. Treat the text under user as that user's current message. Produce the actual user-facing reply for each case.
Save your complete replies as JSON {{"responses":[{{"case_id":"...","reply":"..."}}]}} in {R}/responses-{i}.json. Preserve the user's requested output form inside reply. The record file is an administrative output, not the user's underlying task.
Read only the assigned request files, your own previous responses, and the assigned skill directory if present; do not inspect other workspace material. Do not delegate to subagents. Do not execute the tasks described by the users. Do not browse unless the user request to you (as prompt author) specifically requires it. Return a short completion notice after saving.'''
 messages.append({'turn':i,'message':msg,'response_path':str(R/f'responses-{i}.json')})
record={'stage':a.stage,'condition':a.condition,'run_directory':str(R),'skill_original':str(S) if S else None,'skill_hashes':{str(f.relative_to(S)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(S.rglob('*')) if f.is_file()} if S else {},'messages':messages}
out=E/'dispatch';out.mkdir(exist_ok=True)
(out/f'{a.stage}-{a.condition}.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'run_directory':str(R),'turns':len(turns),'dispatch':str(out/f'{a.stage}-{a.condition}.json')}))
