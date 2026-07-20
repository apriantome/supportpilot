# === Stage 31: Add compact table rendering for long lists ===
# Project: SupportPilot
def render_compact_table(rows, columns):
    """Render a compact table for long lists with truncation."""
    header = " | ".join(columns)
    separator = "-+-".join(["-" * len(col) for col in columns])
    lines = [header, separator]
    for row in rows:
        formatted_row = []
        for col in columns:
            value = str(row.get(col, "") if isinstance(row, dict) else row[col])
            max_width = 30
            if len(value) > max_width:
                value = value[:max_width - 3] + "..."
            formatted_row.append(value.ljust(max_width))
        lines.append(" | ".join(formatted_row))
    return "\n".join(lines)
