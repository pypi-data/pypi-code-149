class PlayerDistanceModel(BaseModel):
    def __init__(self, pitch: Pitch):
        super().__init__(pitch)

        # initialize instance attributes
        self.player_distances_ = None

    def fit(self, xy1: XY, xy2: XY = None) -> None:
        """"""
        if not xy2:
            xy2 = xy1

        T = len(xy1)
        distances = np.full((T, xy1.N, xy2.N), np.nan)

        for t in range(T):
            distances[t] = cdist(xy1[t].reshape(-1, 2), xy2[t].reshape(-1, 2))

        self.player_distances_ = distances

    def get_player_distances(self):
        distances = InteractionProperty(
            self.player_distances_,
            name="stretch_index",
            framerate=5
        )

        return distances

