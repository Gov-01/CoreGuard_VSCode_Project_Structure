def is_manager(user_payload: dict) -> bool:
    return user_payload.get("role") == "manager"
