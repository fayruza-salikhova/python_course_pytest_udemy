import pytest
from src.models.company import Company

@pytest.fixture
def company() -> Company:
    return Company(name = "Fiver", stock_symbol = "FVRR")

def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")

@pytest.mark.parametrize(
    "company_name",
    ["TikTok", "Instagram", "Twitch"],
    ids = ["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"]

)
def test_parametrized(company_name: str) -> None:
    print(f"\nTest With {company_name}")

def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)
