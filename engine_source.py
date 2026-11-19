import os,json,random,urllib.request as U
VAL=[0,100,320,330,500,900,0]
PHA=[0,0]+VAL[2:6]+[0]
BMG,BEG=25,40
TB=[-50,-40,-30,-20,-10,-6,0,4,8,10,12,14,16,20,24,26,30,34,38,40,50]
def _dec(s):
  o=[]
  for i in range(0,32,4):
    k=s[i:i+4];o+=[TB[ord(c)-97] for c in k+k[::-1]]
  return o
PA=_dec("gggguuuujjnqhhjogggnhfeghjjdgggg")
PZ=_dec("gggguuuurrssnnopiikmgghiggghgggg")
NT=_dec("abccbdggcgjlchlncglnchjlbdghabcc")
BT=_dec("deeeegggeghjehhj""egjjejjjehggdeee")
RT=_dec("gggghjjjfgggfgggfgggfgggfggggggh")
QT=_dec("deefegggeghhfghh""gghhehhheghgdeef")
QT[39]=-6;QT[46]=QT[53]=0
KG=_dec("cbbacbbacbbacbbadccbedddnnggnqjg")
KZ=_dec("abcdcdegcenqceqtceqtcenqccggaccc")
TMG=[None,PA,NT,BT,RT,QT,KG]
TEG=[None,PZ,NT,BT,RT,QT,KZ]
PM=[[0]*128 for _ in range(15)]
PE=[[0]*128 for _ in range(15)]
for _pc in range(1,7):
  for _co in (0,1):
    _cd=_pc+8*_co;_sg=1 if _co==0 else -1
    for _r in range(8):
      for _f in range(8):
        _i=(7-_r)*8+_f if _co==0 else _r*8+_f
        _sq=_r*16+_f
        PM[_cd][_sq]=_sg*(VAL[_pc]+TMG[_pc][_i])
        PE[_cd][_sq]=_sg*(VAL[_pc]+TEG[_pc][_i])
_R=random.Random(987654321).getrandbits
ZK=[[_R(64) for _ in range(128)] for _ in range(15)]
ZC=[_R(64) for _ in range(16)]
ZE=[_R(64) for _ in range(128)]
ZS=_R(64)
B=[0]*128;S,C,E,H,Z,Vm,Ve,Ph=0,0,-1,0,0,0,0,6400
NP=[0,0];K=[4,116];US=[];HL=[];RC={}
BP=[0,0]
TK,TD,TF,TV,TTM=[[0]*262144 for _ in range(5)]
KL=[[0,0] for _ in range(128)]
HH=[0]*1920
ND=0;ST=False;RB=0;NB=84000;INF=300000
ND8=[33,31,18,14,-14,-18,-31,-33]
KD=[17,16,15,1,-1,-15,-16,-17]
BD=[17,15,-15,-17]
RD=[16,1,-1,-16]
MV={2:(ND8,0),6:(KD,0),3:(BD,1),4:(RD,1),5:(KD,1)}
SQ=[s for s in range(128) if not s&0x88]
def atk(s,by):
  b=B
  for d in ((-15,-17),(15,17))[by]:
    x=s+d
    if not x&0x88 and b[x]==1+8*by:return True
  for ds,pc in ((ND8,2),(KD,6)):
    for d in ds:
      x=s+d
      if not x&0x88 and b[x]==pc+8*by:return True
  for ds,ts in ((BD,(3,5)),(RD,(4,5))):
    for d in ds:
      x=s
      while True:
        x+=d
        if x&0x88:break
        q=b[x]
        if q:
          if q>>3==by and (q&7) in ts:return True
          break
  return False
def ev():
  p=min(Ph,6400);w=Vm*p+Ve*(6400-p)
  return int(w/6400) if S==0 else -int(w/6400)
def gen(cap):
  ms=[];ap=ms.append;en=S^1
  for s in SQ:
    p=B[s]
    if not p or p>>3!=S:continue
    t=p&7
    if t==1:
      d=16 if S==0 else -16
      r=s>>4;ls=r==(6 if S==0 else 1)
      t1=s+d
      if not B[t1]:
        if ls:
          for pr in (5,4,3,2):ap(s|t1<<7|pr<<14)
        elif not cap:
          ap(s|t1<<7)
          if r==(1 if S==0 else 6) and not B[s+2*d]:ap(s|(s+2*d)<<7)
      for dd in (d-1,d+1):
        t1=s+dd
        if t1&0x88:continue
        q=B[t1]
        if q and q>>3==en and (q&7)!=6:
          if ls:
            for pr in (5,4,3,2):ap(s|t1<<7|pr<<14)
          else:ap(s|t1<<7)
        elif t1==E:ap(s|t1<<7)
    else:
      ds,sl=MV[t]
      for d in ds:
        t1=s
        while True:
          t1+=d
          if t1&0x88:break
          q=B[t1]
          if not q:
            if not cap:ap(s|t1<<7)
          else:
            if q>>3==en and (q&7)!=6:ap(s|t1<<7)
            break
          if not sl:break
      if t==6 and not cap:
        for bit,rq,em,tr,tg in ((1,7,(5,6),(4,5,6),6),(2,0,(3,2,1),(4,3,2),2),(4,119,(117,118),(116,117,118),118),(8,112,(115,114,113),(116,115,114),114)):
          if C&bit and B[rq]==4+8*S and not any(B[x] for x in em) and not any(atk(x,en) for x in tr):ap(s|tg<<7)
  return ms
def _fin():
  HL.append(Z);RC[Z]=RC.get(Z,0)+1
def make(m):
  global S,C,E,H,Z,Vm,Ve,Ph
  us=(C,E,H,Z,Vm,Ve,Ph,NP[0],NP[1])
  if m==0:
    US.append((0,)+us)
    if E>=0:Z^=ZE[E];E=-1
    S^=1;Z^=ZS;H+=1
    _fin();return
  f=m&127;t=(m>>7)&127;pr=(m>>14)&7
  p=B[f];col=p>>3;ty=p&7;q=B[t];cq=t
  if ty==1 and t==E and not q:
    cq=t-16 if col==0 else t+16;q=B[cq]
  US.append((q,)+us)
  nq=pr+8*col if pr else p
  Vm-=PM[p][f];Ve-=PE[p][f];Z^=ZK[p][f]
  Vm+=PM[nq][t];Ve+=PE[nq][t];Z^=ZK[nq][t]
  if q:
    Vm-=PM[q][cq];Ve-=PE[q][cq];Z^=ZK[q][cq]
    Ph-=PHA[q&7]
    if 2<=(q&7)<=5:NP[q>>3]-=VAL[q&7]
    if (q&7)==3:
      ow=q>>3;BP[ow]-=1
      if BP[ow]==1:sg=1-2*ow;Vm-=sg*BMG;Ve-=sg*BEG
    B[cq]=0
  B[f]=0;B[t]=nq
  if pr:
    Ph+=PHA[pr];NP[col]+=VAL[pr]
    if pr==3:
      BP[col]+=1
      if BP[col]==2:sg=1-2*col;Vm+=sg*BMG;Ve+=sg*BEG
  if ty==6:
    K[col]=t
    if t-f==2:rf,rt=f+3,f+1
    elif f-t==2:rf,rt=f-4,f-1
    else:rf=-1
    if rf>=0:
      rp=B[rf];B[rf]=0;B[rt]=rp
      Vm-=PM[rp][rf];Ve-=PE[rp][rf];Z^=ZK[rp][rf]
      Vm+=PM[rp][rt];Ve+=PE[rp][rt];Z^=ZK[rp][rt]
  Z^=ZC[C]
  if ty==6:C&=~(3 if col==0 else 12)
  for sq,bit in ((0,2),(7,1),(112,8),(119,4)):
    if f==sq or t==sq:C&=~bit
  Z^=ZC[C]
  if E>=0:Z^=ZE[E]
  E=(f+t)//2 if ty==1 and abs(t-f)==32 else -1
  if E>=0:Z^=ZE[E]
  S^=1;Z^=ZS
  H=0 if ty==1 or q else H+1
  _fin()
def un(m):
  global S,C,E,H,Z,Vm,Ve,Ph
  q,C,E,H,Z,Vm,Ve,Ph,n0,n1=US.pop()
  NP[0]=n0;NP[1]=n1
  z=HL.pop();RC[z]-=1
  if not RC[z]:del RC[z]
  S^=1
  if m==0:return
  f=m&127;t=(m>>7)&127;pr=(m>>14)&7
  if pr==3:BP[S]-=1
  if q and (q&7)==3:BP[q>>3]+=1
  ty=1 if pr else B[t]&7
  B[f]=ty+8*S;B[t]=0
  if ty==6:
    K[S]=f
    if abs(t-f)==2:
      rf,rt=(f+3,f+1) if t>f else (f-4,f-1)
      B[rf]=B[rt];B[rt]=0
  if q:
    if ty==1 and t==E:B[t-16 if S==0 else t+16]=q
    else:B[t]=q
def sf(fen):
  global S,C,E,H,Z,Vm,Ve,Ph
  B[:]=[0]*128
  ps=fen.split()
  Vm=0;Ve=0;Ph=0;NP[0]=0;NP[1]=0;Z=0
  BP[0]=BP[1]=0
  sq=112
  for ch in ps[0]:
    if ch=="/":sq-=24
    elif ch.isdigit():sq+=int(ch)
    else:
      col=0 if ch.isupper() else 1
      ty="pnbrqk".index(ch.lower())+1
      p=ty+8*col
      B[sq]=p
      Vm+=PM[p][sq];Ve+=PE[p][sq];Ph+=PHA[ty]
      if 2<=ty<=5:NP[col]+=VAL[ty]
      if ty==3:BP[col]+=1
      if ty==6:K[col]=sq
      Z^=ZK[p][sq];sq+=1
  for col in (0,1):
    if BP[col]>1:sg=1-2*col;Vm+=sg*BMG;Ve+=sg*BEG
  S=1 if len(ps)>1 and ps[1]=="b" else 0
  if S:Z^=ZS
  C=0
  if len(ps)>2:C=sum(1<<i for i,ch in enumerate("KQkq") if ch in ps[2])
  Z^=ZC[C]
  E=-1
  if len(ps)>3 and ps[3]!="-":
    E=(int(ps[3][1])-1)*16+ord(ps[3][0])-97
    Z^=ZE[E]
  H=int(ps[4]) if len(ps)>4 else 0
  US.clear();HL[:]=[Z];RC.clear();RC[Z]=1
def uci(m):
  f=m&127;t=(m>>7)&127
  s=chr(97+(f&7))+chr(49+(f>>4))+chr(97+(t&7))+chr(49+(t>>4))
  pr=(m>>14)&7
  return s+"nbrq"[pr-2] if pr else s
def ords(ms,ttm,pl):
  def key(m):
    if m==ttm:return 1<<28
    f=m&127;t=(m>>7)&127;p=B[f];q=B[t];pr=(m>>14)&7
    if q or (p&7)==1 and t==E or pr:
      v=VAL[q&7] if q else VAL[pr] if pr else 100
      return (1<<25)+(v<<4)-(VAL[p&7]>>4)+(VAL[pr]<<4 if q and pr else 0)
    if KL[pl][0]==m:return 1<<24
    if KL[pl][1]==m:return 1<<23
    return HH[p*128+t]
  ms.sort(key=key,reverse=True)
  return ms
def qs(a,b,pl):
  global ND,ST
  if ST:return 0
  ND+=1
  if ND>=NB:ST=True;return ev()
  inchk=atk(K[S],S^1)
  if not inchk:
    stand=ev()
    if stand>=b:return stand
    if stand>a:a=stand
  ms=gen(not inchk)
  legal=0
  for m in ords(ms,0,pl):
    if not inchk and not (m>>14)&7:
      q=B[(m>>7)&127]
      v=VAL[q&7] if q else 100
      if stand+v+180<=a:continue
    make(m)
    if atk(K[S^1],S):un(m);continue
    legal+=1
    sc=-qs(-b,-a,pl+1)
    un(m)
    if ST:return 0
    if sc>=b:return sc
    if sc>a:a=sc
  if inchk and not legal:return -100000+pl
  return a
def search(d,a,b,pl):
  global ND,ST,RB
  if ST:return 0
  if pl>0 and (RC[Z]>1 or H>=100):return 0
  if d<=0:return qs(a,b,pl)
  ND+=1
  if ND>=NB:ST=True;return 0
  i=Z&262143;ttm=0
  if TK[i]==Z:
    ttm=TTM[i]
    if pl>0 and TD[i]>=d:
      v=TV[i]
      if v>99000:v-=pl
      elif v<-99000:v+=pl
      fl=TF[i]
      if fl==0 or (v>=b if fl==1 else v<=a):return v
  inchk=atk(K[S],S^1)
  if inchk:d+=1
  if (pl>0 and d>=3 and not inchk and b<99000 and NP[S]>800
      and ev()>=b):
    make(0)
    sc=-search(d-1-(3 if d>=5 else 2),-b,-b+1,pl+1)
    un(0)
    if ST:return 0
    if sc>=b:return sc
  fut=d<=2 and not inchk and pl>0 and ev()+110+90*d<=a
  best=-INF;bmove=0;legal=0;a0=a
  for m in ords(gen(False),ttm,pl):
    f=m&127;t=(m>>7)&127;p=B[f]
    quiet=(not B[t] and not ((p&7)==1 and t==E) and not (m>>14)&7)
    if fut and quiet and legal>0:continue
    make(m)
    if atk(K[S^1],S):un(m);continue
    legal+=1
    if legal==1:
      sc=-search(d-1,-b,-a,pl+1)
    else:
      red=0
      if (d>=3 and quiet and legal>4 and not inchk and m!=KL[pl][0]
          and m!=KL[pl][1]):
        red=1+(legal>11)
      if red:
        sc=-search(d-1-red,-a-1,-a,pl+1)
        if sc>a:sc=-search(d-1,-a-1,-a,pl+1)
      else:sc=-search(d-1,-a-1,-a,pl+1)
      if a<sc<b:sc=-search(d-1,-b,-a,pl+1)
    un(m)
    if ST:return 0
    if sc>best:
      best=sc;bmove=m
      if pl==0:RB=m
      if sc>a:
        a=sc
        if a>=b:
          if quiet:
            if KL[pl][0]!=m:KL[pl][1]=KL[pl][0];KL[pl][0]=m
            hi=p*128+t
            HH[hi]=min(HH[hi]+d*d,1<<20)
          break
  if not legal:return -100000+pl if inchk else 0
  fl=1 if best>=b else 2 if best<=a0 else 0
  v=best
  if v>99000:v+=pl
  elif v<-99000:v-=pl
  TK[i]=Z;TD[i]=d;TF[i]=fl;TV[i]=v;TTM[i]=bmove
  return best
def bm():
  global ND,ST,RB
  ND=0;ST=False
  RB=gen(False)[0]
  prev=0;depth=1
  while True:
    saved=RB
    if depth<=2:sc=search(depth,-INF,INF,0)
    else:
      sc=search(depth,prev-60,prev+60,0)
      if not ST and (sc<=prev-60 or sc>=prev+60):
        sc=search(depth,-INF,INF,0)
    if ST:RB=saved;break
    prev=sc
    if sc>99000:break
    depth+=1
  return RB
#DRIVER
URL=os.environ["MAKEFUN_ENV_URL"]
def post(path,body):
  try:
    with U.urlopen(U.Request(URL+path,data=json.dumps(body).encode(),headers={"content-type":"application/json"})) as res:return json.load(res)
  except:return None
while True:
  g=post("/game",{})
  if not g or g.get("status")=="done":break
  while g.get("status")=="your_move":
    sf(g["start_fen"])
    for u in g["moves"]:
      make(next(m for m in gen(False) if uci(m)==u))
    g=post("/move",{"game":g["game"],"move":uci(bm())}) or post("/move",{"game":g["game"],"move":g["legal_moves"][0]})
    if not g:break
