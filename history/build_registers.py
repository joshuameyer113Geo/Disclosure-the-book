import re,csv,datetime,urllib.parse
H="/workspace/disclosure/history/"
today="2026-10-28"
files={"TIMELINE.md":"T","MODERN_CASES_FACTS.md":"MC","ANCIENT_LORE.md":"A"}
claims=[]  # (id, title, tag, urls, file)
for f,p in files.items():
    t=open(H+f).read()
    # block split by heading or bullet-with-ID
    pat=re.compile(r'(?:^#{2,3} (?:\d+\. )?\[('+p+r'-\d{3})\] (.*)$)|(?:^- \[('+p+r'-\d{3})\] (.*)$)|(?:\[(MC-019)\] (.*)$)',re.M)
    ms=list(pat.finditer(t))
    for k,m in enumerate(ms):
        cid=m.group(1) or m.group(3) or m.group(5)
        title=(m.group(2) or m.group(4) or m.group(6)).replace("**","").strip()
        end=ms[k+1].start() if k+1<len(ms) else len(t)
        blk=t[m.start():end]
        if m.group(1) is None:  # bullet: only its own line
            blk=blk.split("\n")[0]
        tg=re.search(r'\*\*Tag:\*\* (.+)',blk); tag=tg.group(1) if tg else ""
        urls=re.findall(r'https?://[^\s)>\]]+',blk); urls=[u.rstrip('.,;') for u in urls]
        claims.append([cid,re.sub(r'\s+',' ',title)[:160],tag,list(dict.fromkeys(urls)),f])
def ctype(u):
    h=urllib.parse.urlparse(u).netloc.lower()
    if re.search(r'\.gov|\.mil|nationalarchives|riksarkivet|sian\.an\.gov|cnes\.fr|geipan|congress\.gov|govinfo',h): return "government document"
    if re.search(r'doi\.org|science\.org|nature\.com|pmc\.ncbi|jstor|digitalcommons|degruyter|wiley|iopscience|mdpi|arxiv|eos|journal',h): return "journal"
    if re.search(r'archive\.org|archives\.|britishmuseum|library|\.edu|perseus|oracc|ebl\.lmu|wikisource|ufoscans',h): return "archive"
    if re.search(r'nytimes|bbc|reuters|apnews|washingtonpost|cnn|nbc|cbs|abc|politico|guardian|spiegel|yomiuri|nikkei|time\.com|npr|history\.com|nationalgeographic|scientificamerican|eastoregonian|thedebrief|newsweek|latimes|axios|thehill|smithsonianmag|dvidshub',h): return "press"
    if re.search(r'books\.google|eisenbrauns|amazon',h): return "book"
    if re.search(r'nicap|theblackvault|wikipedia|cufos',h): return "database"
    return "web"
S={};order=[]
for c in claims:
    ids=[]
    for u in c[3]:
        if u not in S: S[u]={"id":f"S-{len(S)+1:04d}","claims":[]}; order.append(u)
        S[u]["claims"].append(c[0]); ids.append(S[u]["id"])
    c.append(ids)
with open(H+"SOURCES.csv","w",newline="") as fh:
    w=csv.writer(fh);w.writerow(["source_id","title","author_publisher","type","url","date_published","date_consulted","verification_status","claim_ids"])
    for u in order:
        h=urllib.parse.urlparse(u).netloc.replace("www.","")
        w.writerow([S[u]["id"],urllib.parse.unquote(urllib.parse.urlparse(u).path.rstrip('/').split('/')[-1] or h)[:90],h,ctype(u),u,"",today,"cited; live-check pending (see URL-check notes)",";".join(dict.fromkeys(S[u]["claims"]))])
md=["# SOURCES (bibliography / source log)","",f"Generated {today} from TIMELINE.md, MODERN_CASES_FACTS.md, ANCIENT_LORE.md. S- IDs are permanent and append-only. ARYAN_OCCULT.md and MYTH_CROSSREF.md were not available (lost in the 2026-10-28 wipe), so their AO-/MX- sources are NOT included yet.",""]
for ty in ["government document","archive","journal","press","book","database","web"]:
    us=[u for u in order if ctype(u)==ty]
    if not us: continue
    md+=[f"## {ty.title()} ({len(us)})",""]+[f"- **{S[u]['id']}** {u} — supports {', '.join(dict.fromkeys(S[u]['claims']))}" for u in us]+[""]
md+=["## Reverse index: claim → sources",""]+[f"- {c[0]}: {', '.join(c[5]) or '(no URL in block; see parent entry)'}" for c in claims]
open(H+"SOURCES.md","w").write("\n".join(md)+"\n")
# chapters
W={"T-017":"2","T-038":"5","T-001":"7","T-002":"8","T-003":"8","T-041":"9","T-043":"9","T-044":"9;31","T-052":"9","T-053":"9","MC-005":"16;28","T-012":"16;28"}
for i in range(48,52): W[f"T-0{i}"]="5"
for i in range(26,30): W[f"MC-0{i}"]="16;28"
for i in range(54,58): W[f"T-0{i}"]="42"
W["T-058"]="44";W["T-059"]="44"
mine={"T-004":"10","T-005":"10","T-006":"11","T-007":"12;27","T-008":"13;30","T-009":"33","T-010":"15","T-011":"34","T-013":"17","T-014":"29","T-015":"35","T-016":"19","T-018":"20","T-019":"22;30","T-020":"23","T-021":"24","T-022":"25","T-023":"36","T-024":"26","T-025":"36;27","T-026":"37","T-027":"37","T-028":"38;43","T-029":"39","T-030":"38","T-031":"40","T-032":"40","T-033":"40","T-034":"41","T-035":"41;43",
"T-036":"3","T-037":"3","T-039":"6","T-040":"32","T-042":"29","T-045":"3","T-046":"32","T-047":"32","T-060":"1","T-061":"32","T-062":"32","T-063":"3","T-064":"6","T-065":"8","T-066":"8","T-067":"8","T-068":"8","T-069":"11","T-070":"27;12","T-071":"32","T-072":"32;45","T-073":"32","T-074":"32","T-075":"45","T-076":"45",
"MC-001":"12","MC-002":"13","MC-003":"14","MC-004":"15","MC-006":"17","MC-007":"18","MC-008":"19","MC-009":"20","MC-010":"21","MC-011":"24","MC-012":"22","MC-013":"25","MC-014":"26","MC-015":"39","MC-016":"36","MC-017":"18","MC-018":"21","MC-019":"36","MC-020":"36","MC-021":"23","MC-022":"32","MC-023":"28","MC-024":"32","MC-025":"38",
"A-001":"3","A-002":"3","A-003":"4;5","A-004":"6","A-005":"3","A-006":"2;29","A-007":"29","A-008":"32","A-009":"32","A-010":"32","A-011":"9","A-012":"9","A-013":"9;31"}
W={**mine,**W}
def conf(tag,title):
    s=(tag+" "+title).lower()
    if "disputed" in s or "contested" in s: return "contested"
    if "lore" in s and "fact" not in s: return "lore"
    if "in between" in s or "open question" in s: return "in between"
    if "fact" in s: return "fact"
    return "in between" if tag else ""
with open(H+"CLAIMS_REGISTER.csv","w",newline="") as fh:
    w=csv.writer(fh);w.writerow(["claim_id","claim","source_ids","confidence","chapter","file"])
    for c in claims: w.writerow([c[0],c[1],";".join(c[5]),conf(c[2],c[1]),W.get(c[0],""),c[4]])
md=["# CLAIMS REGISTER","",f"Generated {today}. Chapter mapping: Eden Writer's mapping plus the Historian's assignments. AO-/MX- claims (ch9) are missing until ARYAN_OCCULT.md and MYTH_CROSSREF.md are regenerated. Confidence comes from each entry's Tag (MC/A bullets without a tag inherit their case; blank means untagged).","","| Claim | Claim (short) | Sources | Confidence | Chapter | File |","|---|---|---|---|---|---|"]
for c in claims: md.append(f"| {c[0]} | {c[1][:90].replace('|','/')} | {', '.join(c[5])} | {conf(c[2],c[1])} | {W.get(c[0],'')} | {c[4]} |")
open(H+"CLAIMS_REGISTER.md","w").write("\n".join(md)+"\n")
used=set(x for v in W.values() for x in v.split(";"))
print(len(claims),"claims;",len(S),"sources; unmapped:",[c[0] for c in claims if c[0] not in W],"; empty chapters:",sorted(set(map(str,range(1,46)))-used,key=int))
from collections import Counter;print(Counter(ctype(u) for u in order)); print("no-source claims:",[c[0] for c in claims if not c[5]])
