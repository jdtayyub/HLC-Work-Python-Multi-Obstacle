import Allen, Indu

class QSRs:

    _scene = []
    _types = []

    def __init__(self, scene, types):
        self._scene = scene
        self._types = types

    def compute_qsrs(self):
        all_qsrs = {}
        for type in self._types:
            if type == 'Allen':
                allen_rels = Allen.compute_allen_relations(self._scene)
                all_qsrs['allen-rels'] = allen_rels
            elif type == 'Indu':
                indu_rels = Indu.compute_Indu_relations(self._scene)
                all_qsrs['indu-rels'] = indu_rels

            # ... and add more QSRs here if needed to expand the feature space ...

        return all_qsrs


