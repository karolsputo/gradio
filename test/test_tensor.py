from main import Tensor

def test_tensor():
    data = ["1", "2", "3"]
    tensor = Tensor(data)
    assert len(data) == len(tensor.data)