# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: SupportPilot
def recommend_priority(request: dict) -> tuple[str, float]:
    """Assign a priority label and numeric score to a support request."""
    urgency = "low"
    score = 50.0
    if request.get("category") == "billing":
        urgency = "high"; score += 20
    elif request.get("category") in ("security", "outage"):
        urgency = "critical"; score += 40
    impact = request.get("impact", "medium")
    if impact == "high": score += 15; urgency = max(urgency, "high")
    elif impact == "low": score -= 10
    if request.get("sla_hours", 72) <= request.get("elapsed_minutes", 60):
        urgency = "critical"; score += 30
    return (urgency, round(score))
