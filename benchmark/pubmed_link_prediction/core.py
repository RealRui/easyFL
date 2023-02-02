from torch_geometric.datasets import Planetoid

from benchmark.toolkits.graph.horizontal.link_prediction import *

TaskCalculator = LinkPredicitonTaskCalculator
class TaskGenerator(LinkPredicitonTaskGenenerator):
    def __init__(self, *args, **kwargs):
        super(TaskGenerator, self).__init__(benchmark='pubmed_link_prediction',rawdata_path='./benchmark/RAW_DATA/PUBMED',
                                            builtin_class=Planetoid, dataset_name='Pubmed', num_clients=10)

class TaskPipe(LinkPredicitonTaskPipe):
    def __init__(self, task_name):
        super(TaskPipe, self).__init__(task_name, Planetoid, transform=None)