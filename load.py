import node
def bed_file(FILE, FILTER=None):
	G 	= {}
	ct 	= 0.
	N 	= 0.
	with open(FILE) as FH:
		for line in FH:
			if "#" not in line[0]:
				chrom,start, stop, INFO 	= line.strip("\n").split("\t")
				if chrom not in G:
					G[chrom] 	= list()

				if FILTER is None or not FILTER[chrom].searchInterval((int(start), int(stop))):
					G[chrom].append((int(start), int(stop), INFO))
					ct+=1
				N+=1
	return G
def refseq_table(FILE, TSS=True):
	G 	= {}
	with open(FILE) as FH:
		header 	= True
		for line in FH:
			if not header:
				N,chrom,strand, start, stop  	= line.strip("\n").split("\t")[1:6]
				if chrom not in G:
					G[chrom] 	= list()
				if TSS:
					if strand == "+":
						G[chrom].append((int(start)-500, int(start) + 500, N))
					else:
						G[chrom].append((int(stop)-500, int(stop) + 500, N))
				else:
					G[chrom].append((int(start) , int(stop)  , N))
			else:
				header=False
	FHW 	= open("/Users/joazofeifa/Lab/genome_files/TSS.bed","w")
	for chrom in G:
		for st, sp, N in G[chrom]:
			FHW.write(chrom + "\t" + str(st) + "\t" + str(sp) + "\t" + N + "\n" )
		G[chrom] 	= node.tree(G[chrom])
	FHW.close()
	return G
						
