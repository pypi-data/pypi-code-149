# 2023.2.3 , cp from c4matcher.py | VBN -> past participle -> e | t -> to, b -> be , g -> VBG, c-> Clause , d-> ADV
import json, traceback,sys, time,  fileinput, os, en,sqlite3, spacy
from pathlib import Path
from spacy.matcher import Matcher

matcher = Matcher(spacy.nlp.vocab) # remind _NP of NP 
matcher.add("vpn", [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":"ADP"} , {"TAG":"NN"}]], greedy ='LONGEST') # be in force 
matcher.add("vnp", [[{"POS":"VERB"}, {"TAG":"NN"}, {"POS":"ADP"} ]], greedy ='LONGEST') # make use of, lay emphasis on
matcher.add("vp", [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":"ADP"} ]], greedy ='LONGEST') # abide by | distinguish from
matcher.add("vpp", [[{"POS":"VERB"}, {"POS":"ADP"}, {"POS":"ADP"} ]], greedy ='LONGEST') # live up to
matcher.add("pn", [[{"POS":"ADP", "DEP":"prep"} , {"TAG":"NN", "DEP":"pobj"}]], greedy ='LONGEST') # by force
matcher.add("pnp", [[{"POS":"ADP", "DEP":"prep"} , {"TAG":"NN", "DEP":"pobj"}, {"POS":"ADP", "DEP":"prep"}]], greedy ='LONGEST') # on account of
matcher.add("bapv", [[{"LEMMA":"be"} , {"TAG":{"IN": ["JJ"]}}, {"LEMMA":"to"}, {"POS":"VERB"}]], greedy ='LONGEST') # 
matcher.add("bvpv", [[{"LEMMA":"be"} , {"TAG":{"IN": ["VBN"]}}, {"LEMMA":"to"}, {"POS":"VERB"}]], greedy ='LONGEST') # be forced to go
matcher.add("bap", [[{"LEMMA":"be"} , {"TAG":{"IN": ["JJ"]}}, {"POS":"ADP"}]], greedy ='LONGEST')#be ignorant of
matcher.add("bvp", [[{"LEMMA":"be"} , {"TAG":{"IN": ["VBN"]}}, {"POS":"ADP"}]], greedy ='LONGEST') # be forced to
matcher.add("vop", [[{"POS":"VERB"} , {"TEXT": {"REGEX": "[a-z]+self$"}}, {"POS":"ADP"}]], greedy ='LONGEST')#throw oneself into
matcher.add("vtv", [[{"POS":"VERB"}, {"LEMMA":"to"}, {"POS":"VERB", "DEP":"xcomp"} ]], greedy ='LONGEST')
matcher.add("vg", [[{"POS":"VERB"},  {"TAG":"VBG", "DEP":"xcomp"} ]], greedy ='LONGEST')
matcher.add("vdpg", [[{"POS":"VERB"},  {"POS":"ADV"} ,  {"POS":"ADP"} ,  {"TAG":"VBG"} ]], greedy ='LONGEST') # look forward to seeing

postag = en.phrase_matcher({
"vpn": [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":"ADP"} , {"TAG":"NN"}]],  # be in force 
"vnp": [[{"POS":"VERB"}, {"TAG":"NN"}, {"POS":"ADP"} ]],  # make use of, lay emphasis on
"vp": [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":"ADP"} ]],  # abide by | distinguish from
"vpp": [[{"POS":"VERB"}, {"POS":"ADP"}, {"POS":"ADP"} ]], # live up to
"vpg": [[{"POS":"VERB"}, {"POS":"ADP"}, {"TAG":"VBG","DEP":"pcomp"} ]], # insisted on going
"pn": [[{"POS":"ADP", "DEP":"prep"} , {"TAG":"NN", "DEP":"pobj"}]],  # by force
"pnp": [[{"POS":"ADP", "DEP":"prep"} , {"TAG":"NN", "DEP":"pobj"}, {"POS":"ADP", "DEP":"prep"}]],  # on account of
"bapv": [[{"LEMMA":"be"} , {"TAG":{"IN": ["JJ"]}}, {"LEMMA":"to"}, {"POS":"VERB"}]],  # 
"bvpv": [[{"LEMMA":"be"} , {"TAG":{"IN": ["VBN"]}}, {"LEMMA":"to"}, {"POS":"VERB"}]],  # be forced to go
"bap": [[{"LEMMA":"be"} , {"TAG":{"IN": ["JJ"]}}, {"POS":"ADP"}]], #be ignorant of
"bvp": [[{"LEMMA":"be"} , {"TAG":{"IN": ["VBN"]}}, {"POS":"ADP"}]],  # be forced to
"vop": [[{"POS":"VERB"} , {"TEXT": {"REGEX": "[a-z]+self$"}}, {"POS":"ADP"}]], #throw oneself into
"vtv": [[{"POS":"VERB"}, {"LEMMA":"to"}, {"POS":"VERB", "DEP":"xcomp"} ]], 
"vg": [[{"POS":"VERB"},  {"TAG":"VBG", "DEP":"xcomp"} ]], 
"vdpg": [[{"POS":"VERB"},  {"POS":"ADV"} ,  {"POS":"ADP"} ,  {"TAG":"VBG"} ]],  # look forward to seeing
})

skenp = Matcher(spacy.nlp.vocab) # I look up from my phone. look back on
skenp.add("vnpn", [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"ENT_TYPE":"NP"}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}]], greedy ='LONGEST') # remind _NP of _NP , bring _NP to life
skenp.add("vpnpn", [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}]], greedy ='LONGEST') # vary from _NP to _NP 
skenp.add("vppn", [[{"POS":"VERB"}, {"POS":"ADP"}, {"POS":"ADP"}, {"ENT_TYPE":"NP"} ]], greedy ='LONGEST') # live up to _NP
skenp.add("vdpn", [[{"POS":"VERB"}, {"POS":"ADV"}, {"POS":"ADP"}, {"ENT_TYPE":"NP"} ]], greedy ='LONGEST') # look back on _NP 
skenp.add("vn", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"} ]], greedy ='LONGEST')
skenp.add("vnn", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"ENT_TYPE":"NP"} ]], greedy ='LONGEST')
skenp.add("vna", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"POS":"ADJ"} ]], greedy ='LONGEST')
skenp.add("vntb", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}]], greedy ='LONGEST')# consider _NP _NP | _NP _ADJ | _NP to be 
skenp.add("vntv", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"POS":"VERB"}]], greedy ='LONGEST')
skenp.add("vntbn", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}, {"ENT_TYPE":"NP"}]], greedy ='LONGEST')
skenp.add("vntba", [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}, {"POS":"ADJ"}]], greedy ='LONGEST')

ske_np = en.phrase_matcher({
"vnpn": [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"ENT_TYPE":"NP"}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}]],  # remind _NP of _NP , bring _NP to life
"vpnpn": [[{"POS":"VERB","TAG": {"NOT_IN": ["VBN"]}}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}, {"POS":{"IN": ["ADP"]}}, {"ENT_TYPE":"NP"}]],  # vary from _NP to _NP 
"vppn": [[{"POS":"VERB"}, {"POS":"ADP"}, {"POS":"ADP"}, {"ENT_TYPE":"NP"} ]],  # live up to _NP
"vdpn": [[{"POS":"VERB"}, {"POS":"ADV"}, {"POS":"ADP"}, {"ENT_TYPE":"NP"} ]],  # look back on _NP 
"vn": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"} ]], 
"vnn": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"ENT_TYPE":"NP"} ]], 
"vna": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"POS":"ADJ"} ]], 
"vne": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"TAG":"VBN"} ]], # leave it kept 
"vntb": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}]], # consider _NP _NP | _NP _ADJ | _NP to be 
"vntv": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"POS":"VERB"}]],
"vntbn": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}, {"ENT_TYPE":"NP"}]], 
"vntba": [[{"POS":"VERB"}, {"ENT_TYPE":"NP"}, {"LEMMA":"to"} , {"LEMMA":"be"}, {"POS":"ADJ"}]],
})

span_NP = lambda sp: " ".join([ "_NP" if t.ent_type_ == 'NP' else t.lemma_ for t in sp])

def merge_np(doc):
	with doc.retokenize() as retokenizer:
		for np in doc.noun_chunks:
			attrs = {"tag": np.root.tag, "dep": np.root.dep, "ent_type": "NP", "lemma":doc[np.end-1].lemma} # , "lemma":doc[np.end-1].lemma | added 2022.7.26
			retokenizer.merge(np, attrs=attrs) 
	return doc

def run(infile, outfile:str=None, batch:int=10000):
	''' c4-train.00604-of-01024.docjsonlg.3.4.1.gz -> c4-train.00604-of-01024.chksi  '''
	if outfile is None: outfile = infile.strip('.').split('.docjson' if '.docjson' in infile else '.')[0].strip('/') + "-xp.naclite" 
	if Path(f"{outfile}").exists(): os.remove(outfile)
	print ("started:", infile ,  ' -> ',  outfile, flush=True)

	conn  =	sqlite3.connect(outfile, check_same_thread=False) 
	conn.execute("create table nac( name varchar(64) not null , attr varchar(64) not null, count int not null default 0, primary key(name, attr) ) without rowid") #conn.execute("create table if not exists si( s varchar(64) not null primary key, i int not null default 0) without rowid")
	conn.execute('PRAGMA synchronous=OFF')
	conn.execute('PRAGMA case_sensitive_like = 1')
	conn.commit()
	add = lambda name, attr:  conn.execute(f"INSERT INTO nac(name, attr,count) VALUES(?,?,?) ON CONFLICT(name, attr) DO UPDATE SET count = count + 1", (name, attr,1))

	def submit( doc, matcher):
		from dic.lex_lemma import lex_lemma
		for name, start, end in matcher(doc):
			try:
				tag = spacy.nlp.vocab[name].text
				chk = doc[start].lemma_ + " " + doc[start+1:end].text
				if tag.startswith("v"): add( doc[start].lemma_ + f":VERB", tag )

				if tag == 'pn': # into force 
					add( doc[start+1].text.lower() + f":NOUN:{tag}", chk )
					add( doc[start+1].text.lower() + f":NOUN", tag )
				elif tag == 'vpn': # come into force 
					add( doc[start].lemma_ + f":VERB:{tag}", chk )
					add( doc[end - 1].text.lower() + f":NOUN:{tag}", chk ) # check boundary ? 
					add( doc[end - 1].text.lower() + f":NOUN", tag )
				elif tag == 'vnp': # make use of 
					add( doc[start].lemma_ + f":VERB:{tag}", chk )
					add( doc[start+1].lemma_ + f":NOUN:{tag}", chk )
					add( doc[start+1].lemma_ + f":NOUN", tag )
				elif tag in ('vpp', 'vp','vdpg'): # abide by
					add( doc[start].lemma_ + f":VERB:{tag}", doc[start:end].lemma_ )
				elif tag in ('vtv', 'vg'): 
					add( doc[start].lemma_ + f":VERB:{tag}", doc[start].lemma_ + " " + doc[start+1:end].text )
				elif tag in ('vop'): # devote oneself to
					add( doc[start].lemma_ + f":VERB:{tag}", doc[start].lemma_  + " oneself " + doc[start+2].text)
				elif tag in ('vnpn', 'vppn','vdpn', 'vn','vna','vnn','vntb','vntv','vntbn','vntba'): # remind _NP of _NP
					add( doc[start].lemma_ + f":VERB:{tag}", span_NP(doc[start:end]) )
				elif tag == 'bvp':  # be forced to , forced => force 
					add( lex_lemma.get(doc[start+1].text.lower(),doc[start+1].text.lower()) + f":VERB:{tag}", chk )
					add( lex_lemma.get(doc[start+1].text.lower(),doc[start+1].text.lower()) + f":VERB", tag )
				elif tag in ('bap'):
					add( doc[start+1].lemma_ + f":ADJ:{tag}", chk )
					add( doc[start+1].lemma_ + f":ADJ", tag )
				elif tag in ('bapv'):
					add( doc[start+1].lemma_ + f":ADJ:{tag}", doc[start].lemma_  + " " + doc[start+1:end-1].text + " _VERB" ) #
					add( doc[start+1].lemma_ + f":ADJ", tag )
				elif tag in ('bvpv'):
					add( doc[start+1].lemma_ + f":VERB:{tag}", doc[start].lemma_  + " " + doc[start+1:end-1].text + " _VERB" ) # be forced to _VERB
					add( doc[start+1].lemma_ + f":VERB", tag )
				elif tag == 'pnp': # on account of 
					add( doc[start+1].lemma_ + f":NOUN:{tag}", chk )
					add( doc[start+1].lemma_ + f":NOUN", tag )
				else:
					add( doc[start].lemma_ + f":X:{tag}", chk ) ## what is it? 
			except Exception as e:
				print ("ex:", e, name, start, end) 

	start = time.time()
	for sid, line in enumerate(fileinput.input(infile,openhook=fileinput.hook_compressed)): #356317 docs of each doc file
		try:
			arr = json.loads(line.strip()) 
			doc = spacy.from_json(arr) 
			[ add(f"{t.head.lemma_}:{t.head.pos_}", "vc") for t in doc if t.dep_ == 'ccomp' and t.head.pos_ == 'VERB' ]
			[ ( add(t.lemma_, t.pos_), add(f"{t.lemma_}:{t.pos_}", t.tag_))  for t in doc if t.pos_ in ('VERB','NOUN','ADJ','ADV') ]

			submit(doc, matcher) 
			merge_np(doc) 
			submit(doc, skenp) 
			if (sid+1) % batch == 0 : 
				print (f"[{infile} -> {outfile}] sid = {sid}, \t| ", round(time.time() - start,1), flush=True)
				conn.commit()
		except Exception as e:
			print ("ex:", e, sid, line[0:30]) 
	conn.commit()
	print(f"{infile} is finished, \t| using: ", time.time() - start) 

if __name__	== '__main__':
	import fire 
	fire.Fire(run)

'''
sqlite> create table if not exists si( s varchar(64) not null primary key, i int not null default 0) without rowid;
sqlite> insert into si select name, sum(count) from nac group by name; 
'''