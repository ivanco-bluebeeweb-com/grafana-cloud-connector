"""Extension declaration, capabilities, health check for Grafana Cloud Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "grafana-cloud-connector",
    version="0.1.0",
    display_name="Grafana Cloud",
    icon="icon.svg",
    capabilities=["grafana_cloud:manage"],
    description="Official Imperal connector for Grafana Cloud (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("grafana_cloud_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Grafana Cloud connection(s) configured." if count else "Not connected yet."
    }
