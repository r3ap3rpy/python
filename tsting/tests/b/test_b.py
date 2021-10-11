from pytest import mark

@mark.body
class BodyTest:
    @mark.b
    def test_body(self):
        assert True