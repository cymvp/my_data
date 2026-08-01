import core, statistics as st
def gapb(g):
    return '高开>=5%' if g>=0.05 else ('高开3~5%' if g>=0.03 else ('高开0~3%' if g>0 else ('低开0~3%' if g>-0.03 else '低开>=3%')))
print("=== 日历对半（文档做法）核对 下跌×高开≥5% ===")
r=core.build(); ds=sorted(set(x['date'] for x in r)); mid=ds[len(ds)//2]
v=[x for x in r if x['trend']=='下跌' and gapb(x['gap'])=='高开>=5%']
a=[x for x in v if x['date']<mid]; b=[x for x in v if x['date']>=mid]
print("  前半 n=%d 收高率%s  后半 n=%d 收高率%.0f%%  (分界 %s)"%(len(a),('%.0f%%'%(core.hi(a)*100)) if a else '-',len(b),core.hi(b)*100,mid))

print("\n=== 趋势定义敏感性：窗口/阈值变化后 下跌×高开≥5% 与 震荡×低开≥3% ===")
print(" 窗口 阈值        下跌×高开>=5%: n 收高率 加权分 | 震荡×低开>=3%: n 收高率 加权分")
for win in [40,60,90]:
    for dn,up in [(-0.10,-0.03),(-0.15,-0.05),(-0.20,-0.08)]:
        rr=core.build(trend_win=win,dn=dn,up=up)
        v1=[x for x in rr if x['trend']=='下跌' and gapb(x['gap'])=='高开>=5%']
        v2=[x for x in rr if x['trend']=='震荡' and gapb(x['gap'])=='低开>=3%']
        f=lambda v: "n=%4d %5.1f%% %+5.2f"%(len(v),core.hi(v)*100,core.wscore(v)) if v else "空"
        print(f" {win:>3} {dn:.2f}/{up:.2f}   {f(v1)}  | {f(v2)}")

print("\n=== 加权分档位边界敏感性（下跌×高开≥5%）===")
r=core.build(); v1=[x for x in r if x['trend']=='下跌' and gapb(x['gap'])=='高开>=5%']
def ws(v,b1,b2,caps):
    def s(x):
        if x> b2: return caps[2]
        if x> b1: return caps[1]
        if x> 0: return caps[0]
        if x>-b1: return -caps[0]
        if x>-b2: return -caps[1]
        return -caps[2]
    return sum(s(y['oc']) for y in v)/len(v)
for b1,b2 in [(0.01,0.03),(0.02,0.05),(0.03,0.07)]:
    for caps in [(1,3.5,6.5),(1,2,3),(1,3.5,12)]:
        print("  边界±%.0f%%/±%.0f%% 计分%s → 加权分 %+.2f"%(b1*100,b2*100,caps,ws(v1,b1,b2,caps)))
print("  用中位数(开→收) %.2f%%  用均值 %.2f%%"%(st.median(y['oc'] for y in v1)*100, st.mean(y['oc'] for y in v1)*100))
print("\n=== 收高率与加权分的共线性（15格）===")
cells={}
for x in r: cells.setdefault((x['trend'],gapb(x['gap'])),[]).append(x)
xs=[core.hi(v) for v in cells.values()]; ys=[core.wscore(v) for v in cells.values()]
mx,my=st.mean(xs),st.mean(ys)
cov=sum((a-mx)*(b-my) for a,b in zip(xs,ys)); sx=sum((a-mx)**2 for a in xs)**.5; sy=sum((b-my)**2 for b in ys)**.5
print("  Pearson r = %.4f"%(cov/(sx*sy)))
