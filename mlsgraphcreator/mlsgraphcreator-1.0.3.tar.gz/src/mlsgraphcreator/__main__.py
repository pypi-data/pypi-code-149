from graphcreator import createGraph

def main():
	if len(sys.argv) > 1:
		fileName = pd.read_csv(os.path.join(workDir,sys.argv[1]))
	else:
		fileName = pd.read_csv(os.path.join(dataPath,'fgvt-steering-data.csv'))
	graphObject = createGraph(fileName)
	
if __name == "__main__":
	main()
