import json, statistics as st, math
BARS=json.load(open('bars.json'))
SER={c:[[x[0]]+[float(v) for v in x[1:6]] for x in b] for c,b in BARS.items()}
START,END='2025-06-24','2026-07-31'
H=5
recs=[]
for c,b in SER.items():
    for i in range(61,len(b)-H):
        if not (START<=b[i][0]<=END): continue
        r5=b[i][2]/b[i-5][2]-1
        recs.append((c,i,b[i][0],r5))
mkt={}
for c,i,d,_ in recs: mkt.setdefault(d,[]).append(SER[c][i+H][2]/SER[c][i][2]-1)
mkt={d:st.mean(v) for d,v in mkt.items()}
def band(r5):
    if r5>=0.30: return '近5日 >=+30%'
    if r5>=0.15: return '近5日 +15~30%'
    if r5>=0: return '近5日 0~+15%'
    return '近5日 <0'
print("问：强势票上『挂限价等回调』的偏差会不会更大？")
print("做法：决策日收盘为起点，挂 -depth 限价等 5 个交易日；未成交=空仓记 0。")
print("收益一律减去当天全池 5 日平均（剔除行情漂移）。\n")
for depth in [0.03,0.05]:
    print(f"=== 限价 -{depth*100:.0f}%，等 5 天 ===")
    print(" 起点分组          n     成交率   立即买(相对) 阶梯(相对)  差额")
    for nm in ['近5日 <0','近5日 0~+15%','近5日 +15~30%','近5日 >=+30%']:
        g=[x for x in recs if band(x[3])==nm]
        imm=[];lad=[]
        for c,i,d,_ in g:
            b=SER[c]; m=mkt[d]; lvl=b[i][2]*(1-depth)
            hit=any(b[j][4]<=lvl for j in range(i+1,i+1+H))
            imm.append(b[i+H][2]/b[i][2]-1-m)
            lad.append((b[i+H][2]/lvl-1-m) if hit else -m)
        fr=sum(1 for c,i,d,_ in g if any(SER[c][j][4]<=SER[c][i][2]*(1-depth) for j in range(i+1,i+1+H)))/len(g)
        print(f" {nm:<16} {len(g):5d}  {fr*100:5.1f}%   {st.mean(imm)*100:+7.2f}%   {st.mean(lad)*100:+7.2f}%  {(st.mean(lad)-st.mean(imm))*100:+6.2f}pp")
    print()
print("=== 只看『前一日涨停』的起点（最接近连板场景）===")
def cap(code): return 0.20 if code[0]=='3' or code[:3]=='688' else 0.10
lu=[]
for c,i,d,_ in recs:
    b=SER[c]
    if b[i][2]/b[i-1][2]-1>=cap(c)-0.005 and abs(b[i][2]-b[i][3])<1e-6: lu.append((c,i,d))
print(f" 样本 n={len(lu)} 股票-日，独立交易日 {len(set(x[2] for x in lu))}")
for depth in [0.03,0.05,0.075]:
    hit=[];imm=[];lad=[]
    for c,i,d in lu:
        b=SER[c]; m=mkt[d]; lvl=b[i][2]*(1-depth)
        h=any(b[j][4]<=lvl for j in range(i+1,i+1+H)); hit.append(h)
        imm.append(b[i+H][2]/b[i][2]-1-m); lad.append((b[i+H][2]/lvl-1-m) if h else -m)
    print(f"  限价 -{depth*100:4.1f}%: 5 日内成交率 {sum(hit)/len(hit)*100:5.1f}%   立即买(相对) {st.mean(imm)*100:+6.2f}%  阶梯(相对) {st.mean(lad)*100:+6.2f}%  差额 {(st.mean(lad)-st.mean(imm))*100:+6.2f}pp")
print("\n 对照：全样本同口径 5 日内成交率")
for depth in [0.03,0.05,0.075]:
    fr=sum(1 for c,i,d,_ in recs if any(SER[c][j][4]<=SER[c][i][2]*(1-depth) for j in range(i+1,i+1+H)))/len(recs)
    print(f"  限价 -{depth*100:4.1f}%: {fr*100:5.1f}%")
