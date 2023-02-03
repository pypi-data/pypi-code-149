from utilities.choices import ChoiceSet


class AppEnvironmentClusterEnvChoices(ChoiceSet):
    key = 'AppEnvironment.cluster_env'

    CHOICE_PRD = 'PRD'
    CHOICE_INT = 'INT'
    CHOICE_TST = 'TST'
    CHOICE_DEV = 'DEV'

    CHOICES = [
        (CHOICE_PRD, 'PRD', 'gray'),
        (CHOICE_INT, 'INT', 'green'),
        (CHOICE_TST, 'TST', 'cyan'),
        (CHOICE_DEV, 'DEV', 'blue'),
    ]