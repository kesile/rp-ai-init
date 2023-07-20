from db.initDoc import initDoc
from axns.st import st
from axns.uq import uq
from axns.tc import text
from axns.fd import fd
from lib.init import gp
from lib.adv import adv, personas, summarize
from lib.upd import upd

parameters = initDoc()

uq = uq()

fd = fd()

post = text(gp(parameters))
st(uq, post, "inPo")

for i in range(3):
    feedback = ""
    feedback = feedback + text(adv(post, parameters, personas[i])) + "\n"

feedback = text(feedback, summarize)
st(uq, feedback, "inFe")

for i in range(fd):
    post = text(upd(post, feedback, parameters))
    st(uq, post, "rePo", i+1)
    for j in range(3):
        feedback = ""
        feedback = feedback + text(adv(post, parameters, personas[j])) + "\n"
    feedback = text(feedback, summarize)
    st(uq, feedback, "reFe", i+1)

post = text(upd(post, feedback, parameters))
st(True, post, "fiPo")