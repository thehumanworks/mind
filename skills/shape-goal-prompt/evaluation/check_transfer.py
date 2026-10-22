"""Deterministic checks for the two small downstream handoff tasks."""
import csv, io, json, re

def evaluate(case,output):
 if case['case_id']=='T1':
  try: rows=list(csv.reader(io.StringIO(output)));parse=True
  except csv.Error:rows=[];parse=False
  expected=case['expected_rows']
  return {'csv_parses':parse,'header':bool(rows) and rows[0]==expected[0],
   'row_count':len(rows)==len(expected),'rows_and_order_exact':rows==expected}
 try:obj=json.loads(output);parsed=True
 except (ValueError,TypeError):obj={};parsed=False
 actions=obj.get('confirmed_actions',[]) if isinstance(obj,dict) else []
 questions=obj.get('open_questions',[]) if isinstance(obj,dict) else []
 actions=actions if isinstance(actions,list) else []
 review=[x for x in actions if isinstance(x,dict) and 'checklist' in str(x.get('action','')).lower() and 'review' in str(x.get('action','')).lower()]
 archive=[x for x in actions if isinstance(x,dict) and 'archive' in str(x.get('action','')).lower() and 'faq' in str(x.get('action','')).lower()]
 due=str(review[0].get('due','')).lower() if len(review)==1 else ''
 dates=due in {'20 november 2026','november 20, 2026','2026-11-20','20 nov 2026','nov 20, 2026'}
 qtext=json.dumps(questions).lower()
 return {'json_parses':parsed,'exact_top_level_keys':isinstance(obj,dict) and set(obj)=={'confirmed_actions','open_questions'},
  'two_adopted_actions':len(actions)==2 and len(review)==1 and len(archive)==1,
  'required_action_fields':len(actions)==2 and all(isinstance(x,dict) and set(x)>={'action','owner','due'} for x in actions),
  'corrected_review_due':dates,'review_owner':len(review)==1 and review[0].get('owner')=='Eli',
  'archive_unknowns':len(archive)==1 and archive[0].get('owner','MISSING') is None and archive[0].get('due','MISSING') is None,
  'open_questions_retained':isinstance(questions,list) and 'faq' in qtext and 'analytics' in qtext,
  'no_extra_action':len(actions)==2 and len(review)==1 and len(archive)==1}
