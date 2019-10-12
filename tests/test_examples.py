

def test_example_03():
    import pddlpy
    
    domprob = pddlpy.DomainProblem('examples-pddl/domain-03.pddl', 'examples-pddl/problem-03.pddl')
    
    assert { tuple(e.predicate) for e in domprob.initialstate() } == {('adjacent', 'loc2', 'loc1'), ('unloaded', 'robr'), ('atl', 'robr', 'loc1'), ('unloaded', 'robq'), ('in', 'conta', 'loc1'), ('atl', 'robq', 'loc2'), ('adjacent', 'loc1', 'loc2'), ('in', 'contb', 'loc2')}
    
    assert list(domprob.operators()) == ['move', 'load', 'unload']

    # groud_operator() returns a set
    #assert { list(domprob.ground_operator('move'))[0].precondition_pos == {('atl', 'robq', 'loc1'), ('adjacent', 'loc1', 'loc1')}


def test_example_ld01():
    import pddlpy
    
    domprob = pddlpy.DomainProblem('examples-pddl/domain-ld01.pddl', 'examples-pddl/problem-ld01.pddl')
