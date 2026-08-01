import json, urllib.request, os, time
CODES = """300308 300502 300394 603986 301308 688525 688256 688041 688521 002371 688012 688072
688126 688019 300054 688981 688347 688249 600584 002156 002185 300661 300782 603501 688008
002463 600183 002916 601138 000977 603019 301526 603256 002080 605376 300285 002837 002851""".split()
def mk(c):
    return ('sh' if c[0]=='6' else 'sz')+c
out={}
for c in CODES:
    s=mk(c)
    u=f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={s},day,,,800,qfq"
    for attempt in range(3):
        try:
            d=json.load(urllib.request.urlopen(u,timeout=20))
            bars=d['data'][s].get('qfqday') or d['data'][s].get('day')
            out[c]=bars; print(c,len(bars),bars[0][0],bars[-1][0]); break
        except Exception as e:
            print("retry",c,e); time.sleep(2)
json.dump(out,open(os.path.join(os.path.dirname(__file__),'bars.json'),'w'))
print("stocks",len(out))
