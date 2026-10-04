import re,sys,json
def run(t):
 s=[x.strip() for x in re.split(r'(?<=[.!?])\s+',t) if x.strip()]; q=[x for x in s if x.endswith('?')]
 return {'sentences':len(s),'questions':len(q),'question_ratio':round(len(q)/max(1,len(s)),2),'questions_found':q}
if __name__=='__main__': print(json.dumps(run(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Text: ')),indent=2))