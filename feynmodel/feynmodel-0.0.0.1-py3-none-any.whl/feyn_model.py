

class FeynModel:
	all_particles = []
	all_vertices = []

	def add_particle(self, particle):
		if particle not in self.all_particles:
			self.all_particles.append(particle)

	def add_vertex(self, vertex):
		if vertex not in self.all_vertices:
			self.all_vertices.append(vertex)