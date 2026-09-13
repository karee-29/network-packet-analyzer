import csv,json,dataclasses
def write_csv(rs,path):
 with open(path,"w",newline="",encoding="utf8") as f:
  w=csv.DictWriter(f,fieldnames=[x.name for x in dataclasses.fields(rs[0])] if rs else ["source_ip"]);w.writeheader()
  for r in rs:w.writerow(r.to_dict())
def write_json(rs,path):
 with open(path,"w",encoding="utf8") as f:json.dump([r.to_dict() for r in rs],f,indent=2)
