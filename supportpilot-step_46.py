# === Stage 46: Add a schema version field and migration helper ===
# Project: SupportPilot
SCHEMA_VERSION = 2


def migrate_to_v2(store: dict) -> None:
    """Migrate from v1 (no schema field, single 'status' string) to v2.

    In v1 every request used ``status`` for its lifecycle and a flat set of
    extra keys (e.g. ``priority``, ``category``).  We preserve them on the
    object, rename ``status`` into ``state`` (open / resolved), move the old
    ``priority`` and ``category`` fields onto an ``attributes`` dict so that
    older code still reads from a known location, then stamp the new schema
    version.

    The migration is intentionally forgiving: unknown keys are just kept on
    the object so nothing useful ever disappears.
    """
    old = store.get("requests", [])
    for req in old:
        if "schema_version" in req:
            continue  # already migrated, skip
        state = req.pop("status")
        if state == "resolved":
            req.setdefault("state", "resolved")
        else:
            req["state"] = "open"

        attrs = {}
        for key in ("priority", "category"):
            if key in req:
                attrs[key] = req.pop(key)
        if not attrs:
            attrs = None  # keep JSON clean when nothing extra was set
        req["attributes"] = attrs

    store["schema_version"] = SCHEMA_VERSION
