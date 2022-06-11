from pm4py.objects.petri_net.importer import importer as pnml_importer
import pm4py as pm
from pm4py.algo.evaluation.replay_fitness import algorithm as replay_fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
for i in range(4):
    net, im, fm = pnml_importer.apply('code12/p{}.pnml'.format(i))
    log=pm.read_xes('code12/p{}.xes'.format(i))
    fitness1 = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)
    prec1 = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)
    fitness2 = replay_fitness_evaluator.apply(log, net, im, fm, variant=replay_fitness_evaluator.Variants.ALIGNMENT_BASED)
    prec2 = precision_evaluator.apply(log, net, im, fm, variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)
    print(fitness1['log_fitness'],fitness2)
    print(prec1,prec2)
    print("$$$$$$$$$$$")
print("***************************")