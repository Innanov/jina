import pytest

from jina.flow import Flow
from tests import random_docs


@pytest.mark.parametrize('rest_api', [False, True])
def test_flow(rest_api):
    docs = random_docs(10)
    f = Flow(rest_api=rest_api).add(name='p1')

    with f:
        f.index(docs)
        assert f.num_pods == 2
        assert f._pod_nodes['p1'].num_peas == 1
        assert f.num_peas == 2


@pytest.mark.parametrize('rest_api', [False, True])
def test_flow_before(rest_api):
    docs = random_docs(10)
    f = Flow(rest_api=rest_api).add(uses_before='_pass', name='p1')

    with f:
        f.index(docs)
        assert f.num_pods == 2
        assert f._pod_nodes['p1'].num_peas == 2
        assert f.num_peas == 3


@pytest.mark.parametrize('rest_api', [False, True])
def test_flow_after(rest_api):
    docs = random_docs(10)
    f = Flow(rest_api=rest_api).add(uses_after='_pass', name='p1')

    with f:
        f.index(docs)
        assert f.num_pods == 2
        assert f._pod_nodes['p1'].num_peas == 2
        assert f.num_peas == 3


@pytest.mark.parametrize('rest_api', [False, True])
def test_flow_before_after(rest_api):
    docs = random_docs(10)
    f = Flow(rest_api=rest_api).add(uses_before='_pass', uses_after='_pass', name='p1')

    with f:
        f.index(docs)
        assert f.num_pods == 2
        assert f._pod_nodes['p1'].num_peas == 3
        assert f.num_peas == 4