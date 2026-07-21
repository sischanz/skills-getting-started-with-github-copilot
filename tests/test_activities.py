def test_get_activities_returns_all_activities_with_expected_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    for details in payload.values():
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
