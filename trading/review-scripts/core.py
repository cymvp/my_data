import json, math, statistics as st
from collections import defaultdict
BARS=json.load(open('bars.json'))
SECT={'300308':'光模块','300502':'光模块','300394':'光模块','603986':'存储','301308':'存储','688525':'存储',
'688256':'算力芯片','688041':'算力芯片','688521':'算力芯片','002371':'半导设备','688012':'半导设备','688072':'半导设备',
'688126':'半导材料','688019':'半导材料','300054':'半导材料','688981':'晶圆','688347':'晶圆','688249':'晶圆',
'600584':'封测','002156':'封测','002185':'封测','300661':'模拟功率','300782':'芯片设计','603501':'芯片设计','688008':'芯片设计',
'002463':'PCB','600183':'PCB','002916':'PCB','601138':'服务器','000977':'服务器','603019':'服务器',
'301526':'电子布','603256':'电子布','002080':'电子布','605376':'MLCC','300285':'MLCC','002837':'温控电源','002851':'温控电源'}
START='2025-06-24'; END='2026-07-31'
def build(trend_win=60, dn=-0.15, up=-0.05, start=START, end=END):
    rows=[]
    for code,bars in BARS.items():
        b=[[x[0]]+[float(v) for v in x[1:6]] for x in bars]  # date,open,close,high,low,vol
        for i in range(len(b)):
            d,o,c,h,l,v=b[i]
            if d<start or d>end: continue
            if i<max(trend_win,20) or i+1>=len(b)+0: pass
            if i<max(trend_win,21): continue
            prev_close=b[i-1][2]
            peak=max(x[2] for x in b[i-trend_win:i])
            dd=(prev_close-peak)/peak
            trend='下跌' if dd<=dn else ('震荡' if dd<=up else '上涨')
            vol20=sum(x[5] for x in b[i-20:i])/20
            nxt=b[i+1] if i+1<len(b) else None
            rows.append(dict(code=code,sect=SECT[code],date=d,o=o,c=c,h=h,l=l,v=v,pc=prev_close,
                gap=(o-prev_close)/prev_close, chg=(c-prev_close)/prev_close, oc=(c-o)/o,
                brk=l<o, lowpct=(l-o)/o, highpct=(h-o)/o, volx=v/vol20 if vol20 else None, trend=trend, dd=dd,
                nd_chg=(nxt[2]-c)/c if nxt else None, nd_gap=(nxt[1]-c)/c if nxt else None,
                nd_oc=(nxt[2]-nxt[1])/nxt[1] if nxt else None, nd_brk=(nxt[4]<nxt[1]) if nxt else None))
    return rows
def score(x):
    if x>0.05: return 6.5
    if x>0.02: return 3.5
    if x>0: return 1.0
    if x>-0.02: return -1.0
    if x>-0.05: return -3.5
    return -6.5
def wscore(rs,key='oc'): return sum(score(r[key]) for r in rs)/len(rs) if rs else float('nan')
def hi(rs,key='oc'): return sum(1 for r in rs if r[key]>0)/len(rs) if rs else float('nan')
def ztest(k,n,p=0.5):
    if n==0: return float('nan'),float('nan')
    ph=k/n; z=(ph-p)/math.sqrt(p*(1-p)/n)
    return z, math.erfc(abs(z)/math.sqrt(2))
def z2(k1,n1,k2,n2):
    p=(k1+k2)/(n1+n2); 
    if p in (0,1): return 0.0,1.0
    se=math.sqrt(p*(1-p)*(1/n1+1/n2)); z=(k1/n1-k2/n2)/se
    return z, math.erfc(abs(z)/math.sqrt(2))
