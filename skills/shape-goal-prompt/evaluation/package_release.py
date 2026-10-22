"""Build the skill ZIP and an auditable evaluation bundle after validation."""
import hashlib,json,pathlib,shutil,zipfile

E=pathlib.Path(__file__).resolve().parent;P=E.parent
out=P.parent/'deliverables'/'shape-goal-prompt-package'
assert not out.exists(),f'Choose a fresh output path: {out}'
out.mkdir(parents=True);dest=out/'evaluation';dest.mkdir()
for f in E.rglob('*'):
 if f.is_file() and '__pycache__' not in f.parts and f.name!='SHA256SUMS.json':
  target=dest/f.relative_to(E);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,target)
shutil.copytree(P/'variants',dest/'variants')
audits=dest/'audits';audits.mkdir()
for f in (P/'research').glob('*audit.md'):shutil.copyfile(f,audits/f.name)
shutil.copyfile(P/'research'/'SYNTHESIS.md',out/'research-summary.md')
shutil.copyfile(E/'USAGE.md',out/'README.md')
skill=P/'package'/'shape-goal-prompt'
hashes={str(f.relative_to(skill)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(skill.rglob('*')) if f.is_file()}
(dest/'delivered-skill-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
with zipfile.ZipFile(out/'shape-goal-prompt.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(skill.rglob('*')):
  if f.is_file():z.write(f,pathlib.Path('shape-goal-prompt')/f.relative_to(skill))
manifest={str(f.relative_to(out)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.rglob('*')) if f.is_file() and f.name!='SHA256SUMS.json'}
(dest/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
archive=out.parent/'shape-goal-prompt-bundle.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(out.rglob('*')):
  if f.is_file():z.write(f,f.relative_to(out))
print(json.dumps({'directory':str(out),'archive':str(archive),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':len(manifest)+1},indent=2))
