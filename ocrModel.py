#[   [[1.0, 1.0], [28.0, 1.0], [28.0, 12.0], [1.0, 12.0]], 
#    ('P:0/1', 0.8532305955886841)]
class OcrModel(object):
    def __init__(self, R) -> None:
        rect = R[0]
        self.center = (rect[0][0] + (rect[1][0] - rect[0][0])*0.5, rect[0][1] + (rect[2][1] - rect[0][1])*0.5)
        self.text = R[1][0]
        self.p = R[1][1]