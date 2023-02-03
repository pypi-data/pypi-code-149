from littlefieldpy.model.Paths import Paths


class CompletedJobs:
    def __init__(self, lf):
        self.lf = lf

    def count(self, x='all'):
        return self.lf.get_data_multi(Paths.COMPLETED_JOB_COUNT, x)

    def lead_times(self, x='all'):
        return self.lf.get_data_multi(Paths.LEAD_TIMES, x)

    def revenues(self, x='all'):
        return self.lf.get_data_multi(Paths.REVENUES, x)
