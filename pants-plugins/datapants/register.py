
import pants.engine.rules
import pants.engine.goal
import pants.engine.target
import pants.engine.console


class TableFileField(pants.engine.target.StringField):
    help = "The source file of the dataset"

class Table(pants.engine.target.Target):
    alias = "table"
    core_fields = (
            *pants.engine.target.COMMON_TARGET_FIELDS,
            TableFileField,
        )

class ComputationSubsystem(pants.engine.goal.GoalSubsystem):
    name = "compute"
    help = "A subsystem for doing computations."

class Computation(pants.engine.goal.Goal):
    subsystem_cls = ComputationSubsystem
    environment_behavior = pants.engine.goal.Goal.EnvironmentBehavior.LOCAL_ONLY

@pants.engine.rules.goal_rule()
def compute(console: pants.engine.console.Console) -> Computation:
    console.print_stdout(console.green("Computing..."))
    return Computation(exit_code = 0)

def rules():
    return pants.engine.rules.collect_rules()
