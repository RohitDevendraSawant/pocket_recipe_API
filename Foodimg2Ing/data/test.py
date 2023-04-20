fn = "/content/instr_vocab.pkl"
p = os.path.join("/content/instr_vocab.pkl",fn)
print(p)
df = pkl.load(open(p,"rb"))