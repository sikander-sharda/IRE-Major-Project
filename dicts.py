
'''f = open("Domains.txt", "r")
g = open("domains.txt", "w")
t = []
for line in f.readlines():
	t.append(line.lower())
for item in t:
	g.write("\"%s\"\n"% item)

'''


frameworks = {
"babel.js":["js",0], 
"node.js":["js",0],
"swift": ["js",0],
"go":["js",0],
"typescript":["js",0],
"haskel":["js",0],
"closure":["js",0],
"angular.js":["js",0],
"angular":["js",0],
"react":["js",0],
"polymer":["js",0],
"ember.js":["js",0],
"vue.js":["js",0],
"bootstrap":["html",0],
"bootstrap":["css",0],
"sass":["html",0],
"foundation":["html",0],
"less":["html",0],
"symfony":["php",0],
"zend":["php",0],
"laravel":["php",0],
"lumen":["php",0],
"slim":["php",0],
"django":["python",0],
"flask":["python",0],
"rails":["ruby",0],
"sinatra":["ruby",0],
"play":["java",0],
"spark":["java",0],
"node.js":["js",0],
"express":["js",0],
"hapi":["js",0],
"sails.js":["js",0],
"revel":["js",0],
"aws":["js",0],
"lambda":["js",0],
"ionic":["js",0],
"meteor":["js",0],
"web2py":["python", 0]
}

modules={
"scikit":["python", 0],
"sklearn":["python", 0],
	"wxpython":["python",0],
	"pygtk":["python",0],
	"pyqt":["python",0],
	"pmw":["python",0],
	"tkinter":["python",0],
"tix":["python",0],
"mysqldb":["python",0],
"pygresql":["python",0],
"gadfly":["python",0],

"sqlalchemy":["python",0],

"psycopg":["python",0],

"kinterbasdb":["python",0],

"cx_oracle":["python",0],

"pysqlite":["python",0],
"msnlib":["python",0],
"pymsn":["python",0],
"msnp":["python",0],
"twisted":["python",0],
"pil":["python",0],

"gdmodule":["python",0],

"videocapture":["python",0],
"scipy":["python",0],
"numpy":["python",0],



"numarray":["python",0],



"matplotlib":["python",0],

"pygame":["python",0],

"pyglet":["python",0],

"pysoy":["python",0],

"pyopengl":["python",0],

"jabberpy":["python",0],

"scrape":["python",0],

"beautifulsoup":["python",0],
"beautiful soup":["python",0],

"pythonweb":["python",0],

"mechanize":["python",0],

"geoname.py":["python",0],

"pyserial":["python",0],

"uspp":["python",0],

"pyparallel":["python",0],

"pyusb":["python",0],

"ctypes":["python",0],

"pywin32":["python",0],

"pywinauto":["python",0],

"pyrtf":["python",0],

"wmi":["python",0],

"pymo":["python",0],

"pys60":["python",0],

"pysoundic":["python",0],

"pymedia":["python",0],

"fmod":["python",0],

"pymidi":["python",0],

"libgmail":["python",0],
"pygoogle":["python",0],
"pyexpect":["python",0],
"pywordnet":["python",0],

"cmd":["python",0],

"vpython":["python",0],
"requests":["python",0],
"scrapy":["python",0],
"wxpython":["python",0],
"pillow":["python",0],
"sqlalchemy":["python",0],
"beautiful":["python",0],
"soup":["python",0],
"twisted":["python",0],
"numpy":["python",0],
"scipy":["python",0],
"mathplotlib":["python",0],
"pygame":["python",0],
"pyglet":["python",0],
"pyqt":["python",0],
"pygtk":["python",0],
"pywin32":["python",0],
"nltk":["python",0],
"nose":["python",0],
"sympy":["python",0],
"spacy":["python",0],
"dispy":["python",0],
"pyscp":["python",0],
"dopy":["python",0],
"apache":["java",0],
"freeling":["java",0],
"opennlp":["java",0],
"lingpipe":["java",0],
"weka":["java",0],
"rapid miner":["java",0],
"elki":["java",0],
"moa":["java",0],
"apache samoa":["java",0],
"tensorflow":["python",0],
"theano":["python",0],
"pylearn2":["python",0],
"pyevolve":["python",0],
"nupic":["python",0],
"pattern":["python",0],
"caffe":["python",0],
"nilearn":["python",0],
"fuel":["python",0],
"bob":["python",0],
"skdata":["python",0],
"milk":["python",0],
"iepy":["python",0],
"quepy":["python",0],
"hebel":["python",0],
"mlxtend":["python",0],
"nolearn":["python",0],
"ramp":["python",0],
"feature forge":["python",0],
"rep":["python",0],
"python-elm":["python",0],
"pythonxy":["python",0],
"xcs":["python",0],
"pyml":["python",0],
"mlpy":["python",0],
"orange":["python",0],
"spearmint":["python",0],
"crab":["python",0],
"pymc":["python",0],
"shogun":["python",0],
"pymvpa":["python",0],
"apache":["java",0],
"jsat":["java",0],
"mllib":["java",0],
"mallet":["java",0],
"mahout":["java",0],
"ipython":["python",0],
}

domains={
"algorithms":0,
"artificial intelligence":0,
"complexity and advanced algorithms":0,
"compilers":0,
"introduction to databases":0,
"database systems":0,
"data warehousing and data mining":0,
"advances in database systems":0,
"advances in data mining":0,
"computer networks":0,
"advanced computer networks":0,
"graphics":0,
"statistical methods in ai":0,
"image processing":0,
"machine learning":0,
"computer vision":0,
"natural language processing":0,
"nlp":0,
"natural language processing 2":0,
"natural language applications":0,
"natural language dialog systems":0,
"information retrieval and extraction":0,
"ire":0,
"principles of programming languages":0,
"intro to robotics: machines & control":0,
"embedded robotics":0,
"mobile robotics":0,
"multi agent systems":0,
"introduction to cognitive science":0,
"computational geometry":0,
"cryptography and network security":0,
"topics in information security":0,
"systems and network security":0,
"optimization methods":0,
"digital signal analysis & applications":0,
"principles of information security":0,
"software engineering":0,
}

languages={
    "(visual) basic": [
        0,
        0
    ],
    "(visual) foxpro": [
        0,
        0
    ],
    "css": [
        0,
        0
    ],
    ".net": [
        0,
        0
    ],
    "4th dimension/4d": [
        0,
        0
    ],
    "abap": [
        0,
        0
    ],
    "abc": [
        0,
        0
    ],
    "actionscript": [
        0,
        0
    ],
    "ada": [
        0,
        0
    ],
    "agilent vee": [
        0,
        0
    ],
    "algol": [
        0,
        0
    ],
    "alice": [
        0,
        0
    ],
    "angelscript": [
        0,
        0
    ],
    "apex": [
        0,
        0
    ],
    "apl": [
        0,
        0
    ],
    "applescript": [
        0,
        0
    ],
    "arc": [
        0,
        0
    ],
    "arduino": [
        0,
        0
    ],
    "asp": [
        0,
        0
    ],
    "aspectj": [
        0,
        0
    ],
    "assembly": [
        0,
        0
    ],
    "atlas": [
        0,
        0
    ],
    "augeas": [
        0,
        0
    ],
    "autohotkey": [
        0,
        0
    ],
    "autoit": [
        0,
        0
    ],
    "autolisp": [
        0,
        0
    ],
    "automator": [
        0,
        0
    ],
    "avenue": [
        0,
        0
    ],
    "awk": [
        0,
        0
    ],
    "bash": [
        0,
        0
    ],
    "bc": [
        0,
        0
    ],
    "bcpl": [
        0,
        0
    ],
    "beta": [
        0,
        0
    ],
    "blitzmax": [
        0,
        0
    ],
    "boo": [
        0,
        0
    ],
    "bourne shell": [
        0,
        0
    ],
    "bro": [
        0,
        0
    ],
    "c": [
        0,
        0
    ],
    "c shell": [
        0,
        0
    ],
    "c#": [
        0,
        0
    ],
    "c++": [
        0,
        0
    ],
    "cli": [
        0,
        0
    ],
    "c-omega": [
        0,
        0
    ],
    "caml": [
        0,
        0
    ],
    "ceylon": [
        0,
        0
    ],
    "cfml": [
        0,
        0
    ],
    "cg": [
        0,
        0
    ],
    "ch": [
        0,
        0
    ],
    "chill": [
        0,
        0
    ],
    "cil": [
        0,
        0
    ],
    "cl (os/400)": [
        0,
        0
    ],
    "clarion": [
        0,
        0
    ],
    "clean": [
        0,
        0
    ],
    "clipper": [
        0,
        0
    ],
    "clojure": [
        0,
        0
    ],
    "clu": [
        0,
        0
    ],
    "cobol": [
        0,
        0
    ],
    "cobra": [
        0,
        0
    ],
    "coffeescript": [
        0,
        0
    ],
    "coldfusion": [
        0,
        0
    ],
    "comal": [
        0,
        0
    ],
    "common lisp": [
        0,
        0
    ],
    "coq": [
        0,
        0
    ],
    "cpp": [
        0,
        0
    ],
    "ct": [
        0,
        0
    ],
    "curl": [
        0,
        0
    ],
    "d": [
        0,
        0
    ],
    "dart": [
        0,
        0
    ],
    "dcl": [
        0,
        0
    ],
    "dcpu-16 asm": [
        0,
        0
    ],
    "delphi/object pascal": [
        0,
        0
    ],
    "dibol": [
        0,
        0
    ],
    "dylan": [
        0,
        0
    ],
    "e": [
        0,
        0
    ],
    "ec": [
        0,
        0
    ],
    "ecl": [
        0,
        0
    ],
    "ecmascript": [
        0,
        0
    ],
    "egl": [
        0,
        0
    ],
    "eiffel": [
        0,
        0
    ],
    "elixir": [
        0,
        0
    ],
    "emacs lisp": [
        0,
        0
    ],
    "erlang": [
        0,
        0
    ],
    "etoys": [
        0,
        0
    ],
    "euphoria": [
        0,
        0
    ],
    "exec": [
        0,
        0
    ],
    "f#": [
        0,
        0
    ],
    "factor": [
        0,
        0
    ],
    "falcon": [
        0,
        0
    ],
    "fancy": [
        0,
        0
    ],
    "fantom": [
        0,
        0
    ],
    "felix": [
        0,
        0
    ],
    "forth": [
        0,
        0
    ],
    "fortran": [
        0,
        0
    ],
    "fortress": [
        0,
        0
    ],
    "gambas": [
        0,
        0
    ],
    "git": [
        0,
        0
    ],
    "gnu octave": [
        0,
        0
    ],
    "go": [
        0,
        0
    ],
    "google appsscript": [
        0,
        0
    ],
    "gosu": [
        0,
        0
    ],
    "groovy": [
        0,
        0
    ],
    "haskell": [
        0,
        0
    ],
    "haxe": [
        0,
        0
    ],
    "heron": [
        0,
        0
    ],
    "hpl": [
        0,
        0
    ],
    "hypertalk": [
        0,
        0
    ],
    "icon": [
        0,
        0
    ],
    "idl": [
        0,
        0
    ],
    "inform": [
        0,
        0
    ],
    "informix-4gl": [
        0,
        0
    ],
    "intercal": [
        0,
        0
    ],
    "io": [
        0,
        0
    ],
    "ioke": [
        0,
        0
    ],
    "j": [
        0,
        0
    ],
    "j#": [
        0,
        0
    ],
    "jade": [
        0,
        0
    ],
    "java": [
        0,
        0
    ],
    "java fx script": [
        0,
        0
    ],
    "javascript": [
        0,
        0
    ],
    "js": [
        0,
        0
    ],
    "jscript": [
        0,
        0
    ],
    "jscript.net": [
        0,
        0
    ],
    "julia": [
        0,
        0
    ],
    "jquery": [
        0,
        0
    ],
    "korn shell": [
        0,
        0
    ],
    "kotlin": [
        0,
        0
    ],
    "labview": [
        0,
        0
    ],
    "ladder logic": [
        0,
        0
    ],
    "lasso": [
        0,
        0
    ],
    "limbo": [
        0,
        0
    ],
    "lingo": [
        0,
        0
    ],
    "lisp": [
        0,
        0
    ],
    "logo": [
        0,
        0
    ],
    "logtalk": [
        0,
        0
    ],
    "lotusscript": [
        0,
        0
    ],
    "lpc": [
        0,
        0
    ],
    "lua": [
        0,
        0
    ],
    "lustre": [
        0,
        0
    ],
    "m4": [
        0,
        0
    ],
    "mad": [
        0,
        0
    ],
    "magic": [
        0,
        0
    ],
    "magik": [
        0,
        0
    ],
    "malbolge": [
        0,
        0
    ],
    "mantis": [
        0,
        0
    ],
    "maple": [
        0,
        0
    ],
    "mathematica": [
        0,
        0
    ],
    "matlab": [
        0,
        0
    ],
    "max/msp": [
        0,
        0
    ],
    "maxscript": [
        0,
        0
    ],
    "mel": [
        0,
        0
    ],
    "mercury": [
        0,
        0
    ],
    "mirah": [
        0,
        0
    ],
    "miva": [
        0,
        0
    ],
    "ml": [
        0,
        0
    ],
    "modula-2": [
        0,
        0
    ],
    "modula-3": [
        0,
        0
    ],
    "monkey": [
        0,
        0
    ],
    "moo": [
        0,
        0
    ],
    "moto": [
        0,
        0
    ],
    "ms-dos batch": [
        0,
        0
    ],
    "mumps": [
        0,
        0
    ],
    "mysql": [
        0,
        0
    ],
    "natural": [
        0,
        0
    ],
    "nemerle": [
        0,
        0
    ],
    "nimrod": [
        0,
        0
    ],
    "nqc": [
        0,
        0
    ],
    "nsis": [
        0,
        0
    ],
    "nu": [
        0,
        0
    ],
    "nxt-g": [
        0,
        0
    ],
    "oberon": [
        0,
        0
    ],
    "object rexx": [
        0,
        0
    ],
    "objective-c": [
        0,
        0
    ],
    "objective-j": [
        0,
        0
    ],
    "ocaml": [
        0,
        0
    ],
    "occam": [
        0,
        0
    ],
    "ooc": [
        0,
        0
    ],
    "opa": [
        0,
        0
    ],
    "opencl": [
        0,
        0
    ],
    "openedge abl": [
        0,
        0
    ],
    "opengl": [
        0,
        0
    ],
    "opl": [
        0,
        0
    ],
    "oz": [
        0,
        0
    ],
    "paradox": [
        0,
        0
    ],
    "parrot": [
        0,
        0
    ],
    "pascal": [
        0,
        0
    ],
    "perl": [
        0,
        0
    ],
    "php": [
        0,
        0
    ],
    "pike": [
        0,
        0
    ],
    "pilot": [
        0,
        0
    ],
    "pl/i": [
        0,
        0
    ],
    "pl/sql": [
        0,
        0
    ],
    "html": [
        0,
        0
    ],
    "pliant": [
        0,
        0
    ],
    "postscript": [
        0,
        0
    ],
    "pov-ray": [
        0,
        0
    ],
    "powerbasic": [
        0,
        0
    ],
    "powerscript": [
        0,
        0
    ],
    "powershell": [
        0,
        0
    ],
    "processing": [
        0,
        0
    ],
    "prolog": [
        0,
        0
    ],
    "puppet": [
        0,
        0
    ],
    "pure data": [
        0,
        0
    ],
    "python": [
        0,
        0
    ],
    "q": [
        0,
        0
    ],
    "r": [
        0,
        0
    ],
    "racket": [
        0,
        0
    ],
    "realbasic": [
        0,
        0
    ],
    "rebol": [
        0,
        0
    ],
    "revolution": [
        0,
        0
    ],
    "rexx": [
        0,
        0
    ],
    "rpg (os/400)": [
        0,
        0
    ],
    "ruby": [
        0,
        0
    ],
    "rust": [
        0,
        0
    ],
    "s": [
        0,
        0
    ],
    "s-plus": [
        0,
        0
    ],
    "sas": [
        0,
        0
    ],
    "sather": [
        0,
        0
    ],
    "scala": [
        0,
        0
    ],
    "scheme": [
        0,
        0
    ],
    "scilab": [
        0,
        0
    ],
    "scratch": [
        0,
        0
    ],
    "sed": [
        0,
        0
    ],
    "seed7": [
        0,
        0
    ],
    "self": [
        0,
        0
    ],
    "shell": [
        0,
        0
    ],
    "signal": [
        0,
        0
    ],
    "simula": [
        0,
        0
    ],
    "simulink": [
        0,
        0
    ],
    "slate": [
        0,
        0
    ],
    "smalltalk": [
        0,
        0
    ],
    "smarty": [
        0,
        0
    ],
    "spark": [
        0,
        0
    ],
    "spss": [
        0,
        0
    ],
    "sql": [
        0,
        0
    ],
    "sqr": [
        0,
        0
    ],
    "squeak": [
        0,
        0
    ],
    "squirrel": [
        0,
        0
    ],
    "standard ml": [
        0,
        0
    ],
    "suneido": [
        0,
        0
    ],
    "supercollider": [
        0,
        0
    ],
    "tacl": [
        0,
        0
    ],
    "tcl": [
        0,
        0
    ],
    "tex": [
        0,
        0
    ],
    "thinbasic": [
        0,
        0
    ],
    "tom": [
        0,
        0
    ],
    "transact-sql": [
        0,
        0
    ],
    "turing": [
        0,
        0
    ],
    "typescript": [
        0,
        0
    ],
    "vala/genie": [
        0,
        0
    ],
    "vbscript": [
        0,
        0
    ],
    "verilog": [
        0,
        0
    ],
    "vhdl": [
        0,
        0
    ],
    "viml": [
        0,
        0
    ],
    "visual basic": [
        0,
        0
    ],
    "webdna": [
        0,
        0
    ],
    "whitespace": [
        0,
        0
    ],
    "x10": [
        0,
        0
    ],
    "xbase": [
        0,
        0
    ],
    "xbase++": [
        0,
        0
    ],
    "xen": [
        0,
        0
    ],
    "xpl": [
        0,
        0
    ],
    "xquery": [
        0,
        0
    ],
    "xslt": [
        0,
        0
    ],
    "yacc": [
        0,
        0
    ],
    "yorick": [
        0,
        0
    ],
    "z shell": [
        0,
        0
    ]
}

ml = {
"scikit":"python",
"tensorflow":"python",
"theano":"python",
"pylearn2":"python",
"pyevolve":"python",
"nupic":"python",
"pattern":"python",
"caffe":"python",
"nilearn":"python",
"fuel":"python",
"bob":"python",
"skdata":"python",
"milk":"python",
"iepy":"python",
"quepy":"python",
"hebel":"python",
"mlxtend":"python",
"nolearn":"python",
"ramp":"python",
"feature forge":"python",
"rep":"python",
"python-elm":"python",
"pythonxy":"python",
"xcs":"python",
"pyml":"python",
"mlpy":"python",
"orange":"python",
"spearmint":"python",
"crab":"python",
"pymc":"python",
"shogun":"python",
"pymvpa":"python",
"weka":"java",
"rapid miner":"java",
"elki":"java",
"moa":"java",
"apache samoa":"java",
"apache":"java",
"jsat":"java",
"mllib":"java",
"mallet":"java",
"mahout":"java"
}

nlp = {
"nltk":"python",
"spacy":"python",
"apache":"java",
"freeling":"java",
"opennlp":"java",
"lingpipe":"java",
"nlp":0
}

webdev = {
"babel.js":"js", 
"node.js":"js",
"swift": "js",
"go":"js",
"typescript":"js",
"haskel":"js",
"closure":"js",
"angular.js":"js",
"angular":"js",
"react":"js",
"polymer":"js",
"ember.js":"js",
"vue.js":"js",
"bootstrap":"html",
"bootstrap":"css",
"sass":"html",
"foundation":"html",
"less":"html",
"symfony":"php",
"zend":"php",
"laravel":"php",
"lumen":"php",
"slim":"php",
"django":"python",
"flask":"python",
"rails":"ruby",
"sinatra":"ruby",
"play":"java",
"spark":"java",
"node.js":"js",
"express":"js",
"hapi":"js",
"sails.js":"js",
"revel":"js",
"aws":"js",
"lambda":"js",
"ionic":"js",
"meteor":"js",
"web2py":"python"
}

networking = {
"c":0,
"c++":0,
"perl":0,
"python":0,
"ruby":0,
"java":0,
"c#":0
}

distributed = {
"dispy":"python",
"pyscp":"python",
"dopy":"python",
"axum":0,
"elixir":0,
"erlang":0,
"janus":0,
"salsa":0,
"scala":0,
}

graphics = {
    "graphics":0,
    "opengl":0,
    "computer vision":0,
    "image processing":0
}
