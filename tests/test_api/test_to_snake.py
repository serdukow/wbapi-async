import pytest

from wbapi.type import ApiResponse


@pytest.mark.unit
class TestToSnake:
    def test_simple_camel(self) -> None:
        r = ApiResponse({"nmId": 123})
        assert r.to_snake() == {"nm_id": 123}

    def test_multi_word(self) -> None:
        r = ApiResponse({"advertId": 1, "lastChangeDate": "2024-01-01"})
        assert r.to_snake() == {"advert_id": 1, "last_change_date": "2024-01-01"}

    def test_already_snake(self) -> None:
        r = ApiResponse({"rrd_id": 99, "date_from": "2024-01-01"})
        assert r.to_snake() == {"rrd_id": 99, "date_from": "2024-01-01"}

    def test_all_lowercase(self) -> None:
        r = ApiResponse({"next": 0, "limit": 10})
        assert r.to_snake() == {"next": 0, "limit": 10}

    def test_uppercase_abbreviation(self) -> None:
        # nmID → nm_id, not nm_i_d
        r = ApiResponse({"nmID": 123})
        assert r.to_snake() == {"nm_id": 123}

    def test_b2b(self) -> None:
        r = ApiResponse({"isB2B": True})
        assert r.to_snake() == {"is_b2_b": True}

    def test_leading_uppercase(self) -> None:
        r = ApiResponse({"OrderId": 1})
        assert r.to_snake() == {"order_id": 1}

    def test_nested_not_converted(self) -> None:
        r = ApiResponse({"orderId": 1, "meta": {"nmId": 2}})
        result = r.to_snake()
        assert result["order_id"] == 1
        assert result["meta"] == {"nmId": 2}

    def test_non_dict_returns_data(self) -> None:
        r = ApiResponse([1, 2, 3])
        assert r.to_snake() == [1, 2, 3]

    def test_empty_dict(self) -> None:
        r = ApiResponse({})
        assert r.to_snake() == {}

    def test_values_preserved(self) -> None:
        r = ApiResponse({"advertId": None, "nmId": 0, "name": ""})
        assert r.to_snake() == {"advert_id": None, "nm_id": 0, "name": ""}
