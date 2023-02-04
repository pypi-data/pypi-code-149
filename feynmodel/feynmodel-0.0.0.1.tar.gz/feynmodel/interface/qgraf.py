

# Convert a feynmodel to a qgraf model
# return the qgraf model as string
def feynmodel_to_qgraf(feynmodel):
	return_string = ""
	for p in feynmodel.particles:
		stat = ['+','+','-'][p.spin]
		return_string += f"[{p.name},{p.antiname},{stat}]\n" 
	pass