# Grafana Cloud Connector — Connector Discovery

**Vendor API Baseline:** https://grafana.com

## Архитектура API
- **Базовый адрес:** `https://<org>.grafana.net/api`
- **Протокол:** REST / HTTPS (JSON)
- **Аутентификация:** Grafana Service Account Token (Authorization: Bearer <token>)
- **Ключевые эндпоинты:**
  - дашборды (/dashboards/db)
  - источники данных (/datasources)
  - правила алертов (/v1/provisioning/alert-rules)
- **Тестовая точка проверки подключения:** `GET /api/org`.
