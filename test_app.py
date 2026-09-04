from app import app


def test_health_check():
    cliente = app.test_client()
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200  # nosec B101